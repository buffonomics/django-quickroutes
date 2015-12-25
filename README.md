# django-quickroutes
Make routes very Quickly while developing with Django as you would in Flask.

## Why
I'm a believer in convention-over-configuration. I know, I probably shouldn't be interested in Django then because of this as that's just not the Django way.
But I think Django has come far enough as a framework and as a community in this century that some of this rigidness should now give way for faster ways of doing things and moving quickly with app development.

One of the frustrating bits of working with Django was me having to always tweak the urls.py file as I worked. 
I wanted all the time-saving, monolithic goodness (IMO) of Django, with the dev-agility (I should trademark that word) of Flask.

django-quickroutes is the beginning of my efforts to impose some tolerance into Django's unneccesarily rigid practices.


## How to use
Add the q.route decorator on top of your view functions and be sure your views are being imported into your urls.py.
Then call q.initQuickRoutes(urlPatterns) in your urls.py file to register the quick routes. 

So in demo-speak....

### In your views
```from django_quickroutes import q

@q.route("/foo/bar")
function view1(request):
...

@q.route("/foo/bar/:id")
function view2(request, id):
...
```

django-quickroutes doesn't care about the forward slash. 
This is the same as saying "/restaurants/:type/:city".:

```@q.route("restaurants/:type/:city")
function listRestaurants(request, type, city):
...
```

If, for some reason, you prefer django's idea of what a route descriptor should look like (i.e. raw regex),
You can still save time by doing this:
```
@q.route("^foo/bar/(?P<id>\d+)/$")
function view4(request, id):
...
```
Just be sure you begin the route by the character '^' (aka regex's beginning-of-string char) to let DJ-QR know you're going old-school on this q.route.


## In urls.py of your app
`
import myapp.views

urlPatterns=[
  ....your other routes that you've defined...
]
....

# Place at the end of the file and pass in the urlPatterns collection. 
# dj-qr will append your quick-routes.
initQuickRoutes(urlPatterns)
`


