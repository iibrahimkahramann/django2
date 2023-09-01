from django.shortcuts import render
page_defaults = {
    "title": "başlıksız"
}
def homepage(request):
    name = "orhan"
    content ={
        "title":"anasyfa",
        "body": "<h1>anasyafa</h1>"
    }
    context  ={
        **page_defaults,
        **content
    }

    return render(request,"pages/page.html",context)

def about(request):
    content = {
        "title":"hakkımızda",
        "body": "<h1>hakkımızda</h1>"
    }
    context = {
        **page_defaults,
        **content
    }

    return render(request,"pages/page.html",context)

def contact(request):
    content = {
        "title":"iletişim",
        "body": "<h1>iletişim</h1>"
    }
    context = {
        **page_defaults,
        **content
    }
    return render(request,"pages/page.html",context)




