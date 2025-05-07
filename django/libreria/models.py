from django.db import models
from datetime import date
from django.contrib.auth.models import User
from creditcards.models import CardExpiryField, SecurityCodeField #per creare il form per la registrazione delle carte di credito

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
      return self.nome #per fare in modo che l'oggetto venga salvato con il nome del genere scritto


class Libreria(models.Model):
    titolo = models.CharField(max_length=100)
    autore = models.ForeignKey("Autori", on_delete=models.CASCADE)
    categorie = models.ManyToManyField(Categoria)
    prezzo = models.DecimalField(max_digits=4, decimal_places=2) 
    copertina = models.ImageField(upload_to="copertine/", blank=True, null=True) #upload della copertina del libro che poi viene mostrata nel template

    def __str__(self):
      return f"{self.titolo} - {self.autore}" #l'oggetto registrato prende il nome dal titolo del libro e autore

#autori dei libri
class Autori(models.Model):
   nome= models.CharField(max_length=20)
   cognome=models.CharField(max_length=30)
   data_nascita=models.DateField()
   presentazione_dell_autore= models.TextField(max_length=1500)
   immagine = models.ImageField(upload_to="autori/", blank=True, null=True)

   def __str__(self):
      return f"{self.nome}" + f" {self.cognome}"

#Trame dei libri
class Trame(models.Model):
   trame=models.TextField(max_length=2500)
   libro=models.OneToOneField(Libreria, on_delete=models.CASCADE) #perché ogni libro ha una sola trama
    
   def __str__(self):
       return f"{self.libro}"

#Acquisti effettuati dai clienti
class Acquisti(models.Model):
    acquirente = models.ForeignKey(User, on_delete=models.CASCADE)
    oggetto_acquistato = models.ForeignKey(Libreria, on_delete=models.CASCADE)
    data_acquisto = models.DateTimeField(auto_now_add=True)
    quantita = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.acquirente.username} - {self.oggetto_acquistato.titolo} ({self.data_acquisto.strftime('%d-%m-%Y')})"

#il numero di oggetti nello store diminuisce in base al numero di acquisti effettuati
class Store(models.Model):
   libro=models.ForeignKey(Libreria, on_delete=models.CASCADE)
   quantita=models.IntegerField() 

   def __str__(self):
      return f"{self.libro}"
   

# Modello per la votazione e recensione
class Votazione(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libreria, on_delete=models.CASCADE)
    voto = models.PositiveIntegerField(choices=[ #accetta solo valori interi positivi
      (1, "1⭐"), 
      (2, "2⭐"), 
      (3, "3⭐"), 
      (4, "4⭐"), 
      (5, "5⭐"), 
    ])
    recensione = models.TextField(blank=True, null=True)  #Campo opzionale

    class Meta():
        unique_together = ('user', 'libro')  # Un utente può votare un libro solo una volta

    def __str__(self):
        return f"{self.user.username} ha dato {self.voto} ⭐ al libro {self.libro.titolo}"

#il profilo di un utente registrato  
class Profilo(models.Model):
   username= models.OneToOneField(User, on_delete=models.CASCADE)
   nome=models.CharField(max_length=25)
   cognome=models.CharField(max_length=35)
   email=models.EmailField()
   data_di_nascita = models.DateField(blank=True, null=True)
   bio=models.TextField(blank=True, null=True)

   def __str__(self):
      return f"Profilo di {self.nome} {self.cognome}"
   
#per aggiungere i dati della carta in modo da effettuare gli acquisti
class CartaFittizia(models.Model):
    titolare_della_carta=models.CharField(max_length=100)
    numero_della_carta = models.CharField(max_length=16)
    data_di_scadenza = CardExpiryField(max_length=5)
    cvv = SecurityCodeField(max_length=3)

    def __str__(self):
       return f"Carta di {self.titolare_della_carta}"





