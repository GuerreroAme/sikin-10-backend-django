from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, FileExtensionValidator

class Logro(models.Model):
    """Modelo para almacenar los logros de los usuarios."""

    usuario = models.CharField(max_length=120, verbose_name="Nombre Usuario")
    titulo = models.CharField(max_length=120, verbose_name="Título", blank=False, validators=[MaxLengthValidator(120)])
    fecha = models.DateField(verbose_name="Fecha")
    area = models.CharField(max_length=120, verbose_name="Área", choices=[
        ('personal', 'Personal'),
        ('profesional', 'Profesional'),
        ('aprendizaje', 'Aprendizaje'),
        ('deportiva', 'Deportiva'),
        ('laboral', 'Laboral'),
    ])
    descripcion = models.TextField(verbose_name="Descripción", max_length=255, validators=[MaxLengthValidator(255)])
    imagen = models.ImageField(upload_to="imagenes/logros", verbose_name="Imagen", validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])

    def obtener_logros_por_usuario(self, usuario):
        """Obtiene todos los logros de un usuario específico."""
        return Logro.objects.filter(usuario=usuario)

    def obtener_logros_por_area(self, area):
        """Obtiene todos los logros de una área específica."""
        return Logro.objects.filter(area=area)

    class Meta:
        db_table = 'logros'

