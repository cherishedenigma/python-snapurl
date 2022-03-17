Overview:
Given a URL, our service generates a shorter and unique alias of it. 
This is called a short link. This link should be short enough to be easily copied and pasted into applications.
When users access a short link, this service should redirect them to the original link.
The application is written in python.

API Reference

Before use, update DOMAIN setting variable in settings.py to the server you are running this service on.

Example: 
POST http://<DOMAIN>/add/
{	
	“origin”: “https://www.google.com/search?q=dell+benefits”
}

Returns string of the shorten URL:
“http://<DOMAIN>/kpgv9iUODV”

GET http://<DOMAIN>/kpgv9iUODV”
Redirects to  https://www.google.com/search?q=dell+benefits


Future Work:
Additional features we can expect are: 
Logging implementations.
Strict validation protocols and error handling.
Caching redirects for commonly used links.
Connectivity to a full service database management system.
Improving maximum origin URL capacity.
Adding secure web implementations on production server.
