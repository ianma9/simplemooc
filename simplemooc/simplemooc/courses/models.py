from django.db import models
from django.urls import reverse

class Course(models.Model):

    name = models.CharField(
        'Nome', 
        max_length=100
    )
    slug = models.SlugField(
        'Atalho'
    )
    description = models.TextField(
        'Descrição Simples', 
        blank=True
    )
    about = models.TextField(
        'Sobre o Curso', 
        blank=True
    )
    start_date = models.DateField(
        'Data de Início', 
        null=True,  
        blank=True
    )
    
    image = models.FileField(
        upload_to='courses/images', 
        verbose_name='Imagem', 
        blank=True
    )
    
    created_at = models.DateTimeField(
        'Criado em', 
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Atuailzado em', 
        auto_now=True
    )

    def __str__(self):
        return self.name
 
    def get_absolute_url(self):
        return reverse('details', 
        args=[str(self.slug)]
    )

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'



