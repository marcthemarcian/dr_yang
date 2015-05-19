from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from yang import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dr_yang.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^questionnaire/', views.QuestionnaireView.as_view(), name="questionnaire"),
    url(r'^assess/', views.AssessView.as_view(), name="assess"),
    url(r'^about/', views.AboutView.as_view(), name="about"),
)
