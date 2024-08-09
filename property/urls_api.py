from django.urls import path
from .views_api import (
    PropertyListCreateView,
    PropertyDetailView,
    PropertyTypeListCreateView,
    PropertyTypeDetailView,
    PropertyCategoryListCreateView,
    PropertyCategoryDetailView,
    BlogListCreateView,
    BlogDetailView,
    BlogSingleCreativeListCreateView,
    BlogSingleCreativeDetailView,
    ContactListCreateView,
    ContactDetailView,
    SubscriberListCreateView,
    SubscriberDetailView,
    AgentsListCreateView,
    AgentsDetailView,
    ContactAgentsListCreateView,
    ContactAgentsDetailView,
    property_list_view,
)

urlpatterns = [
    path('properties/', PropertyListCreateView.as_view(), name='property-list-create'),
    path('properties/<int:pk>/', PropertyDetailView.as_view(), name='property-detail'),

    path('property-types/', PropertyTypeListCreateView.as_view(), name='property-type-list-create'),
    path('property-types/<int:pk>/', PropertyTypeDetailView.as_view(), name='property-type-detail'),

    path('property-categories/', PropertyCategoryListCreateView.as_view(), name='property-category-list-create'),
    path('property-categories/<int:pk>/', PropertyCategoryDetailView.as_view(), name='property-category-detail'),

    path('blogs/', BlogListCreateView.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),

    path('blog-single-creatives/', BlogSingleCreativeListCreateView.as_view(), name='blog-single-creative-list-create'),
    path('blog-single-creatives/<int:pk>/', BlogSingleCreativeDetailView.as_view(), name='blog-single-creative-detail'),

    path('contacts/', ContactListCreateView.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),

    path('subscribers/', SubscriberListCreateView.as_view(), name='subscriber-list-create'),
    path('subscribers/<int:pk>/', SubscriberDetailView.as_view(), name='subscriber-detail'),

    path('agents/', AgentsListCreateView.as_view(), name='agents-list-create'),
    path('agents/<int:pk>/', AgentsDetailView.as_view(), name='agents-detail'),

    path('contact-agents/', ContactAgentsListCreateView.as_view(), name='contact-agents-list-create'),
    path('contact-agents/<int:pk>/', ContactAgentsDetailView.as_view(), name='contact-agents-detail'),

    path('api/properties/', property_list_view, name='property-list-json'),
]
