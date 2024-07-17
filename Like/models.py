from django.db import models
from Logro.models import Logro

class Like(models.Model):
    """Modelo para almacenar los likes de los logros."""

    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Usuario")
    logro = models.ForeignKey(Logro, on_delete=models.CASCADE, verbose_name="Logro")
    fecha_like = models.DateTimeField(auto_now_add=True, verbose_name="Fecha del like")

    class Meta:
        db_table = 'likes'
        unique_together = ['usuario', 'logro']  # Un usuario solo puede dar like a un logro una vez

    def __str__(self):
        return f"{self.usuario.username} dio like al logro {self.logro.titulo}"