from django.contrib import admin
from .models import contactme  # Import your model
from django.contrib import admin
from .models import AboutMe, Skill, Education, Experience, Service, ContactInfo

#@admin.register(contactme)
class ContactMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'subject', 'created_at', 'status')  # Fields to display in the list view
    search_fields = ('name', 'email', 'subject')  # Enable search functionality
    list_filter = ('created_at',)  # Add a filter by date
    list_editable= ('status',)

# Alternatively, you can use:
admin.site.register(contactme, ContactMeAdmin)

# Inline model for Skills (since it's related to AboutMe)
class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1  # Number of empty forms to show

# Register AboutMe with inline Skills
@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    inlines = [SkillInline]

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('educationLevels', 'startDate', 'endDate', 'created_at', 'updated_at')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'location', 'start_date', 'end_date', 'created_at', 'updated_at')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'fetured', 'created_at', 'updated_at')
    list_filter = ('fetured',)

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'email', 'phone', 'created_at', 'updated_at')

