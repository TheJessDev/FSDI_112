from django.views.generic import TemplateView


class HomePageView(TimplateView):
    template_name = "home.html"