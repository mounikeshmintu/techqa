from django.db import models

# from django_extensions.db.models import (
#     TitleSlugDescriptionModel, TimeStampedModel)


class Task():
    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def __unicode(self):
        return self.title

# Create your models here.
class CatManager(models.Manager):
    def category_filter(self,*args,**kwargs):
        return super(CatManager,self).filter(category='python')
class Category(models.Model):
    title=models.CharField(max_length=50)
    def __str__(self):
        return self.title
class Question(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    category=models.ForeignKey(Category)
    objects=CatManager()
    def __str__(self):
        return self.name
