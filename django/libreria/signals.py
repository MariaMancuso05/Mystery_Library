from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Acquisti, Store

@receiver(post_save, sender=Acquisti)
def aggiorna_magazzino(sender, instance, created, **kwargs):
    if created:  # Solo al momento della creazione dell'acquisto
        try:
            store_entry = Store.objects.get(libro=instance.oggetto_acquistato)
            store_entry.quantita -= instance.quantita
            store_entry.quantita = max(store_entry.quantita, 0)  # Evita quantità negative
            store_entry.save()
        except Store.DoesNotExist:
            print("Libro non presente nel magazzino")





