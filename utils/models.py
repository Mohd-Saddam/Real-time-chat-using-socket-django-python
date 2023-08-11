from django.db import models


class TimeStampedModel(models.Model):
    """TimeStampedModel
     An abstract base class model that provides self-managed "created" and
    "modified" fields.
    """

    created_on = models.DateTimeField(auto_now_add=True, db_column="created_on")
    updated_on = models.DateTimeField(auto_now=True, db_column="updated_on")

    class Meta:
        get_latest_by = "updated_on"
        abstract = True
        default_permissions = ()
