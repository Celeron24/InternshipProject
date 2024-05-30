from datetime import date
from dateutil import parser as date_parser
from .forms import RSSFeedSearchForm, ArchiveNewsSearchForm
from .models import NewsArticle
from django.core.files.base import ContentFile
from django.utils.dateparse import parse_date
import requests
from django.shortcuts import render
import feedparser
from django.utils.text import slugify


def archive(request):
    form = ArchiveNewsSearchForm(request.POST or None)
    archived_news = None
    news = NewsArticle.objects.all()
    if request.method == 'POST':
        form = ArchiveNewsSearchForm(request.POST)
        if form.is_valid():
            filter_archive_date = form.cleaned_data['filter_archive_date']
            # Ensure filter_archive_date is a date object
            if isinstance(filter_archive_date, date):
                archived_news = NewsArticle.objects.filter(published_date=filter_archive_date)
    return render(request, 'newshub/archived_news.html', {'form': form, 'archived_news': archived_news, 'news': news})


def parse_date(date_str):
    try:
        parsed_date = date_parser.parse(date_str)
        return parsed_date.date()
    except ValueError:
        return None


def extract_image_url(entry):
    # Check if 'summary' field exists and extract image URL from it
    if 'summary' in entry:
        summary = entry['summary']
        # Extracting image URL from the summary
        start_index = summary.find('<img src="') + len('<img src="')
        end_index = summary.find('"', start_index)
        image_url = summary[start_index:end_index]
        return image_url
    return None


def search_feed(feed, query, start_date, end_date):
    results = []
    for entry in feed.entries:
        published_date = parse_date(entry.published)
        if published_date and start_date <= published_date <= end_date:
            if query.lower() in entry.title.lower() or (entry.summary and query.lower() in entry.summary.lower()):
                # Extract image URL
                image_url = extract_image_url(entry)
                entry['image_url'] = image_url  # Add image URL to the entry dictionary
                results.append(entry)
    return results


def rss_feed_search(request):
    form = RSSFeedSearchForm(request.POST or None)
    search_results = []

    if request.method == 'POST' and form.is_valid():
        query = form.cleaned_data['query']
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']

        search_results = NewsArticle.objects.filter(
           title__icontains=query,
           published_date__range=[start_date, end_date]
        )

    context = {
        'form': form,
        'search_results': search_results,
    }
    return render(request, 'newshub/search.html', context)


def save_image_from_url(url, title):
    response = requests.get(url)
    if response.status_code == 200:
        return ContentFile(response.content, name=f"{slugify(title)}.jpg")
    return None


def fetch_rss_entries(rss_urls):
    entries = []
    for rss_url in rss_urls:
        feed = feedparser.parse(rss_url)
        for entry in feed.entries:
            title = entry.get('title')
            link = entry.get('link')
            summary = entry.get('summary')
            image_url = None
            if 'media_thumbnail' in entry and entry['media_thumbnail']:
                thumbnail_url = entry['media_thumbnail'][0]['url']
                image_url = thumbnail_url.replace('/standard/240/', '/standard/1024/')
            entries.append({
                'title': title,
                'link': link,
                'summary': summary,
                'image_url': image_url
            })
    return entries


def index(request):
    form = RSSFeedSearchForm(request.POST or None)
    first_article = NewsArticle.objects.last()
    rss_urls = [
        "https://feeds.bbci.co.uk/news/rss.xml",
        "https://feeds.bbci.co.uk/news/world/rss.xml",
        "https://feeds.bbci.co.uk/news/business/rss.xml",
        "https://feeds.bbci.co.uk/news/health/rss.xml",
    ]
    entries = fetch_rss_entries(rss_urls)
    return render(request, 'newshub/index.html', {'entries': entries, 'form': form, 'first_article': first_article})


def health(request):
    form = RSSFeedSearchForm(request.POST or None)
    rss_urls = ["https://feeds.bbci.co.uk/news/health/rss.xml"]
    entries = fetch_rss_entries(rss_urls)
    return render(request, 'newshub/health.html', {'entries': entries, 'form': form})


def entertainment_and_arts(request):
    form = RSSFeedSearchForm(request.POST or None)
    rss_urls = ["https://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml"]
    entries = fetch_rss_entries(rss_urls)
    return render(request, 'newshub/entertainment_arts.html', {'entries': entries, 'form': form})


