from rest_framework import serializers
from .models import Property, PropertyCategory, PropertyType, Blog, BlogSingleCreative, Contact, Subscriber, Agents, ContactAgents

class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = ['id', 'name']

class PropertyCategorySerializer(serializers.ModelSerializer):
    property_type = PropertyTypeSerializer()  # nested serializer for PropertyType
    class Meta:
        model = PropertyCategory
        fields = ['id', 'name', 'property_type']

class PropertySerializer(serializers.ModelSerializer):
    property_type = PropertyTypeSerializer()
    property_category = PropertyCategorySerializer()
    
    class Meta:
        model = Property
        fields = ['id', 'name', 'address', 'bedroom', 'bathroom', 'living_area', 'price', 'property_type', 'property_category', 'image']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['property_type'] = PropertyTypeSerializer(instance.property_type).data
        representation['property_category'] = PropertyCategorySerializer(instance.property_category).data
        return representation

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'type', 'title', 'uploaded_at', 'image']

class BlogSingleCreativeSerializer(serializers.ModelSerializer):
    blog = BlogSerializer()
    
    class Meta:
        model = BlogSingleCreative
        fields = ['id', 'blog', 'title', 'blogger_name', 'uploaded_at', 'content']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['blog'] = BlogSerializer(instance.blog).data
        return representation

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phone', 'comment']

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['id', 'email']

class AgentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agents
        fields = ['id', 'name', 'desc', 'image']

class ContactAgentsSerializer(serializers.ModelSerializer):
    agent = AgentsSerializer()
    
    class Meta:
        model = ContactAgents
        fields = ['id', 'agent', 'name', 'email', 'message', 'submitted_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['agent'] = AgentsSerializer(instance.agent).data
        return representation

    