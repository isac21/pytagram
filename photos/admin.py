from django.contrib import admin
from .models import Album, Photo

# Register your models here.


#class PhotoInline(admin.TabularInline):
#    model = Photo
#    extra = 3

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1

class AlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ('name', 'description')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')


admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
