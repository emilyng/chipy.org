from django.contrib import admin

from .models import MeetingSponsor, Sponsor, SponsorGroup


class MeetingSponsorInline(admin.StackedInline):
    extra = 0
    model = MeetingSponsor


class SponsorAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "sponsor_group"]
    list_filter = ["sponsor_group"]
    search_fields = ["name", "slug", "url"]
    prepopulated_fields = {"slug": ("name",)}


class SponsorGroupAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(SponsorGroup, SponsorGroupAdmin)
