#Post/views
#Dajngo
from django.shortcuts import render
from django.http import HttpResponse
#Utilities
from datetime import datetime

posts =[
    {
        'title':'Monot Blanc',
        'user':{
            'name': 'Alison Velastegui',
            'picture':'https://picsum.photos/200/200/?image=1036',

        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo':'https://picsum.photos/200/200/?image=1036',
    },
    {
        'title':'Via Lactea',
        'user':{
            'name': 'Alison Velastegui',
            'picture':'https://picsum.photos/200/200/?image=903',

        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo':'https://picsum.photos/200/200/?image=903',
    },
    {
        'title':'Nuevo Auditorio',
        'user':{
            'name': 'Alison Velastegui',
            'picture':'https://picsum.photos/200/200/?image=1076',

        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo':'https://picsum.photos/200/200/?image=1076',
    }
]
def list_post(request):
    """List existing posts"""
    return render(request,'posts/feed.html',{'posts':posts})
    