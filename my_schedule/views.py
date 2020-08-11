from django.shortcuts import render
from django.http import HttpResponse

from my_schedule.models import Schedule

# Create your views here.
def schedule_list(request):
    schedules = Schedule.objects.all()
    context = {'schedules': schedules}
    return render(request, 'my_schedule/schedule_list.html', context)