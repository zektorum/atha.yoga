from typing import Optional

from django.db.models import QuerySet, Q

from articles.app.services.types import ArticleFilterData
from articles.models import Article, Tag, Category
from core.app.repositories.base_repository import BaseRepository


class ArticleRepository(BaseRepository):
    model = Article

    def find_article_by_slug(self, article_slug: str) -> Article:
        return self.model.objects.filter(published=True, slug=article_slug).first()

    def filter_articles(
        self,
        data: Optional[ArticleFilterData] = None,
        category: Optional[Category] = None,
        tag: Optional[Tag] = None,
    ) -> QuerySet[Article]:
        filter_query = Q(published=True)
        if data:
            if query := data.get("query", None):
                filter_query &= Q(title__icontains=query)
        if category:
            filter_query &= Q(category__in=category.get_children()) | Q(
                category=category
            )

        if tag:
            return tag.articles.filter(filter_query)
        else:
            return self.model.objects.filter(filter_query)


class ArticleCategoryRepository(BaseRepository):
    model = Category

    def find_all_categories(self) -> QuerySet[Category]:
        return self.model.objects.all()

    def find_category_by_slug(self, category_slug: str) -> Category:
        return self.model.objects.filter(slug=category_slug).first()


class ArticleTagRepository(BaseRepository):
    model = Tag

    def find_all_tags(self) -> QuerySet[Tag]:
        return self.model.objects.all()

    def find_tag_by_slug(self, tag_slug: str) -> Tag:
        return self.model.objects.filter(slug=tag_slug).first()
