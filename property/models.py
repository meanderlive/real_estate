from django.db import models
from froala_editor.fields import FroalaField

class PropertyType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Property Type"
        verbose_name_plural = "Property Types"

class PropertyCategory(models.Model):
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=False)
    
    def __str__(self):
        return f"{self.property_type.name} - {self.name}"
    
    
    class Meta:
        verbose_name = "Property Category"
        verbose_name_plural = "Property Categories"
    
class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    living_area = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True)
    property_category = models.ForeignKey(PropertyCategory, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='property_images/')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"
        
class Blog(models.Model):
    type = models.CharField(max_length=20)
    title = models.CharField(max_length=59)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/')
    
    def __str__(self):
        return self.title

class BlogSingleCreative(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    blogger_name = models.CharField(max_length=20)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    content = FroalaField()
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    comment = models.TextField()
    

    def __str__(self):
        return self.name

class Subscriber(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email
    
class Agents(models.Model):
    name = models.CharField(max_length=15)
    desc = models.CharField(max_length=25)
    image = models.ImageField(upload_to='agent_images/')

    def __str__(self):
        return self.name
    
class ContactAgents(models.Model):
    agent = models.ForeignKey(Agents, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.name} for {self.agent.name}"