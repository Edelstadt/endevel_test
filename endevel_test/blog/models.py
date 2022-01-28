from django.db import models
from ckeditor.fields import RichTextField


class Tag(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=50,
        unique=True,
        blank=False,
        db_index=True,
    )

    def __str__(self) -> str:
        return self.name


class Article(models.Model):
    title_cs = models.CharField(
        verbose_name="Titulek",
        max_length=100,
        unique=True,
        blank=False,
    )
    title_eng = models.CharField(
        verbose_name="Title",
        max_length=100,
        unique=True,
        blank=False,
    )
    content_cs = RichTextField()
    content_eng = RichTextField()
    tags = models.ManyToManyField(
        Tag,
        verbose_name="Tags",
    )
    header_image = models.ImageField(
        upload_to="media/images/header_image",
    )
    thumb_image = models.ImageField(
        upload_to="media/images/thumb_image",
    )

    def __str__(self) -> str:
        return self.title_eng
