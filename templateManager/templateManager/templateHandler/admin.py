from django.contrib import admin
from .models import NavbarOption, Post, Image, About, HomeDesign



class ImageAdmin(admin.StackedInline):
    model = Image



class NavbarOptionAdmin(admin.ModelAdmin):
    list_display = ('name' , 'created' , 'updated')

class PostAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]
    list_display = ('title', 'menu' , 'created' , 'updated')


admin.site.register(Post, PostAdmin)
admin.site.register(NavbarOption, NavbarOptionAdmin)
admin.site.register(About)
admin.site.register(HomeDesign)