from django.shortcuts import render, redirect
import csv
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
from io import TextIOWrapper
from base.models import Domain, Topic, Subtopic, Course


# Create your views here.
def import_data(request):
    if request.user.is_superuser == False:
        return redirect("roadmap")

    if request.method == "POST":
        file = TextIOWrapper(request.FILES['file'].file, encoding=request.encoding)

        reader = csv.reader(file)

        # for row in reader:
        #     print(row)

        #     domain = Domain.objects.filter(domain_name = row[0])
        #     if domain:
        #         domain = Domain.objects.get(domain_name = row[0])
        #         topic = Topic.objects.filter(topic_name = row[1])

        #         if not topic:
        #             topic = Topic.objects.create(domain = domain, topic_name = row[1], topic_description = row[2], topic_link = row[3])
        #             topic.save()


        # for row in reader:
        #     print(row)

        #     domain = Domain.objects.filter(domain_name = row[0])
        #     if domain:
        #         domain = Domain.objects.get(domain_name = row[0])
        #         topic = Topic.objects.filter(topic_name = row[1])

        #         if topic:
        #             topic = Topic.objects.get(topic_name = row[1])
                    
        #             subtopic = Subtopic.objects.filter(subtopic_name = row[2])

        #             if not subtopic:
        #                 subtopic = Subtopic.objects.create(domain = domain, topic = topic, subtopic_name = row[2], subtopic_description = row[3], subtopic_link = row[4])
        #                 subtopic.save()


        for row in reader:
            print(row)

            domain = Domain.objects.filter(domain_name = row[0])
            if domain:
                domain = Domain.objects.get(domain_name = row[0])
                topic = Topic.objects.filter(topic_name = row[1])

                if topic:
                    topic = Topic.objects.get(topic_name = row[1])
                    
                    subtopic = Subtopic.objects.filter(subtopic_name = row[2])

                    if subtopic:
                        subtopic = Subtopic.objects.get(domain = domain, subtopic_name = row[2])
                        
                        course = Course.objects.filter(course_link = row[3])

                        if not course:

                            url_input = row[3]
                            url_opener = urlopen(Request(url_input, headers={'User-Agent': 'Mozilla'}))
                            videoInfo = bs(url_opener, features="html.parser")

                            video_title = videoInfo.title.get_text()

                            channel_title = str(videoInfo.find("link", itemprop="name"))[len('<link content="'):-len('" itemprop="name"/>')]

                            course = Course.objects.create(submitted_by = request.user, subtopic = subtopic, course_title = video_title, course_author = channel_title, course_link = row[3])


            
    return render(request, 'import_data/import_data.html')