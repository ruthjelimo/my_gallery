from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Author
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
    # return HttpResponse('Ruth gallery site')

def album_of_day(request):
    date = dt.date.today()
    return render(request, 'all-albums/today-album.html', {"date": date,})
   

# Create your views here.

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def album_of_day(request):
    date = dt.date.today()

    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>Album for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)
def past_days_album(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request, 'all-albums/past-album.html', {"date": date})