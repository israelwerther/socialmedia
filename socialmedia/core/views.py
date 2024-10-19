from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
