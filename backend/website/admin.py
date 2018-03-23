from django.contrib import admin

from website import models


class FeatureAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Feature)
