# Manually created by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return render(request,'index.html')
    # return HttpResponse("hello")


def analyze(request):
    # Get the text
    djtext = request.POST.get('text','default')
    
    # Check checkbox value
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    
    # print(djtext) 
    # print(removepunc)
    
    
    analyze = ""
    punctuation = '''!()-[]{};:'"\/,<>.?@#$%^&*_~'''
    
    # check which checkbox is on
    if removepunc == "on":
        for char in djtext:
            if char not in punctuation:
                analyze = analyze + char
    
        params={
            'purpose':"Remove punc :-",
            'analyzed_text':analyze,
        }
        # return render(request,'analyze.html',params)
        djtext = analyze
    
    
    if(fullcaps == "on"):
        analyze = ""
        for char in djtext:
            analyze = analyze + char.upper()
        
        params={
            'purpose':"Change to upper case :- ",
            'analyzed_text':analyze,
        }
        # return render(request,'analyze.html',params)
        djtext = analyze
    
    
    if(extraspaceremover == "on"):
        analyze = ""
        for index, char in enumerate(djtext):                         
            if not (djtext[index] == " "  and djtext[index + 1 ] == " "):
                analyze = analyze + char
                
        params={
            'purpose':"Remove space :- ",
            'analyzed_text':analyze,
        }
        # return render(request,'analyze.html',params)
        djtext = analyze
    
    
    if(newlineremover == "on"):
        analyze = ""
        for char in djtext:                
            if char != "\n" and char != "\r":
                analyze = analyze + char.upper()
        
        params={
            'purpose':"Remove New lines :- ",
            'analyzed_text':analyze,
        }
        # return render(request,'analyze.html',params)
        djtext = analyze

        
    if(removepunc != "on" and fullcaps != "on" and extraspaceremover != "on" and newlineremover != "on"):
        return HttpResponse("Error(please Tick checkbox)")
    
    return render(request,'analyze.html',params)
