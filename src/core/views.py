
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseRedirect
from rest_framework.decorators import api_view
from core.hashing import createHash, getList, getOrigin
from django.http.response import JsonResponse
from .serializers import PostSerializer

#API To accept incoming URL to shorten
@api_view(["POST"])
def core_add(request):
    serializer = PostSerializer(data = request.data)
    if serializer.is_valid():
        data = createHash(serializer.data.get("origin"))
        return JsonResponse(data.get("url"), safe=False)
    else:
        return HttpResponseBadRequest()

#API To redirect to Origin URL by hashkey. If hashkey is invalid, return not found.
@api_view(["GET"])
def redirect_view(request, hashkey):
    data = getOrigin(hashkey)
    if data != None :
        return HttpResponseRedirect(data)
    else:
        return HttpResponseNotFound()


#Test API to view all stored shorten urls
@api_view(["GET"])
def viewall(request):
    data = getList()
    return JsonResponse(data, safe=False)



    