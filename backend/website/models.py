from django.db import models
from bakery.models import BuildableModel


class Feature(BuildableModel):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    slug = models.SlugField(blank=True, null=True)
    picture = models.ImageField(upload_to='features')
    details = models.TextField(blank=True, null=True)

    insert_date = models.DateTimeField(auto_now_add=True)
    last_updates = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/ipasibas/{0}/'.format(self.slug)

    def _build_related(self):
        from website import views
        views.FrontPage().build_queryset()
