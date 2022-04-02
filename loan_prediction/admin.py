from django.contrib import admin

from .models import PipelineInput


class AwardAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'name_slug': ('name',)}


for model, model_admin in zip(
    [PipelineInput],
    [AwardAdmin]
):
    admin.site.register(model, model_admin)
