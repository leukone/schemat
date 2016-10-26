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

class ProjectList(generics.ListCreateAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer
    def post(self, request, format=None):
    	serializer = ProjectSerializer(data=request.DATA, files=request.FILES)
		if serializer.is_valid():
        	serializer.save()
        	return Response(serializer.data, status=status.HTTP_201_CREATED)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request):
		serializer = ProjectSerializer(projects, context = {'request':request })
		return Response(serializer.data)

"""class MiniImageList(APIView):

	def get(self, request):
		projects = Project.objects.all()
		serializer = MiniImageSerializer(projects, context = {'request':request })
		return Response(serializer.data)"""


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
		
