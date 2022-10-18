from django.contrib import admin
from django.urls import path
from cover.views import indexcover
from pendahuluan.views import indexpendahuluan
from katapengantar.views import indexkatapengantar
from materi1.views import indexmateri1
from materi2.views import indexmateri2
from videopembelajaran.views import indexvideopembelajaran
from aplikasigeogebra.views import indexaplikasigeogebra
from daftarpustaka.views import indexdaftarpustaka
from glosarium.views import indexglosarium
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cover/', indexcover),
    path('pendahuluan/', indexpendahuluan),
    path('katapengantar/', indexkatapengantar),
    path('materi1/', indexmateri1),
    path('materi2/', indexmateri2),
    path('videopembelajaran/', indexvideopembelajaran),
    path('aplikasigeogebra/', indexaplikasigeogebra),
    path('daftarpustaka/', indexdaftarpustaka),
    path('glosarium/', indexglosarium),
]
