"""forrest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewset,AmanatViewset,AzoViewset

router = DefaultRouter()
router.register(r'books',BookViewset)

routerAzo = DefaultRouter()
routerAzo.register(r'azo',AzoViewset)


routerAmanat = DefaultRouter()
routerAmanat.register(r'amanat',AmanatViewset)


urlpatterns = [
    # url('books/(?P<id>[0-9]+)/',BooksView.as_view()),
    # url('books/$', BooksView.as_view()),
    # url('azo/',   AzoView.as_view()),
    path('',include(router.urls)),
    path('',include(routerAzo.urls)),
    path('',include(routerAmanat.urls)),



 ]
