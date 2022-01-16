import uuid

from django.db import models
from django.core.cache import cache

# Create your models here.


class CreationModificationBase(models.Model):
    """
        Mixin for adding creation and modification datetime.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(
        auto_now_add=True, help_text="When this instance was created."
    )
    modified = models.DateTimeField(
        auto_now=True, help_text="When this instance was modified."
    )

    class Meta:
        abstract = True


class SingletonBase(models.Model):
    """
        Abstract model for creating singleton Models
        Singleton models can have at most one instance/record.
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
        self.set_cache()

    def delete(self, *args, **kwargs):
        pass

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()

        return cache.get(cls.__name__)
