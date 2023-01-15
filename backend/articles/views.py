from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator, Page
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db.models import QuerySet
from articles.models import Article, Category, Tag
from django.shortcuts import render
from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label="Поиск статей:", widget=forms.TextInput())


def paginate(request: WSGIRequest, queryset: QuerySet, per_page: int = 5) -> Page:
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)


def index(request: WSGIRequest) -> HttpResponse:
    articles = paginate(request, Article.objects.filter(published=True))
    return render(
        request,
        "articles/index.html",
        {
            "articles": articles,
            "categories": Category.objects.all(),
            "tags": Tag.objects.all(),
            "search_form": SearchForm(),
        },
    )


def search(request: WSGIRequest) -> HttpResponse:
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"].strip().replace("  ", " ")
            articles = paginate(
                request, Article.objects.filter(published=True, title__icontains=query)
            )
            return render(
                request,
                "articles/index.html",
                {
                    "articles": articles,
                    "categories": Category.objects.all(),
                    "tags": Tag.objects.all(),
                    "search_form": form,
                },
            )
    else:
        return HttpResponseRedirect(reverse("index"))


def article(request: WSGIRequest, article_slug: str) -> HttpResponse:
    try:
        article = Article.objects.get(published=True, slug=article_slug)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")

    return render(request, "articles/article.html", {"article": article})


def category(request: WSGIRequest, category_slug: str) -> HttpResponse:
    try:
        category = Category.objects.get(slug=category_slug)
    except Category.DoesNotExist:
        raise Http404("Category does not exist")

    articles = paginate(
        request,
        Article.objects.filter(
            Q(published=True)
            & (Q(category__in=category.get_children()) | Q(category=category))
        ),
    )
    return render(
        request,
        "articles/index.html",
        {
            "articles": articles,
            "categories": Category.objects.all(),
            "tags": Tag.objects.all(),
            "search_form": SearchForm(),
        },
    )