def business(request):
    form = RSSFeedSearchForm(request.POST or None)
    rss_urls = ["https://feeds.bbci.co.uk/news/business/rss.xml"]
    entries = fetch_rss_entries(rss_urls)
    return render(request, 'newshub/business.html', {'entries': entries, 'form': form})


def asia(request):
    form = RSSFeedSearchForm(request.POST or None)
    rss_urls = ["https://feeds.bbci.co.uk/news/world/asia/rss.xml"]
    entries = fetch_rss_entries(rss_urls)
    return render(request, 'newshub/asia.html', {'entries': entries, 'form': form})


def africa(request):
    form = RSSFeedSearchForm(request.POST or None)
    rss_urls = ["https://feeds.bbci.co.uk/news/world/africa/rss.xml"]
    entries = fetch_rss_entries(rss_urls)
    return render(request, 'newshub/africa.html', {'entries': entries, 'form': form})


def technology(request):
    form = RSSFeedSearchForm(request.POST or None)
    rss_urls = ["https://feeds.bbci.co.uk/news/technology/rss.xml"]
    entries = fetch_rss_entries(rss_urls)
    return render(request, 'newshub/technology.html', {'entries': entries, 'form': form})


def europe(request):
    form = RSSFeedSearchForm(request.POST or None)
    rss_urls = ["https://feeds.bbci.co.uk/news/world/europe/rss.xml"]
    entries = fetch_rss_entries(rss_urls)
    return render(request, 'newshub/europe.html', {'entries': entries, 'form': form})


def sports(request):
    form = RSSFeedSearchForm(request.POST or None)
    rss_urls = ["http://newsrss.bbc.co.uk/rss/sportonline_uk_edition/cricket/rss.xml"]
    entries = fetch_rss_entries(rss_urls)
    return render(request, 'newshub/sports.html', {'entries': entries, 'form': form})


def politics(request):
    form = RSSFeedSearchForm(request.POST or None)
    rss_urls = ["https://feeds.bbci.co.uk/news/politics/rss.xml"]
    entries = fetch_rss_entries(rss_urls)
    return render(request, 'newshub/politics.html', {'entries': entries, 'form': form})


def wales(request):
    form = RSSFeedSearchForm(request.POST or None)
    rss_urls = ["https://feeds.bbci.co.uk/news/wales/rss.xml"]
    entries = fetch_rss_entries(rss_urls)
    return render(request, 'newshub/wales.html', {'entries': entries, 'form': form})


def scotland(request):
    form = RSSFeedSearchForm(request.POST or None)
    rss_urls = ["https://feeds.bbci.co.uk/news/scotland/rss.xml"]
    entries = fetch_rss_entries(rss_urls)
    return render(request, 'newshub/scotland.html', {'entries': entries, 'form': form})


def northern_ireland(request):
    form = RSSFeedSearchForm(request.POST or None)
    rss_urls = ["https://feeds.bbci.co.uk/news/northern_ireland/rss.xml"]
    entries = fetch_rss_entries(rss_urls)
    return render(request, 'newshub/northernireland.html', {'entries': entries, 'form': form})


def england(request):
    form = RSSFeedSearchForm(request.POST or None)
    rss_urls = ["https://feeds.bbci.co.uk/news/england/rss.xml"]
    entries = fetch_rss_entries(rss_urls)
    return render(request, 'newshub/england.html', {'entries': entries, 'form': form})


def us_canada(request):
    form = RSSFeedSearchForm(request.POST or None)
    rss_urls = ["https://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml"]
    entries = fetch_rss_entries(rss_urls)
    return render(request, 'newshub/uscanada.html', {'entries': entries, 'form': form})


def middle_east(request):
    form = RSSFeedSearchForm(request.POST or None)
    rss_urls = ["https://feeds.bbci.co.uk/news/world/middle_east/rss.xml"]
    entries = fetch_rss_entries(rss_urls)
    return render(request, 'newshub/middleeast.html', {'entries': entries, 'form': form})


def latin_america(request):
    form = RSSFeedSearchForm(request.POST or None)
    rss_urls = ["https://feeds.bbci.co.uk/news/world/latin_america/rss.xml"]
    entries = fetch_rss_entries(rss_urls)
    return render(request, 'newshub/LatinAmerica.html', {'entries': entries, 'form': form})
