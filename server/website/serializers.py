from rest_framework import serializers
from website.models import Project, ContactInfo, Info, MiniImage

class MiniImageSerializer(serializers.ModelSerializer):        

    image = serializers.ImageField(max_length=None, use_url=True)
    
    class Meta:
        model = MiniImage
        fields = ("number", "image")


class ProjectSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """

    image = serializers.ImageField(max_length=None, use_url=True)
    gallery = serializers.serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='project-detail'
    )
    
    class Meta:
        model = Project
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
