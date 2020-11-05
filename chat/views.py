from django.shortcuts import render, HttpResponse
from django.views.generic import View

def index(request):
    return render(request, 'chat/index.html', {})

class ChatRoom(View):
    template_name = 'chat/room.html'

    def get(self, request, *arg, **kwargs):
        print(request.build_absolute_uri())
        return HttpResponse(
            f'<script>alert(\'Please enter home page to type your name.\'); window.location = \'http://{request.get_host()}/\';</script>'
        )

    def post(self, request, *args, **kwargs):
        return render(request,
        self.template_name,
        {'name': request.POST.get('name', 'NoName')}
        )