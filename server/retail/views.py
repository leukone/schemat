from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from retail.models import Project, Info, ContactInfo
from retail.serializers import ProjectSerializer, InfoSerializer, ContactInfoSerializer

#projects/
class ProjectList(APIView):

	def get(self, request):
		projects = Project.objects.all()
		serializer = ProjectSerializer(projects, many = True, context = {'request':request })
		return Response(serializer.data)

class AboutUs(APIView):

	def get(self, request):
		projects = Info.objects.all()
		serializer = InfoSerializer(projects, many = True, context = {'request':request })
		return Response(serializer.data)

class Contact(APIView):

	def get(self, request):
		projects = ContactInfo.objects.all()
		serializer = ContactInfoSerializer(projects,  many = True, context = {'request':request })
		return Response(serializer.data)
		
