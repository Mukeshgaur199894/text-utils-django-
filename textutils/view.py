

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index2.html')

def  analyze(request):
    #get the text
    djtext=request.POST.get('text','default')

    #chosse the opertaion in djtext
    removepunc=request.POST.get('removepunc','off')
    capfirst=request.POST.get('capfirst','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')


    if removepunc=="on":
        analyzed = ""
        punctuation = '''(){}[]-_'"><,./?\|!@#$%^;&*~'''
        for char in djtext:
            if char not in punctuation:
                analyzed+=char
        params={'purpose':'Remove punctuation ','analyzed_text':analyzed}
        #analyze the text
        djtext=analyzed
        # return render(request,'analyze2.html',params)

    if capfirst=="on":
        analyzed=""
        for char in djtext:
            analyzed+=char.upper()
        params={'purpose':'capitalised the letter','analyzed_text':analyzed}
        # return render(request,'analyze2.html',params)
        djtext=analyzed

    if newlineremover=="on":
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed += char
        params = {'purpose': 'new line remover', 'analyzed_text': analyzed}
        # return render(request, 'analyze2.html', params)
        djtext=analyzed
    if extraspaceremover=="on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if  not(djtext[index-1]==" " and djtext[index]==" "):
                analyzed += char
        params = {'purpose': 'extra space remover', 'analyzed_text': analyzed}
        # return render(request, 'analyze2.html', params)
        djtext=analyzed
    elif charcount=="on":
        count=0
        word="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in djtext:
            if i in word:
                count+=1
        params = {'purpose': 'character count in the text','analyzed_text':analyzed,'count': count}
        # return render(request, 'analyze2.html', params)


    if (removepunc!='on' and charcount!='on' and extraspaceremover!='on' and newlineremover!="on"and capfirst!="on"):
        return HttpResponse("please select the correct operation ")
    return render(request,'analyze2.html' ,params)
