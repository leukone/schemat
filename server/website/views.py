from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from website.models import Project, Info, ContactInfo
from website.serializers import ProjectSerializer, InfoSerializer, ContactInfoSerializer, MiniImageSerializer
from django.views.generic import View,TemplateView
from django.http import JsonResponse, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

class ProjectList(APIView):

	#def get(self, request):
		queryset = Project.objects.all().select_related('gallery')
		serializer = ProjectSerializer#(projects, context = {'request':request })
		#return Response(serializer.data)
	def get(self, request):
		projects = Info.objects.all()
		serializer = ProjectSerializer(queryset, many = True, context = {'request':request })
		return Response(serializer.data)


#class MiniImageList(generics.ListAPIView):
#	serializer_class = MiniImageSerializer
#
#	def get_queryset(self):
#		project = self.kwargs['project']
#		projects = Project.objects.all()
#		serializer = MiniImageSerializer(projects, context = {'request':request })
#		return MiniImage.objects.filter(project_name = project)


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
		
