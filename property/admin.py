from django.contrib import admin
from .models import PropertyType, PropertyCategory, Property, Blog, BlogSingleCreative, Contact, Subscriber, Agents, ContactAgents

@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(PropertyCategory)
class PropertyCategoryAdmin(admin.ModelAdmin):
    list_display = ('property_type', 'name')
    

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'address', 'bedroom', 'bathroom', 'living_area', 'property_type', 'property_category')
    list_filter = ('property_type', 'property_category', 'address')
    search_fields = ('name', 'address', 'price')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('type', 'title')

@admin.register(BlogSingleCreative)
class BlogSingleCreativeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'comment')

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email',)
    
@admin.register(Agents)
class AgentsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(ContactAgents)
class ContactAgents(admin.ModelAdmin):
    list_display = ('name', 'agent')