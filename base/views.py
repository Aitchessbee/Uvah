from http.client import HTTPResponse
import json
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import CustomUser, Domain, Topic, Subtopic, Course
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
# from django.core import serializers
# from django.db.models import Q


# Create your views here.
def home(request):
    return redirect('roadmap')

def roadmap(request):
    # return render(request, 'base/home.html')
    domains = Domain.objects.all()
    # print(domains)
    # for i in domains:
    #     print(i)
    context = {"domains": domains}

    return render(request, 'base/roadmap.html', context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect("roadmap")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("roadmap")
        else:
            messages.info(request, "Try again! Email or Password is incorrect")
        

    return render(request, 'base/login.html')

def user_register(request):
    if request.user.is_authenticated:
        return redirect("roadmap")

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            form.save()
            new_user = authenticate(username=email, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect("roadmap")
    
    form = UserForm()
    context = {"form": form}

    return render(request, 'base/register.html', context)

def user_logout(request):
    logout(request)
    return redirect("roadmap")

def domain(request, domain_link):
    domain = Domain.objects.filter(domain_link=domain_link).first()

    topics = Topic.objects.filter(domain=domain)
    # print(topics)

    context = {"topics": topics, "domain": domain}

    return render(request, 'base/domain.html', context)

def topic(request, domain_link, topic_link):
    if request.method == "POST":
        print("request received")

        user = request.user

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        # print(body["course_id"])

        course = Course.objects.get(id=body["course_id"])
    
        print(body["action"])

        if body["action"] == "addBookmark":
            user.favorite_courses.add(course)
        else:
            user.favorite_courses.remove(course)

        user.save()

        return HttpResponse(status=200) 
        

    topic=Topic.objects.filter(topic_link=topic_link).first()

    subtopics = Subtopic.objects.filter(topic=topic)
    # courses = Course.objects.filter(subtopic_id__in=list(Topic.objects.filter(topic_name=topic).values_list('id', flat=True)))
    courses = Course.objects.filter(subtopic__in=subtopics, approved=True)
    favorite_courses = request.user.favorite_courses.filter(subtopic__in=subtopics)

    print(favorite_courses)

    # print(courses)
    # for i in courses:
    #     print(i.course_author)

    context = {"subtopics": subtopics, "courses": courses, "topic": topic, "favorite_courses": favorite_courses}

    return render(request, 'base/topic.html', context)

def get_topics(request):
    domain = request.GET['domain']
    print(domain)
    # topics = Topic.objects.filter(domain=Domain.objects.filter(domain_name=domain).first())
    topics = Topic.objects.filter(domain=Domain.objects.filter(domain_name=domain).first()).values_list('topic_name', flat=True)
    print(list(topics))
    # topics = Topic.objects.filter(domain=domain)
    # data = serializers.serialize('json', topics)
    # return HttpResponse(data, content_type='application/json')
    # return HttpResponse(list(topics), content_type='application/json')
    # return JsonResponse({"topics": list(topics)})
    return JsonResponse(list(topics), safe=False)
    
def get_subtopics(request):
    domain_inp = request.GET['domain']
    topic_inp = request.GET['topic']
    domain = Domain.objects.filter(domain_name=domain_inp).first()
    topic = Topic.objects.filter(topic_name=topic_inp, domain=domain).first()

    subtopics = Subtopic.objects.filter(domain=domain, topic=topic).values_list('subtopic_name', flat=True)

    return JsonResponse(list(subtopics), safe=False)


def webdev(request):
    return render(request, 'base/webdev.html')

def frontend(request):
    return render(request, 'base/frontend.html')

def backend(request):
    return render(request, 'base/backend.html')

def profile(request):
    user = request.user

    suggested_courses = Course.objects.filter(submitted_by=user)
    favorite_courses = user.favorite_courses.all()

    context = {"user": user, "courses": suggested_courses, "favorite_courses": favorite_courses}
    return render(request, 'base/profile.html', context)

def submitCourse(request):
    domains = Domain.objects.all()
    topics = Topic.objects.all()
    subtopics = Subtopic.objects.all()

    if request.method == "POST":
        user = request.user

        course_title = request.POST.get('course-title')
        course_author = request.POST.get('course-author')
        course_link = request.POST.get('course-link')

        domain_name = request.POST.get('domain')
        domain = Domain.objects.filter(domain_name=domain_name).first()

        topic_name = request.POST.get('topic')
        topic = Topic.objects.filter(topic_name=topic_name).first()

        subtopic_name = request.POST.get('subtopic')
        subtopic = Subtopic.objects.filter(subtopic_name=subtopic_name, domain=domain, topic=topic).first()

        Course.objects.create(
            submitted_by = user,
            subtopic = subtopic,
            course_title = course_title,
            course_author = course_author,
            course_link = course_link
        )

    context = {"domains": domains, "topics": topics, "subtopics": subtopics}

    return render(request, 'base/submitCourse.html', context)

def test(request):
    data = User.objects.all()
    
    context = {"users": data}

    return render(request, "base/test.html", context)

def contactUs(request):
    return render(request, "base/contactus.html")

def leaderboard(request):
    users = CustomUser.objects.filter(courses_submitted__gte=1).order_by('-courses_submitted', "username")
    # print(users)
    
    context = {
        "users": users,
    }

    return render(request, "base/ranking.html", context)

def course_approval(request):
    if request.user.is_superuser == False:
        return redirect("roadmap")

    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        # print(body["course_id"])

        if body["action"] == "approve":
            course = Course.objects.get(id=body["course_id"])
            course.approved = True
            course.save()

            user = course.submitted_by
            user.courses_submitted = user.courses_submitted + 1
            user.save()

        else:
            course = Course.objects.get(id=body["course_id"])
            course.delete()


    unapproved_courses = Course.objects.filter(approved=False)

    context = {"unapproved_courses": unapproved_courses}

    
    return render(request, "base/approval.html", context)

