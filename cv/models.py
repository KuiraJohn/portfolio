from django.db import models




class contactme(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('read', 'Read'),
        ('dismissed', 'Dismissed'),
        ('interested', 'Interested'),
    ]

    name = models.CharField(max_length=100, blank=False)
    email= models.EmailField(max_length=100)
    phone_number=models.CharField(max_length=20)
    subject= models.CharField(max_length=200)
    message= models.TextField(max_length=2000)
    status = models.CharField(choices=STATUS_CHOICES,max_length=50, default="New")
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.name}-{self.subject}"


class AboutMe(models.Model):
    title = models.CharField(max_length=255, default="About Me")
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/')  # Store images dynamically
    hire_me_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    about = models.ForeignKey(AboutMe, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.percentage}%"


class Education(models.Model):
    startDate= models.DateField()
    endDate=models.DateField()
    educationLevels= models.CharField(max_length=200)
    description=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.educationLevels

class Experience(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    position = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.position} at {self.company}"


class Service(models.Model):
    icon = models.CharField(max_length=100)  # FontAwesome class (e.g., "fa-desktop")
    title = models.CharField(max_length=200)
    description = models.TextField()
    fetured =models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
