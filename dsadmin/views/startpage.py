from django.views.generic import TemplateView

from dsadmin.views.basepage import BaseAdminView

class MainView(BaseAdminView, TemplateView):
    template_name = 'index.html'
