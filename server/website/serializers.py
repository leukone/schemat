from rest_framework import serializers
from website.models import Project, ContactInfo, Info, MiniImage

class MiniImageSerializer(serializers.ModelSerializer):        

    image = serializers.ImageField(max_length=None, use_url=True)
    
    class Meta:
        model = MiniImage
        fields = ("number", "image")

class ProjectSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """

    projectphoto = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Project
        fields = ("ident", "title", "description", "projectphoto", "gallery")


class InfoSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """

    image = serializers.ImageField(max_length=None, use_url=True)
    
    class Meta:
        model = Info
        fields = ("ident", "title", "info", "image")

class ContactInfoSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """

    image = serializers.ImageField(max_length=None, use_url=True)
    
    class Meta:
        model = ContactInfo
        fields = ("title","contactinfo", "email", "phone", "image")

#class PhotoSerializer(serializers.ModelSerializer):
#    """ Serializer to represent the Chain model """
#    image = serializers.Field('image.url')
#    class Meta:
#        model = Photo
#        fields = ("id_", "image")
