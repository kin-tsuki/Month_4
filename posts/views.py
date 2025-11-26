from django.shortcuts import render, redirect 
from django.http import HttpResponse


def author_view(request):
    return HttpResponse("""English Modernism <br>Virginia Woolf (1882-1941) was an English novelist, essayist, biographer, and feminist.
Woolf was a prolific writer, whose modernist style changed with each new novel. 
Her letters and memoirs reveal glimpses of Woolf at the center of English 
literary culture during the Bloomsbury era. Woolf represents a historical moment 
when art was integrated into society, as T.S. Eliot describes in his obituary 
for Virginia. 'Without Virginia Woolf at the center of it, it would have 
remained formless or marginal…With the death of Virginia Woolf, a whole pattern of 
culture is broken.'""")


def html_view(request):
    return render(request, "base.html")
    

