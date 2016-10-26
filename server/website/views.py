from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from website.models import Project, Info, ContactInfo
from website.serializers import ProjectSerializer, InfoSerializer, ContactInfoSerializer, MiniImageSerializer
from django.views.generic import View,TemplateView
from django.http import JsonResponse, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

class ProjectList(GenericAPIView):

	def get(self, request):
		projects = Project.objects.all()
		serializer = ProjectSerializer(projects, context = {'request':request })
		return Response(serializer.data)

#class MiniImageList(GenericAPIView):
#
#	def get(self, request):
#		projects = Project.objects.all()
#		serializer = MiniImageSerializer(projects, context = {'request':request })
#		return Response(serializer.data)


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
		
