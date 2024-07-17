from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Like, Logro
from .serializers import LikeSerializer, LikeLogroSerializer, ConteoLikesSerializer
from django.shortcuts import get_object_or_404


class DarLikeView(generics.CreateAPIView):
    """Vista para dar like a un logro."""

    serializer_class = LikeSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        logro = get_object_or_404(Logro, pk=self.request.data['logro'])
        usuario = self.request.user

        # Verificar si el usuario ya ha dado like al logro
        like_existente = Like.objects.filter(usuario=usuario, logro=logro).exists()
        if like_existente:
            return Response({'mensaje': 'Ya has dado like a este logro.'}, status=400)

        # Crear el like
        like = Like.objects.create(usuario=usuario, logro=logro)
        serializer = LikeSerializer(like)
        return Response(serializer.data, status=201)


class EliminarLikeView(generics.DestroyAPIView):
    """Vista para eliminar un like de un logro."""

    serializer_class = LikeSerializer
    permission_classes = [permissions.AllowAny]

    def destroy(self, request, *args, **kwargs):
        logro = get_object_or_404(Logro, pk=self.kwargs['pk'])
        usuario = self.request.user

        # Verificar si el usuario ha dado like al logro
        like = get_object_or_404(Like, usuario=usuario, logro=logro)

        # Eliminar el like
        like.delete()
        return Response({'mensaje': 'Like eliminado correctamente.'}, status=200)


class ListarLikesLogroView(generics.ListAPIView):
    """Vista para listar los likes de un logro."""

    serializer_class = LikeLogroSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        logro = get_object_or_404(Logro, pk=self.kwargs['pk'])
        return Like.objects.filter(logro=logro)


class ObtenerConteoLikesView(generics.RetrieveAPIView):
    """Vista para obtener el conteo de likes de un logro."""

    serializer_class = ConteoLikesSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        logro = get_object_or_404(Logro, pk=self.kwargs['pk'])
        cantidad_likes = Like.objects.filter(logro=logro).count()
        return {'cantidad_likes': cantidad_likes}
