"""pollsapp URL Configuration

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
from django.contrib import admin
from django.urls import include, path
from . import routers
from polls import views as polls_views
from polls.views import TrackView

urlpatterns = [
    path('', polls_views.index, name='index'),

    path('track/post/', TrackView.as_view()),
    path('track/get/', TrackView.as_view()),
    # path('track/delete/<int:pk>/', TrackView.as_view()),

    path('count/', polls_views.total_count),
    path('listquestions/',polls_views.fetch_questions_list),

    path('polls/', include('polls.urls')),
    path('api/', include(routers.SharedAPIRootRouter.router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]