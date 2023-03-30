from django.db import models

from django.utils.html import mark_safe
from django.core.validators import FileExtensionValidator
# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.FileField(
        upload_to='service/', validators=[FileExtensionValidator(['svg', 'jpeg', 'png', 'jpg'])])
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def img_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width ="300"/')


class Institution(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.FileField(
        upload_to='institution/', validators=[FileExtensionValidator(['svg', 'jpeg', 'png', 'jpg'])])

    def img_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/')

    def __str__(self):
        return self.title


class Officials(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    twitter_links = models.CharField(max_length=255)
    linked_links = models.CharField(max_length=255)
    social_links = models.CharField(max_length=255)
    image = models.FileField(
        upload_to='officials/', validators=[FileExtensionValidator(['svg', 'jpeg', 'png', 'jpg'])])

    def img_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Officials"


class News(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.FileField(
        upload_to='news/', validators=[FileExtensionValidator(['svg', 'jpeg', 'png', 'jpg'])])
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "News"

    def img_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/')

    def __str__(self):
        return self.title


class Achievements(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Achievements'


class Resource(models.Model):
    title = models.CharField(max_length=255, primary_key=True)
    image = models.FileField(
        upload_to="resources/", validators=[FileExtensionValidator(['svg', 'jpeg', 'png', 'jpg'])])
    # class Meta:
    #     app_label = 'service'

    def img_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/')

    def __str__(self):
        return self.title


class Article(models.Model):
    article = models.FileField()
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)


class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField()
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)


class Replay(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Jobs(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Jobs"


class Applier(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    cv = models.FileField(max_length=255, upload_to='cvs/',
                          validators=[FileExtensionValidator(['pdf'])])
    jobs = models.ManyToManyField(Jobs)


class About(models.Model):
    pass


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    suggestion = models.TextField()

    class Meta:
        verbose_name_plural = 'ContactUs'
