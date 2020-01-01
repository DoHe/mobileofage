from django.core.management.base import BaseCommand

from moa.constants import COMIC_URL
from moa.models import Comic
from moa.scraping.scrape import scrape_comic


class Command(BaseCommand):
    help = 'Updates recent comics'

    def handle(self, *args, **options):
        comic_id = ''
        for i in range(5):
            image, alt, title, date, comic_id, prev, nxt = scrape_comic(
                COMIC_URL + comic_id
            )
            db_comic = Comic(
                id=comic_id,
                image=image,
                alt=alt,
                date=date,
                title=title,
                previous=prev,
                next=nxt,
            )
            db_comic.save()
            comic_id = prev
            print(f"Updated data for comic number {i+1} ({title})")
