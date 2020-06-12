from django.db import models

# Create your models here.


class Monitor(models.Model):
    url = models.URLField(max_length=200)
    frequence_in_secs = models.IntegerField()
    # result = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.url}"


class Response(models.Model):
    url_id = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    checked_ts = models.DateTimeField(auto_now_add=True)
    secs_for_first_response = models.DecimalField(
        max_digits=8, decimal_places=5)
    response_code = models.IntegerField()

    def __str__(self):
        return f"{self.url_id} | {self.checked_ts}"
