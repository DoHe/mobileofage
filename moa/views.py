from django.views.generic.base import TemplateView

from .scraping.scrape import scrape_comic


class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comic = self.request.GET.get('c')
        if comic:
            image, alt, title, prev, nxt = scrape_comic(comic)
            context['url'] = comic
            context['image'] = image
            context['alt'] = alt
            context['title'] = title
            context['previous'] = '/?c=' + prev
            if nxt:
                context['next'] = '/?c=' + nxt
        return context
