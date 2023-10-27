from django.http import HttpResponse


class IPRestrictedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        client_ip = request.META.get('REMOTE_ADDR')
        print(client_ip)
        ip_address = [
            '127.0.0.1'
        ]
        if client_ip not in ip_address and request.path.find('admin') != -1:
            return HttpResponse('Permission denied!')
        response = self.get_response(request)
        return response
