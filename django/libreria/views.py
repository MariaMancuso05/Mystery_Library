# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Libreria, Profilo, User, Acquisti, Autori, Categoria, Votazione
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy 
from django.views.generic import CreateView #crea un nuovo oggetto nel database
from django.contrib.auth import logout
from .forms import CartaFittiziaForm, ProfiloForm
from django.contrib import messages


def index(request):
    return HttpResponse("Indice della libreria.")

def homelib(request):
    return render(request, "libreria/homelib.html")

def shop(request):
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        libri_disponibili = Libreria.objects.filter(categorie__id=categoria_id)
    else:
        libri_disponibili= Libreria.objects.all()
    
    categorie = Categoria.objects.all()
    return render(request, 'libreria/shop.html', {
        # render(richiesta utente, mostra pagina html, mostra i dati inseriti).
        'libri': libri_disponibili, #libri è il nome della variabile usata nel template che prende i dati dal modello Libreria
        'categorie': categorie,
        'categoria_attiva': categoria_id 
        }) 

        #quantita_disponibile=Store.quantita()

def autori(request, autore_id):
    autore=Autori.objects.get(id=autore_id)
    return render(request, "libreria/autori.html", {"autore":autore}) #il template riceve una variabile chiamata autore con dentro tutti i dati dell’autore

def infolibri(request, libro_id):
    libro=Libreria.objects.get(id=libro_id)
    trama = getattr(libro, 'trame', None)
    votazioni = Votazione.objects.filter(libro=libro)

    return render(request, "libreria/infolibri.html", {
        "libro":libro,
        "trama":trama,
        "votazioni":votazioni
        }) 

#per la registrazione degli utenti
class SignUpView(CreateView): #per aggiungere un nuovo utente nel database dopo che è stata fatta la registrazione
    form_class = UserCreationForm #richiama il form già pronto di Django
    success_url = reverse_lazy("login") # quando la registrazione va a buon fine, l'utente viene mandato alla pagina di login.
    template_name = "registration/signup.html" #dice a Django quale template html mostrare per la pagina di registrazione.


@login_required #dopo il login viene mostrato il profilo dell'utente
def profilo_utente(request):
    profilo = Profilo.objects.get(username=request.user)
    # Recupera tutti gli acquisti dell'utente e carica anche i dati del libro in un'unica query
    acquisti = Acquisti.objects.filter(acquirente=request.user).select_related('oggetto_acquistato')
    
    return render(request, 'registration/profilo.html',{
        'profilo': profilo,
        'acquisti': acquisti
        })


@login_required
def modifica_profilo(request):
    profilo = Profilo.objects.get(username=request.user)
    
    if request.method == 'POST':
        form = ProfiloForm(request.POST, instance=profilo)
        if form.is_valid():
            form.save()
            return redirect('libreria:profilo') 
    else:
        form = ProfiloForm(instance=profilo)
    
    return render(request, 'registration/modifica_profilo.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, "registration/logout.html")


@login_required  #permette agli utenti loggati di acquistare i libri disponibili e di pagare tramite carta
def acquista_libro(request, oggetto_acquistato_id):
    libro = Libreria.objects.get(id=oggetto_acquistato_id)
    
    if request.method == 'POST':
        # Gestione dell'acquisto
        quantita = int(request.POST.get('quantita', 1))
        Acquisti.objects.create(acquirente=request.user, oggetto_acquistato=libro, quantita=quantita)
        #l'utente viene associato al proprio acquisto

        # Form della carta
        form = CartaFittiziaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('successo_pagamento')
    else:
        form = CartaFittiziaForm()

    return render(request, 'libreria/acquisti.html', {'libreria': libro, 'form': form})


def acquisto_completato(request):
    return render(request, "libreria/acquisto_completo.html")

#la view per la votazione dei libri acquistati dall'utente
@login_required
def vota_libro(request, libro_id):
    libro = Libreria.objects.get(id=libro_id)
    opzioni_voto = [(1, "1⭐"), (2, "2⭐"), (3, "3⭐"), (4, "4⭐"), (5, "5⭐")]

    if request.method == 'POST':
        voto_valore = int(request.POST.get('voto'))
        recensione = request.POST.get('recensione', '')

        votazione, created = Votazione.objects.update_or_create(
            user=request.user,
            libro=libro,
            defaults={'voto': voto_valore, 'recensione': recensione}
        )

        messages.success(request, "Grazie per la tua votazione!")
        return redirect('libreria:infolibri', libro_id=libro.id) 

    return render(request, 'libreria/votazione.html', {
        'libro': libro,
        'opzioni_voto': opzioni_voto
        })


#@login_required
#def lista_acquisti(request):
    #acquisti = Acquisti.objects.filter(acquirente=request.user)
    #return render(request, 'lista_acquisti.html', {'acquisti': acquisti})


#def libro_dettaglio(request, libro_id):
    #libro = get_object_or_404(Libreria, id=libro_id)
    #votazione_utente = Votazione.objects.filter(user=request.user, libro=libro).first()

    #if request.method == "POST":
        #voto = request.POST.get('voto')
        #recensione = request.POST.get('recensione', "")
        #if not votazione_utente:
            #Votazione.objects.create(user=request.user, libro=libro, voto=voto, recensione=recensione)
        #else:
            #votazione_utente.voto = voto
            #votazione_utente.recensione = recensione
            #votazione_utente.save()
        #return redirect('libro_dettaglio', libro_id=libro.id)

    #return render(
        #request,
        #'libreria/libro_dettaglio.html',
        #{'libro': libro, 'votazione_utente': votazione_utente}
    #)

#Recupera tutti i libri dal database.
#Passa i libri alla pagina HTML shop.html per mostrarli.




