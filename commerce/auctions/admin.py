from django.contrib import admin
from .models import Category, Listing, User, Comments, Bid

admin.site.register(Category)
admin.site.register(Listing)
admin.site.register(User)
admin.site.register(Comments)
admin.site.register(Bid)

# Register your models here.
