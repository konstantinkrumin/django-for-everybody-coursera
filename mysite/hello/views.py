from django.http import HttpResponse

def HelloView(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    response = HttpResponse('view count='+str(num_visits))
    response.set_cookie('dj4e_cookie', '4a914e5c', max_age=1000)
    return response