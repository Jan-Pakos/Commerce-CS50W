from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, Category, Listing, Comments, Bid

from .models import User


# views.py

def index(request):
    categories = Category.objects.all()
    activeListings = Listing.objects.filter(active=True)
    return render(request, "auctions/index.html", {
        "listings": activeListings,
        "categories": categories,
    })

def viewcategory(request):
    if request.method == "POST":
        selected_category = request.POST["category"]
        category = Category.objects.get(categorytype=selected_category)
        activeListings = Listing.objects.filter(active=True, category=category)
        categories = Category.objects.all()
        return render(request, "auctions/index.html", {
            "listings": activeListings,
            "categories": categories,
        })

def listing(request, id):
    getlisting = Listing.objects.get(pk=id)
    isListinginwatchlist = request.user in getlisting.watchlist.all()
    getcomments = Comments.objects.filter(listing=getlisting)
    isbidowner = request.user.username == getlisting.owner.username
    return render(request, "auctions/listing.html", {
        "listing": getlisting,
        "islistinginwatchlist": isListinginwatchlist,
        "comments": getcomments,
        "isbidowner": isbidowner,
    })

def endauction(request, id):
    # get the objects from listing model
    getlisting = Listing.objects.get(pk=id)
    # set listing active to false
    getlisting.active = False
    # save listing objects state
    getlisting.save()
    # checking if listing is in watchlist
    isListinginwatchlist = request.user in getlisting.watchlist.all()
    getcomments = Comments.objects.filter(listing=getlisting)
    isbidowner = request.user == getlisting.owner
    return render(request, "auctions/listing.html", {
        "listing": getlisting,
        "islistinginwatchlist": isListinginwatchlist,
        "comments": getcomments,
        "isbidowner": isbidowner,
    })

def wonauctions(request):
    currentuser = request.user
    # filter for winner and inactive auction
    wonlistings = Listing.objects.filter(active=False, highestbidder=currentuser)
    return render(request, "auctions/wonauctions.html", {
        "listings": wonlistings,
    })

    

def viewWatchlist(request):
    categories = Category.objects.all()
    currentuser = request.user
    getlistings = currentuser.listingwatchlist.all()
    return render(request, "auctions/watchlist.html", {
        "listings": getlistings,
    })

def addcomment(request, id):
    currentuser = request.user
    getlisting = Listing.objects.get(pk=id)
    message = request.POST["addcomment"]

    addcomment = Comments(
        owner=currentuser,
        listing=getlisting,
        comment=message,
    )

    addcomment.save()
    return HttpResponseRedirect(reverse("listing", args=(id, )))

def removewatchlist(request, id):
    getlisting = Listing.objects.get(pk=id)
    currentuser = request.user
    getlisting.watchlist.remove(currentuser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))

def addtowatchlist(request, id):
    getlisting = Listing.objects.get(pk=id)
    currentuser = request.user
    getlisting.watchlist.add(currentuser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))

def createlisting(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "auctions/create.html", {
            "categories": categories,
        })
    else:
        # get data from form
        title = request.POST["title"]
        description = request.POST["description"]
        imgURL = request.POST["imgURL"]
        price = request.POST["price"]
        category = request.POST["category"]

        currentUser = request.user

        categoryInfo = Category.objects.get(categorytype=category)
        # create new bid object
        bid = Bid(bid=float(price), owner=currentUser)
        bid.save()

        newListing = Listing(
            owner=currentUser,
            title=title,
            description=description,
            price=bid,
            category=categoryInfo,
        )
        newListing.save()
        return HttpResponseRedirect(reverse(index))

def newbid(request, id):
    newbid = request.POST["newbid"]
    getlisting = Listing.objects.get(pk=id)
    if float(newbid) > getlisting.price.bid:
        updatebid = Bid(owner=request.user, bid=float(newbid), highestbidder=request.user)
        updatebid.save()
        getlisting.price = updatebid
        getlisting.save()
        return render(request, "auctions/listing.html", {
            "listing": getlisting,
            "message": "Your bid was successful.",
            "update": True
        })
    else:
        return render(request, "auctions/listing.html", {
            "listing": getlisting,
            "message": "Your bid must be above the current bid.",
            "update": False
        })
    
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
