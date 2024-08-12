from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, BlogSingleCreative, Property, Contact, Subscriber, Agents, ContactAgents
from django.http import HttpResponse
from .forms import ContactAgentForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    properties = Property.objects.all()
    context = {
        'properties': properties
    }
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")

def agents(request):
    agents = Agents.objects.all()
    context = {
        'agents':agents
    }
    return render(request, "agents.html",context)

def agent_details(request, agent_id):
    agent = get_object_or_404(Agents, id=agent_id)
    context = {
        'agent': agent
    }
    return render(request, "agent-details.html", context)

def blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, "blog.html", context)

def blog_detail(request, blog_id):
    # This view might be used for another type of blog detail if needed
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog-detail.html', {'blog': blog})

def blog_single_creative(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog_creative = get_object_or_404(BlogSingleCreative, blog=blog)
    return render(request, "blog-single-creative.html", {'blog_creative': blog_creative})


def contact(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            comment = request.POST.get('comment')
            
            Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                comment=comment
            )
            success_message = "Your message has been sent successfully!"
            return render(request, 'contact.html', {'success_message': success_message})
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}", status=500)
    
    return render(request, 'contact.html')

def subscriber(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        Subscriber.objects.create(email=email)
        return render(request, 'home.html')
    return render(request, 'home.html')

def rent_properties_detail(request, property_id):
    property = Property.objects.get(id=property_id)
    return render(request, "properties-detail.html",{'property':property})

def sell_properties(request):
    properties = Property.objects.all()
    context = {
        'properties': properties
    }
    return render(request, "sell-properties.html", context)

def sell_properties_detail(request, property_id):
    property = Property.objects.get(id=property_id)
    return render(request, "sell-properties-details.html",{'property':property})

def rent_properties(request):
    properties = Property.objects.all()
    context = {
        'properties': properties
    }
    return render(request, "rent-properties.html", context)


def contactdetails(request, agent_id):
    agent = get_object_or_404(Agents, id=agent_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save the contact information
        contact = ContactAgents(agent=agent, name=name, email=email, message=message)
        contact.save()
        
        # Add a success message
        messages.success(request, 'Your message has been sent successfully!')
        
        # Redirect to the agent details page
        return redirect('agent_details', agent_id=agent.id)

    context = {
        'agent': agent,
    }
    return render(request, "agent-details.html", context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        email = request.POST.get('username')
        print('form',email)
        if form.is_valid():
            user = form.get_user()
            print('user',user)
            auth_login(request, user)
            return redirect('home')  # Adjust this as needed
        else:
            # Pass the form with errors back to the template
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()  # Initialize the form for GET requests
    
    return render(request, 'signup.html', {'form': form})

def user_logout(request):
    logout(request)  # This logs out the user
    return redirect('login')  #