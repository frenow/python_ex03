from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from ..models import Pessoa, Endereco, Setor, Cargo

@require_http_methods(["GET","POST"])
def home(request):
	return HttpResponse("Olá, requisição feita com sucesso!")

@csrf_exempt
@require_http_methods(["POST","GET"])
def listar(request):
	lista = Pessoa.objects.all()
	html = "<ul>"
	for p in lista:
		html+=f"<li>{p.nome} (id={p.id})</li>"
	html+= "</ul>"
	return HttpResponse(html)

def detalhar(request, id_pessoa):
	pessoa = Pessoa.objects.get(id=id_pessoa)
	return HttpResponse(f"Detalhou {pessoa.nome} (id={pessoa.id})")

def excluir(request, id_pessoa):
	try:
		pessoa = Pessoa.objects.get(id=id_pessoa)
		pessoa.delete()		
		return HttpResponse(f"Excluiu {pessoa.nome} (id={pessoa.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Pessoa não encontrada")

def cadastrar(request):
	p = Pessoa(nome="Emerson", idade=20)
	p.save()
	return HttpResponse(f"{p.nome} cadastrado com sucesso (id={p.id})")

def cadastrar_setor(request):
	s = Setor(descricao="Recursos Humano")
	s.save()
	return HttpResponse(f"{s.descricao} cadastrado com sucesso (id={s.id})")

def listar_setor(request):
	lista = Setor.objects.all()
	html = "<ul>"
	for s in lista:
		html+=f"<li>{s.descricao} (id={s.id})</li>"
	html+= "</ul>"
	return HttpResponse(html)

def detalhar_setor(request, id_setor):
	setor = Setor.objects.get(id=id_setor)
	return HttpResponse(f"Detalhou {setor.descricao} (id={setor.id})")

def excluir_setor(request, id_setor):
	try:
		setor = Setor.objects.get(id=id_setor)
		setor.delete()		
		return HttpResponse(f"Excluiu {setor.descricao} (id={setor.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Setor não encontrado")

def cadastrar_cargo(request):
	c = Cargo(descricao="Programador", cbo=123456)
	c.save()
	return HttpResponse(f"{c.descricao} cadastrado com sucesso (id={c.id})")

def listar_cargo(request):
	lista = Cargo.objects.all()
	html = "<ul>"
	for c in lista:
		html+=f"<li>{c.descricao} (id={c.id})</li>"
	html+= "</ul>"
	return HttpResponse(html)

def detalhar_cargo(request, id_cargo):
	cargo = Cargo.objects.get(id=id_cargo)
	return HttpResponse(f"Detalhou {cargo.descricao} (id={cargo.id})")

def excluir_cargo(request, id_cargo):
	try:
		cargo = Cargo.objects.get(id=id_cargo)
		cargo.delete()		
		return HttpResponse(f"Excluiu {cargo.descricao} (id={cargo.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Cargo não encontrado")