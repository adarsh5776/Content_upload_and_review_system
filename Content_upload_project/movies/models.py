from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    runtime = models.IntegerField(
        blank=True, null=True, help_text="Duration in minutes"
    )
    status = models.CharField(max_length=50, blank=True, null=True)
    vote_average = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    vote_count = models.IntegerField(blank=True, null=True)
    budget = models.BigIntegerField(blank=True, null=True)
    revenue = models.BigIntegerField(blank=True, null=True)
    original_language = models.CharField(max_length=50, blank=True, null=True)
    languages = models.TextField(
        blank=True, null=True, help_text="Comma-separated languages"
    )
    genre_id = models.IntegerField(blank=True, null=True)
    production_company_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
