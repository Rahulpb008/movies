from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime
# Create your views here.

def wish(request):
    date=datetime.datetime.now()
    my_dict={'insert_date':date}
    return render(request,'temp1.html',context=my_dict)
def index(request):
    dt=datetime.datetime.now()
    name='Rahul'
    rollno='01'
    mark='100'
    dict={'date':dt,'name':name,'rollno':rollno,'mark':mark}
    return render(request,'temp2.html',context=dict)
def display(request):
    date=datetime.datetime.now()
    msg=('Hello Guest!!!very very Good')
    sde=int(date.strftime('%H'))
    if (sde<12):
        msg+='Morning'
    elif (sde>=12 and sde<=16.00):
        msg+='Afternoon'
    else:
        msg+='Night'
    dict={'date':date,'message':msg,}
    return render(request,'temp3.html',context=dict)
def movie(request):
    my_dict={'head_msg':'Movies Information',
    'sub_msg1':'Sonali slowly getting cured',
    'sub_msg2':'Bahubali-3 is just planning',
    'sub_msg3':'Salman Khan ready to marriage',
    'photo':'images/sunny.jpg'}
    return render(request,'temp5.html',context=my_dict)
def sports(request):
    my_dict={'head_msg':'Sports Information',
    'sub_msg1':'Anushka Sharma Firing Like anything',
    'sub_msg2':'Kohli updating in game anything can happend',
    'sub_msg3':'Worst Performance by India-Sehwag', }
    return render(request,'temp5.html',context=my_dict)
def politics(request):
    my_dict={'head_msg':'Politics Information',
    'sub_msg1':'Achhce Din Aaa gaya',
    'sub_msg2':'Rupee Value now 1$:70Rs',
    'sub_msg3':'In India Single Paisa Black money No more', }
    return render(request,'temp5.html',context=my_dict)
def indexnews(request):
    return render(request,'temp4.html')