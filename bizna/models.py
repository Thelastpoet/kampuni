from django.db import models
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from .utils import unique_slugify

class Company(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    category = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="images/")
    country = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city =  models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    description = models.TextField()
    date_established = models.DateTimeField()
    created_by = models.ForeignKey(User)
    official_website = models.URLField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ['name',]
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('index', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug_str = '%s' % self.name
            unique_slugify(self, slug_str)
        super(Company, self).save(*args, **kwargs)
        
        
class Events(models.Model):
    name = models.CharField(max_length=255)
    company = models.OneToOneField(Company)
    pub_date = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField()
    event_logo = models.ImageField(upload_to="images")
    venue = models.CharField(max_length=255)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name
    