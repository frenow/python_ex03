from django.urls import path

from .views import people_views as pv

urlpatterns = [
	path('', pv.home, name="index"),
	path('listar/', pv.listar, name="listar"),
	path('detalhar/<int:id_pessoa>/', pv.detalhar, name="detalhar"),
	path('excluir/<int:id_pessoa>/', pv.excluir, name="excluir"),
	path('cadastrar/', pv.cadastrar, name="cadastrar"),
	path('cadastrar_setor/', pv.cadastrar_setor, name="cadastrar_setor"),
	path('listar_setor/', pv.listar_setor, name="listar_setor"),
	path('excluir_setor/<int:id_setor>/', pv.excluir_setor, name="excluir_setor"),
	path('detalhar_setor/<int:id_setor>/', pv.detalhar_setor, name="detalhar_setor")
]