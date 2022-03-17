
import re
from xml import dom
from .serializers import SnapUrlSerializer
from .models import SnapUrl
from django.conf import settings
import uuid


def uniqueHash(id):
    map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    shortURL = ""
     
    # for each digit find the base 62
    while(id > 0):
        shortURL += map[id % 62]
        id //= 62
 
    # reversing the shortURL
    return shortURL[len(shortURL): : -1]


#Creates and stores a Unique Hashkey for a given url
def createHash(url):
    
    hashKey = uniqueHash(uuid.uuid1().time)
    data = {

        'hash': hashKey,
        'origin' : url,
        'url': f'{settings.APP_KEYS["Domain"]}{hashKey}'
    }

    serializer = SnapUrlSerializer(data = data)
    
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    return serializer.errors


#Returns the Origin URl for a given hashkey
def getOrigin(hashkey):

    try:
        qs = SnapUrl.objects.filter(hash = hashkey).get()
        return qs.origin
    except:
        return None

    

#Returns all objects stored
def getList():
    qs = SnapUrl.objects.all()
    serializer = SnapUrlSerializer(qs, many=True)
    return serializer.data
