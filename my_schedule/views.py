from django.shortcuts import render
from django.http import HttpResponse

from schedule.models import Calendar

from my_schedule.models import Schedule

# Create your views here.
def schedule_list(request):
    schedules = Schedule.objects.all()
    context = {'schedules': schedules}

    cal = Calendar.objects.all()
    print(cal)
    return render(request, 'my_schedule/schedule_list.html', context)