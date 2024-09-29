from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.createlisting, name="create"),
    path("viewcategory", views.viewcategory, name="viewcategory"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("removewatchlist/<int:id>", views.removewatchlist, name="removewatchlist"),
    path("addtowatchlist/<int:id>", views.addtowatchlist, name="addtowatchlist"),
    path("viewWatchlist", views.viewWatchlist, name="viewWatchlist"),
    path("addcomment/<int:id>", views.addcomment, name="addcomment"),
    path("newbid/<int:id>", views.newbid, name="newbid"),
    path("endauction/<int:id>", views.endauction, name="endauction"),
    path("wonauctions>", views.wonauctions, name="wonauctions")
]
