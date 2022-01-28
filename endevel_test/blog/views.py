from django.views.generic import ListView
import urllib.parse
from django.urls import reverse
from blog.models import Article, Tag


class ArticleListView(ListView):
    model = Article
    template_name = "index.html"
    paginate_by = 5

    def _get_tag_from_request(self):
        return self.request.GET.get("tag", None)

    @staticmethod
    def _generate_prev_next_page(query):
        return reverse("articles") + "?" + urllib.parse.urlencode(query)

    def get_queryset(self):
        tag = self._get_tag_from_request()
        if tag:
            return Article.objects.filter(tags__name=tag)

        return Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        query = {}
        tag = self._get_tag_from_request()
        context = super().get_context_data()
        page_obj = context.get("page_obj", None)

        if tag:
            query["tag"] = tag

        if page_obj and page_obj.has_previous():
            query["page"] = page_obj.previous_page_number()
            context["prev_page_url"] = self._generate_prev_next_page(query)
        if page_obj and page_obj.has_next():
            query["page"] = page_obj.next_page_number()
            context["next_page_url"] = self._generate_prev_next_page(query)

        context["tags"] = Tag.objects.all()

        return context
