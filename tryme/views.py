# try/views.py

from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.shortcuts import render
from .models import Post
from django.views import View

from .forms import NameForm


def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })

def nothing_here(request):
    return HttpResponse("Nothing Here!")

def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {
        'post_list': post_list,
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})

def addapost(request):
    post_list = Post.objects.all()
    counting = 1
    for post in post_list:
        counting += 1
    Post.objects.create(title="No: " + str(counting) + " post is about " + 
                        chr(64+counting), content=chr(64+counting), location="VIU")
    return HttpResponseRedirect('/')

def testforms(request):
    return render(request, 'testforms.html', {'form': NameForm, 'formn': '', 'yourname': ''})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse(request.POST['your_name']) #shows the form atribute named 'your_name'

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return HttpResponse("F")
    #return render(request, 'name.html', {'form': form})

class ClassFormView(View):
    form_class = NameForm
    the_template = 'testforms.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.the_template, {'form' : 'START','formn' : form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
             #process form cleaned data here
             answer = request.POST['your_name']
             answer = answer.replace('\\','')
             answer = answer.replace('<','')
             answer = answer.replace('>','')
             return render(request, self.the_template, {'form' : 'START', 'yourname' : answer})
        return render(request, self.the_template, {'form' : 'START','formn' : form})

