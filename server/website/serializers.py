from rest_framework import serializers
from website.models import Project, ContactInfo, Info

"""class MiniImageSerializer(serializers.ModelSerializer):        

    image = serializers.ImageField(max_length=None, use_url=True)
    
    class Meta:
        model = MiniImage
        fields = ("number", "image")"""

class ProjectSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """

    image = serializers.ImageField(max_length=None, use_url=True)
    gallery1 = serializers.ImageField(max_length=None, use_url=True)
    gallery2 = serializers.ImageField(max_length=None, use_url=True)
    gallery3 = serializers.ImageField(max_length=None, use_url=True)
    gallery4 = serializers.ImageField(max_length=None, use_url=True)
    gallery5 = serializers.ImageField(max_length=None, use_url=True)
    gallery6 = serializers.ImageField(max_length=None, use_url=True)
    gallery = [gallery1, gallery2, gallery3, gallery4, gallery5, gallery6]
    class Meta:
        model = Project
        fields = ("ident", "title", "description", "image", "gallery1", "gallery2", "gallery3", "gallery4", "gallery5", "gallery6")


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
