from django.db import models

class Institucional(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    logo_one = models.ImageField(upload_to='institucional/', null=True, blank=True)
    logo_two = models.ImageField(upload_to='institucional/', null=True, blank=True)
    logo_three = models.ImageField(upload_to='institucional/', null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    zone = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    location   = models.CharField(max_length=100, null=True, blank=True)
    soft_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class PublicationType(models.TextChoices):
    documents = 'DOC', 'Documents'
    articles = 'ART', 'Articles'
    videos = 'VID', 'Videos'
    audios = 'AUD', 'Audios'
    images = 'IMG', 'Images'
    services = 'SER', 'Services'

class Publication(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=3, choices=PublicationType.choices)
    institutional= models.ForeignKey(Institucional, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, null=True, blank=True)
    cite = models.CharField(max_length=250, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(upload_to='publications/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    soft_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
class Identity(models.Model):
    mission = models.TextField()
    vision = models.TextField()
    object = models.TextField()
    institutional = models.ForeignKey(Institucional, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    soft_delete = models.BooleanField(default=False)
    
    def __str__(self):
       return (
            f"+{'-'*10}+\n"
            f"| Mission: {self.mission} |\n"
            f"+{'-'*10}+\n"
            f"| Vision: {self.vision} |\n"
            f"+{'-'*10}+\n"
            f"| Object: {self.object} |\n"
            f"+{'-'*10}+"
        )
    
class SocialNetwork(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    institutional = models.ForeignKey(Institucional, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    soft_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class History(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    institutional = models.ForeignKey(Institucional, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    soft_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Attention(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    attention_hours = models.CharField(max_length=100)
    emergency_number = models.CharField(max_length=100)
    institutional = models.ForeignKey(Institucional, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    soft_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='team/', null=True, blank=True)
    institutional = models.ForeignKey(Institucional, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    soft_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    institutional = models.ForeignKey(Institucional, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    soft_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.question

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, null=True, blank=True)
    institutional = models.ForeignKey(Institucional, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    soft_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name