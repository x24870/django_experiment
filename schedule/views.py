from django.shortcuts import render
from django.http import HttpResponse

from .models import Schedule

# Create your views here.
def schedule_list(request):
    schedules = Schedule.objects.all()
    context = {'schedules': schedules}
    return render(request, 'schedule/schedule_list.html', context)