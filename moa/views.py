from django.contrib.syndication.views import Feed
from django.views.generic.base import TemplateView

from .constants import COMIC_URL
from .models import Comic
from .scraping.scrape import scrape_comic


class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comic_id = self.request.GET.get('c', '')
        from_db = False
        if comic_id:
            try:
                db_comic = Comic.objects.get(id=comic_id)
                from_db = True
            except Comic.DoesNotExist:
                pass
        else:
            db_comic = Comic.objects.order_by('-date')[0]
            from_db = True

        if from_db:
            image = db_comic.image
            alt = db_comic.alt
            title = db_comic.title
            alt = db_comic.alt
            prev = db_comic.previous
            nxt = db_comic.next
        else:
            image, alt, title, date, comic_id, prev, nxt = scrape_comic(
                COMIC_URL + comic_id
            )
            db_comic = Comic(
                id=comic_id,
                image=image,
                alt=alt,
                title=title,
                date=date,
                previous=prev,
                next=nxt,
            )
            db_comic.save()

        context['url'] = COMIC_URL + comic_id
        context['image'] = image
        context['alt'] = alt
        context['title'] = title
        context['previous'] = '/?c=' + prev
        if nxt:
            context['next'] = '/?c=' + nxt
        return context


class ComicFeed(Feed):
    title = "Mobile of Age"
    link = "/"
    description = "All the newest Dumbing of Age comics in a mobile friendly way"
    description_template = "feed.html"

    def items(self):
        return Comic.objects.order_by('-date')[:30]

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return f"/?c={item.id}"
