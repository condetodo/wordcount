from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()

    word_dictonary = {}

    for word in word_list:
        if word in word_dictonary:
            # Increase
            word_dictonary[word] += 1
        else:
            # add to dictonary
            word_dictonary[word] = 1
    sorted_words = sorted(word_dictonary.items(), key=operator.itemgetter(1), reverse=True)
   
    return render(request, 'count.html', {'fulltext': fulltext, 'count':len(word_list), 'sorted_words':sorted_words})

def about(request):
    return render(request, 'about.html')
    