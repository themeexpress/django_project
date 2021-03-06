from django.shortcuts import render
from .models import Post
# Create your views here.
posts = [
    {
        'author':'kamrul',
        'title':'blog post one',
        'content': 'Now we know for certain that were using Python 3.7.3 and pip will update alongside it without any manual aliasing between versions.',
        'date_posted':'Augest 22, 2020'
    },
    {
        'author':'John kali',
        'title':'blog post two django',
        'content': 'Using Moshes recommendation to use a version manager (pyenv) enables us to easily accept future upgrades without getting confused about which Python we are running at a given time.',
        'date_posted':'Augest 22, 2020'
    }
    
]
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})