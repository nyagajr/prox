from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    article_img = models.ImageField(upload_to='images/')
    intro = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Content(models.Model):
    heading = models.CharField(max_length=200)
    content_img = models.ImageField(upload_to='images/')
    content = models.CharField(max_length=2000)

    def __str__(self):
        return self.heading
