from django.views.generic import ListView, DetailView

from website import models


class FrontPage(ListView):
    model = models.Feature
    template_name = 'website/front.html'


class FeatureDetailView(DetailView):

    model = models.Feature
    template_name = 'website/feature.html'

    def get_object(self, queryset=None):
        return self.model.objects.get(slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['other_objects'] = self.model.objects.all().exclude(pk=self.object.pk)
        return data


class NewsListView(ListView):
    model = models.Post
    template_name = 'website/news_index.html'


class NewsDetailView(DetailView):
    model = models.Post
    template_name = 'website/news_item.html'

    def get_object(self, queryset=None):
        return self.model.objects.get(slug=self.kwargs.get('slug'))
