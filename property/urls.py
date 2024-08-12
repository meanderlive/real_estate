from django.urls import path
from .views import (
    home,
    about,
    agent_details,
    agents,
    blog,
    blog_detail,
    blog_single_creative,
    contact,
    rent_properties_detail,
    sell_properties,
    sell_properties_detail,
    rent_properties,
    subscriber,
    contactdetails,
    login,
    signup,
    user_logout,
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('agent-details/', agent_details, name='agent-details'),
    path('agents/', agents, name='agents'),
     path('agents/<int:agent_id>/', agent_details, name='agent_details'),
    path('blog/', blog, name='blog'),
    path('blog/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('blog/creative/<int:blog_id>/', blog_single_creative, name='blog_single_creative'),
    path('contact/', contact, name='contact'),
    # path('properties-detail/', properties_detail, name='properties-detail'),
    path('sell-properties/', sell_properties, name='sell-properties'),
    path('rent-properties/', rent_properties, name='rent-properties'),
    path('subscriber/', subscriber, name='subscriber'),
    # path('agents/', agents, name='agents_list'),
    path('agents/<int:agent_id>/', contactdetails, name='contact_details'),
    path('agents/<int:agent_id>/contact/', contactdetails, name='contact_details'),
    
    path('rent-properties-detail/<int:property_id>/', rent_properties_detail, name='rent-properties-detail'),
    path('sell-properties-details/<int:property_id>/', sell_properties_detail, name='sell-properties-details'),

    path('login/', login, name="login"),
    path('signup/', signup, name='signup'),
    path('logout/', user_logout, name='user_logout'),
]



