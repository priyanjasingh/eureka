from django.db import models
from django.contrib.auth.models import User


class Contributer(models.Model):
  
    user = models.OneToOneField(User)

    # Addition info
    contact = models.CharField(max_length=12, blank=True)
    picture = models.ImageField(upload_to='profile_image', blank=True)
    specialised_subject = models.CharField(max_length=20, blank=False)
    validation_docs = models.FileField(upload_to='validation_docs',blank=False)
  
    def __unicode__(self):
        return self.user.username

class Reviewer(models.Model):
  
    user = models.OneToOneField(User)

    # Addition info
    contact = models.CharField(max_length=12, blank=True)
    picture = models.ImageField(upload_to='profile_image', blank=True)
    specialised_subject = models.CharField(max_length=20, blank=False)
    
    def __unicode__(self):
        return self.user.username



class Class(models.Model):
    """This will be class number like first, second .. eight .. tenth."""
    class_number = models.IntegerField(default=1)
    remark = models.TextField()

    def __unicode__(self):
        return u"%d" % (self.class_number)


class Subject(models.Model):
    """Subjects."""
    name = models.CharField(max_length=200, unique=False)
    topic = models.CharField(max_length=200, unique=False)
    class_number = models.ForeignKey(Class)
    pdf_doc = models.FileField(upload_to='docs_pdf', blank=True)
    video_doc = models.FileField(upload_to='docs_video', blank=True)
    animations_doc = models.FileField(upload_to='docs_animations', blank=True)
    pdf_url = models.URLField(blank=True)
    video_url = models.URLField(blank=True)
    animation_url = models.URLField(blank=True)
    uploaded_on = models.DateField(auto_now=True)
    summary = models.CharField(max_length=200, blank=False)
    contributor = models.ForeignKey(Contributer)
    download_count = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    approve = models.BooleanField(default=False)



    def __unicode__(self):
        return self.topic    


    def increment_download_count(self):
        self.download_count += 1
        self.save()

    
    def increment_rating(self):
        self.rating += 1
        self.save()

class Contact(models.Model):
    """Contact us."""
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=False)
    message = models.TextField(max_length=500)


    def __unicode__(self):
        return u"%s - %s" % (self.name, self.email)


class Faq(models.Model):
    """FAQs"""
    question = models.TextField(max_length=500)
    answer = models.TextField() #


    def __unicode__(self):
        return self.question
