#Post/views
#Dajngo
from django.shortcuts import render
from django.http import HttpResponse
#Utilities
from datetime import datetime

posts =[
    {
        'name':'Monot Blanc',
        'user': 'Alison Velastegui',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name':'Via Lactea',
        'user': 'Alison Velastegui',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=903',
    },
    {
        'name':'Nuevo Auditorio',
        'user': 'Alison Velastegui',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=1076',
    }
]
def list_post(request):
    """List existing posts"""
    content =[]
    for post in posts:
        content.append("""
        <p><strong>{name}</strong></p>
        <p><small>{user} -<i>{timestamp}</i></small></p>
        <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))
    