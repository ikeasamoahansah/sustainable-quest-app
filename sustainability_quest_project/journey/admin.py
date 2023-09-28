from django.contrib import admin
from .models import Hero, Post

# Register your models here.
class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating')

class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'country', 'rating', 'is_completed')

admin.site.register(Hero, HeroAdmin)
admin.site.register(Post, PostAdmin)