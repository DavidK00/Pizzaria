from django.shortcuts import render, redirect
from .models import Topic 
from .forms import TopicForm
from .models import Topic


# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')


def topics(request):
    topics = Topic.objects.all()

    context = {'topics':topics} #passing the entire object to context
     
    return render(request, 'MainApp/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')

    context = {'topic': topic, 'entries':entries} #use key on html page, value is object in view file

    return render(request,'MainApp/topic.html', context) #context is dictionary

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm
    else:
        form =TopicForm(data=request.POST)

        if form.is_valid():
            new_topic = form.save()

            return redirect('MainApp:topics')

    context = {'form': form}
    return render(request, 'MainApp/new_topic.html', context)


    

