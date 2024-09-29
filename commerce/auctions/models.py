from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    categorytype = models.CharField(max_length=255)

    def __str__(self):
        return self.categorytype

class Bid(models.Model):
    bid = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="userbid")

class Listing(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=800)
    price = models.ForeignKey(Bid, on_delete=models.CASCADE, blank=True, null=True, related_name="bidamount")
    imgURL = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE, blank=True, null=True)
    active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    watchlist = models.ManyToManyField(User,blank=True, null=True, related_name="listingwatchlist")
    highestbidder = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="highestbidder")
    def __str__(self):
        return self.title

class Comments(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="usercomment")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="listingcomment")
    comment = models.CharField(max_length=180, null=True, blank=True)

    def __str__(self):
        return f"{self.owner} comment on the {self.listing}"

