from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from website.models import Project, Info, ContactInfo
from website.serializers import ProjectSerializer, InfoSerializer, ContactInfoSerializer
from django.views.generic import View,TemplateView
from django.http import JsonResponse, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

class ProjectList(APIView):

	def get(self, request):
		projects = Project.objects.all()
		serializer = ProjectSerializer(projects, context = {'request':request })
		return Response(serializer.data)

	def post(self, request):
        serializer = ProjectSerializer(data = request.data)
        print(request.data)

        if serializer.is_valid():
            serializer.save(user = request.user)
            print(serializer.validated_data)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

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
		
