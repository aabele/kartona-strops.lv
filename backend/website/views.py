"""
Website views
"""

from bakery.views import BuildableListView, BuildableDetailView, BuildableTemplateView
from website import models


class CNAMEFile(BuildableTemplateView):
    build_path = 'CNAME'
    template_name = 'website/CNAME'


class ContactPage(BuildableTemplateView):
    build_path = 'kontakti/index.html'
    template_name = 'website/contacts.html'


class FrontPage(BuildableListView):
    build_path = 'index.html'
    template_name = 'website/front.html'
    model = models.Feature


class FeatureDetailPage(BuildableDetailView):

    template_name = 'website/feature.html'
    model = models.Feature

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['other_objects'] = self.model.objects.all().exclude(pk=self.object.pk)
        return data


class NewsIndexPage(BuildableListView):
    build_path = 'jaunumi/index.html'
    template_name = 'website/news_index.html'
    model = models.Post


class NewsDetailPage(BuildableDetailView):
    template_name = 'website/news_item.html'
    model = models.Post

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['other_objects'] = self.model.objects.all().exclude(pk=self.object.pk)
        return data
