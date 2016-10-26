from rest_framework import serializers
from website.models import Project, ContactInfo, Info, MiniImage


class MiniImageSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = MiniImage
        depth = 1
        fields = ("photo")

class ProjectSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """
    
    image = serializers.ImageField(max_length=None, use_url=True)
    gallery = MiniImageSerializer(many = True, required = False)

    class Meta:
        model = Project
        depth = 1
        fields = ("ident", "title", "desc", "image", "gallery")

    

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
