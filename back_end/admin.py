from django.contrib import admin
from  . import models
# Register your models here.
from django.contrib.admin.sites import site

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ['title','image']
    list_per_page =10
    date_hierarchy = 'date'


@admin.register(models.Institution)
class InstitutionAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ['title','image']


@admin.register(models.Officials)
class OfficialsAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ['name','title']


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display=['title','image','date']
    ordering = ['date']


@admin.register(models.Achievements)
class AchievementsAdmin(admin.ModelAdmin):
    
    list_display = ['title','date']


@admin.register(models.Resource)
class ResourceAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']

    list_display = [
        'title',
        'image',
    ]
   
@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ['article','resource']

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','resource']

@admin.register(models.Replay)
class ReplayAdmin(admin.ModelAdmin):
    list_display=['name','email','comment']


@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display=['name','email','suggestion']
