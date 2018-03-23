"""
Website views
"""

from bakery.views import BuildableListView, BuildableDetailView
from website import models


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