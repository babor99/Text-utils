from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')

def analyze(request):

    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')

    if removepunc == "on":
        punctuations ='''!()-[]{};:'"/,<>.\?@#$%^&*`~_|'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char 
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed }
        djtext = analyzed

    if capitalize == "on":
        analyzed = ""
        for char in djtext:
            analyzed +=char.upper()
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed }
        djtext = analyzed
            
    if extraspaceremove == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed += char
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed }
        djtext = analyzed

    if newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed += char
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed }

    if (removepunc != "on" and capitalize != "on" and newlineremove != "on" and extraspaceremove != "on"):
        return HttpResponse('Error')

    return render(request, 'analyze.html', params)

    

    
    

 