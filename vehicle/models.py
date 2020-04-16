from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class CarBrand(models.Model):
    code = models.CharField("Code", max_length=3)
    desc = models.CharField("Description", max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(User, verbose_name="Created By", on_delete=models.CASCADE,  blank=True, null=True, related_name="carbrand_createdby_user")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, verbose_name="Updated By", on_delete=models.SET_NULL, blank=True, null=True, related_name="carbrand_updatedby_user")
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ["code"]
        verbose_name_plural = "Car Brand"


class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, verbose_name="Car Brand", on_delete=models.CASCADE, blank=True, null=True)
    code = models.CharField("Code", max_length=6, blank=True, null=True)
    desc = models.CharField("Description", max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(User, verbose_name="Created By", on_delete=models.CASCADE,  blank=True, null=True, related_name="carmodel_createdby_user")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, verbose_name="Updated By", on_delete=models.SET_NULL, blank=True, null=True, related_name="carmodel_updatedby_user")
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ["code"]
        verbose_name_plural = "Car Model"

