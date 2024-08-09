from django.shortcuts import render
from rest_framework import generics
from .models import Property, PropertyCategory, PropertyType, Blog, BlogSingleCreative, Contact, Subscriber, Agents, ContactAgents
from .serializers import PropertySerializer, PropertyCategorySerializer, PropertyTypeSerializer, BlogSerializer, BlogSingleCreativeSerializer, ContactSerializer, SubscriberSerializer, AgentsSerializer, ContactAgentsSerializer
from django.http import JsonResponse
import requests

class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyTypeListCreateView(generics.ListCreateAPIView):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer

class PropertyTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer

class PropertyCategoryListCreateView(generics.ListCreateAPIView):
    queryset = PropertyCategory.objects.all()
    serializer_class = PropertyCategorySerializer
    
class PropertyCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyCategory.objects.all()
    serializer_class = PropertyCategorySerializer

def property_list_view(request):
    properties = Property.objects.all()
    serializer = PropertySerializer(properties, many=True)
    return JsonResponse(serializer.data, safe=False)
    
class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogSingleCreativeListCreateView(generics.ListCreateAPIView):
    queryset = BlogSingleCreative.objects.all()
    serializer_class = BlogSingleCreativeSerializer

class BlogSingleCreativeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogSingleCreative.objects.all()
    serializer_class = BlogSingleCreativeSerializer

class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class SubscriberListCreateView(generics.ListCreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

class SubscriberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

class AgentsListCreateView(generics.ListCreateAPIView):
    queryset = Agents.objects.all()
    serializer_class = AgentsSerializer

class AgentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agents.objects.all()
    serializer_class = AgentsSerializer

class ContactAgentsListCreateView(generics.ListCreateAPIView):
    queryset = ContactAgents.objects.all()
    serializer_class = ContactAgentsSerializer

class ContactAgentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactAgents.objects.all()
    serializer_class = ContactAgentsSerializer