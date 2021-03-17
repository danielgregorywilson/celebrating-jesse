import os


class CorsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        if os.getenv('GAE_APPLICATION', None):
            # Production allowed request origins
            # response["Access-Control-Allow-Origin"] = "http://celebrating-jesse-frontend.s3-website-us-west-2.amazonaws.com"
            # response["Access-Control-Allow-Origin"] = "http://celebratingjesse.net.s3-website-us-west-2.amazonaws.com"
            response["Access-Control-Allow-Origin"] = "http://celebratingjesse.net"
        else:
            # Local development allowed request origins
            # response["Access-Control-Allow-Origin"] = "http://localhost:8080"
            response["Access-Control-Allow-Origin"] = "http://jesse-memorial:8080"
        
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response["Access-Control-Allow-Methods"] = "GET, POST, PATCH, PUT, DELETE, OPTIONS"
        return response
