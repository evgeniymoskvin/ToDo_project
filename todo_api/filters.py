from typing import Optional
from django.db.models.query import QuerySet
from . import serializers


def author_id_filter(queryset: QuerySet, author_id: Optional[int]):
    if author_id is not None:
        return queryset.filter(author_id=author_id)
    else:
        return queryset


def important_filter(queryset: QuerySet, important: Optional[int]):
    if important is not None:
        return queryset.filter(important=important)
    else:
        return queryset


def public_filter(queryset: QuerySet, public: Optional[int]):
    if public is not None:
        return queryset.filter(public=public)
    else:
        return queryset

