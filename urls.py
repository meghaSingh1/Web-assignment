import ...

urlpattern=[
     url(r'^$',views.index,name='index'),
     url(r'^add_movie/$',views.AddMovie,name='add_movie'),
     url(r'^add_movie_form_submission/$',
     	views.add_movie_form_submission,name='add_movie_form_submission')
     
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)