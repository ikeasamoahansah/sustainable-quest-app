from django.contrib import admin
from .models import Goal

# Register your models here.
class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'image1', 'image2', 'image3', 'content1','content2')

admin.site.register(Goal, GoalAdmin)