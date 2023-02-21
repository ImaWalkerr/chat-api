from django.db import models


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True, verbose_name='Active status')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created time')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated time')
    is_deleted = models.BooleanField(default=False, verbose_name='Deleted status')

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()
