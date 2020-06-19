# i have  created a file

from django.http import HttpResponse
def index(request):
    return HttpResponse('''<h1> mukesh </h1> <a href="https://www.youtube.com/">you tube</a><br>
                            <a href="https://www.codechef.com/">code chef</a><br>
                            <a href="https://www.codeforces.com/">codeforces</a><br>
                            ''')
def about(resquest):
    return HttpResponse("hello mukesh gaur")
