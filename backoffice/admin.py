from django.contrib import admin

class ModelAdmin(admin.ModelAdmin):
    pass


class BackofficeAdminSite(admin.AdminSite):
    """
    Backoffice AdminSite
    """
    site_header = "Backoffice AdminSite"
    site_title = "Backoffice AdminSite"
    index_title = "Backoffice AdminSite"
    site_url = None

site = BackofficeAdminSite(name='backoffice-admin')
