from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)

class Project(models.Model):
    """ High-level retail chain model"""
    ident = models.IntegerField(default=1)
    title = models.CharField(max_length=200, default='PROJECT TITLE')
    desc = models.CharField(max_length=1000)
    #image = models.CharField(max_length=100, default='PROJECT TITLE')
    image = models.ImageField(upload_to='images/', default='/home/ola/Documents/schemat/drf_copy/drf_sample/client/static/app/images/2_mini.jpg')

    def __str__(self):
        return str(self.title)

class MiniImage(models.Model):
    identification = models.CharField(max_length=100, default=1)
    photo = models.ImageField(upload_to='images/', default='/home/ola/Documents/schemat/drf_copy/drf_sample/client/static/app/images/2_mini.jpg')
    project = models.ForeignKey(Project, related_name='gallery')

    def __str__(self):
        return str(self.identification)


class Info(models.Model):
    """ High-level retail chain model"""
    ident = models.IntegerField(default=1)
    title = models.CharField(max_length=200, default='About us 1')
    info = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/', default='/home/ola/Documents/schemat/drf_copy/drf_sample/client/static/app/images/2_mini.jpg')

    def __str__(self):
        return str(self.title)

class ContactInfo(models.Model):
    """ High-level retail chain model"""
    title = models.CharField(max_length=200, default='Contact info')
    contactinfo = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', default='/home/ola/Documents/schemat/drf_copy/drf_sample/client/static/app/images/2_mini.jpg')

    def __str__(self):
        return str(self.title)

    def clean(self):
        validate_only_one_instance(self)


# class Picture(models.Model):
#   """ Location employee model.  Foreign key to Store."""
#    project = models.ForeignKey(Project, related_name='photos')
#    id_ = models.IntegerField(default=1)
#    image = models.ImageField(upload_to='blah', default='/home/ola/Documents/schemat/drf_copy/drf_sample/client/static/app/images/2_mini.jpg')
 