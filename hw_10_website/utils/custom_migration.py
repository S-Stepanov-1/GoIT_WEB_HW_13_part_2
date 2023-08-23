import os
import django

from datetime import datetime
from pymongo import MongoClient

from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_10_website.settings")
django.setup()

from quotes.models import Quote, Tag, Author  # noqa

# ----------- Connection to DB ------------
mongo_user = os.environ.get("MONGO_USER")
mongodb_pass = os.environ.get("MONGO_PASS")


client = MongoClient(f"mongodb+srv://{mongo_user}:{mongodb_pass}@stepanovdb.codnmzv.mongodb.net/")
db = client.hw09_scraping
# ------------------------------------------------


authors = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        fullname=author["fullname"],
        born_date=datetime.strptime(author["born_date"], "%B %d, %Y"),
        born_location=author["born_location"],
        description=author["description"],
        photo=author["photo_url"]
    )


quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote["tags"]:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote=quote["quote"])))

    if not exist_quote:
        author = db.authors.find_one({"_id": quote["author"]})
        author_in_sql = Author.objects.get(fullname=author["fullname"])

        q = Quote.objects.create(quote=quote["quote"], author=author_in_sql)

        for tag in tags:
            q.tags.add(tag)
