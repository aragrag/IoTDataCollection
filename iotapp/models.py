from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class IoTObject(models.Model):
    name = models.CharField(max_length=100)
    auth_token = models.OneToOneField(Token, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name = "Objet IoT"
        verbose_name_plural = "Objets IoT"

class IoTData(models.Model):
    # object = models.ForeignKey(IoTObject, on_delete=models.CASCADE)
    object = models.ForeignKey('iotapp.IoTObject', on_delete=models.CASCADE, related_name='datas')

    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # Autres champs pour les données, si nécessaire
    class Meta:
        verbose_name = "Donnée IoT"
        verbose_name_plural = "Données IoT"


# Créez une fonction pour générer un token d'authentification pour un utilisateur (ou une instance de IoTObject)
def generate_auth_token(instance):
    user, created = User.objects.get_or_create(username=instance.name)
    if created:
        user.set_unusable_password()
        user.save()
    token, created = Token.objects.get_or_create(user=user)
    return token

@receiver(post_save, sender=IoTObject)
def create_auth_token(sender, instance, created, **kwargs):
    if created:
        token = generate_auth_token(instance)
        instance.auth_token = token
        instance.save()