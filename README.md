# Django Auction Website

## Project Overview

This is a full-featured auction website built with Django, allowing users to create accounts, list items for auction, place bids, and manage their auction activities.

## Features

### User Management
- User registration and authentication
- Login and logout functionality

### Auction Functionality
- Create new auction listings
- Browse active listings
- Bid on listings
- Add/remove listings from watchlist
- View won auctions
- Comment on listings
- Category-based listing filtering

## Key Models

### Models Used
- **User**: Django's built-in user model
- **Category**: Categorize auction listings
- **Listing**: Represents individual auction items
- **Bid**: Tracks bidding information
- **Comments**: Allows users to comment on listings

## Main Views and Functionality

### Authentication
- `login_view()`: User login
- `logout_view()`: User logout
- `register()`: User registration

### Listing Management
- `index()`: Display active listings
- `viewcategory()`: Filter listings by category
- `listing()`: View individual listing details
- `createlisting()`: Create a new auction listing
- `newbid()`: Place a bid on a listing

### User Interactions
- `addtowatchlist()`: Add listing to watchlist
- `removewatchlist()`: Remove listing from watchlist
- `viewWatchlist()`: View user's watchlist
- `addcomment()`: Add comment to a listing
- `wonauctions()`: View auctions won by the user

### Auction Management
- `endauction()`: Close an active auction

## Getting Started

### Prerequisites
- Python 3.8+
- Django
- Django's authentication system

### Installation
1. Clone the repository
2. Install dependencies
   ```
   pip install django
   ```
3. Run migrations
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Create a superuser
   ```
   python manage.py createsuperuser
   ```
5. Run the development server
   ```
   python manage.py runserver
   ```

## Key Business Logic
- Bids must be higher than the current listing price
- Users can only bid on active listings
- Listings can be categorized
- Users can track their watched and won auctions

## Potential Future Improvements
- Implement more robust bid validation
- Add email notifications for auction events
- Create a more detailed user profile system
- Implement advanced search and filtering
- Add auction time limits

## Technologies Used
- Django
- Python
- HTML/CSS
- SQLite (default Django database)

## License
[Specify your license here]

## Acknowledgments
- Django Documentation
- Python Community
