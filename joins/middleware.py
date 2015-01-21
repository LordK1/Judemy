__author__ = 'k1'


class JoinsMiddleware():
    def process_request(self, request):
        print( "META : " + str(request.META), self)