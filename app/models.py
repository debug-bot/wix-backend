from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Template(models.Model):
    """
    Model to store website templates.
    Templates provide a basic structure which users can customize.
    """
    name = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)  # This can be HTML/CSS/JS for the template
    thumbnail = models.ImageField(upload_to='templates/thumbnails/', null=True, blank=True)  # Assuming image handling is set up
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated_at']
        
        

class Website(models.Model):
    """
    Model to store user-customized websites.
    Users can choose a template and then customize it to create their website.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='websites')
    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True,null=True, blank=True)  # URL-friendly version of the name
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True, blank=True)  
    content = models.TextField(null=True, blank=True)  # This will store the user-customized HTML/CSS/JS
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated_at']

class Page(models.Model):
    """
    Model to store individual pages of a website.
    Each website can have multiple pages.
    """
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='pages')
    title = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)  # URL-friendly version of the name
    content = models.TextField(null=True, blank=True)  # HTML/CSS/JS content of the page
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_at']
