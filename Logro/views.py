from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from Logro.models import Logro
from Logro.serializers import LogroSerializer

# Create your views here.

class CreateLogro(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        serializer = LogroSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'Logro creado exitosamente'}, status=status.HTTP_201_CREATED)

class ListaAllLogros(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        logros = Logro.objects.filter(usuario=request.user).order_by('-fecha')
        serializer = LogroSerializer(logros, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ListaFeedLogros(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        logro_propio = Logro.objects.filter(usuario=request.user).order_by('-fecha').first()
        logros_aleatorios = Logro.objects.exclude(usuario=request.user).order_by('?')[:5]

        data = {
            'logro_propio': LogroSerializer(logro_propio).data if logro_propio else None,
            'logros_aleatorios': LogroSerializer(logros_aleatorios, many=True).data,
        }

        return Response(data, status=status.HTTP_200_OK)

class EditarLogro(APIView):
    permission_classes = [AllowAny]

    def put(self, request, pk):
        try:
            logro = Logro.objects.get(pk=pk)
        except Logro.DoesNotExist:
            return Response({'message': 'Logro no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        if logro.usuario != request.user:
            return Response({'message': 'No tienes permisos para editar este logro'}, status=status.HTTP_403_FORBIDDEN)

        data = request.data
        serializer = LogroSerializer(logro, data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

class EliminarLogro(APIView):
    permission_classes = [AllowAny]

    def delete(self, request, pk):
        try:
            logro = Logro.objects.get(pk=pk)
        except Logro.DoesNotExist:
            return Response({'message': 'Logro no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        if logro.usuario != request.user:
            return Response({'message': 'No tienes permisos para eliminar este logro'}, status=status.HTTP_403_FORBIDDEN)

        logro.delete()
        return Response({'message': 'Logro eliminado exitosamente'}, status=status.HTTP_200_OK)

class OcultarLogro(APIView):
    permission_classes = [AllowAny]

    def put(self, request, pk):
        try:
            logro = Logro.objects.get(pk=pk)
        except Logro.DoesNotExist:
            return Response({'message': 'Logro no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        if logro.usuario != request.user:
            return Response({'message': 'No tienes permisos para ocultar este logro'}, status=status.HTTP_403_FORBIDDEN)

        data = request.data
        is_oculto = data.get('is_oculto')

        if is_oculto is None:
            return Response({'message': 'Proporcione el valor de `is_oculto`'}, status=status.HTTP_400_BAD_REQUEST)

        logro.is_oculto = is_oculto
        logro.save()

        return Response({'message': 'Logro oculto exitosamente'}, status=status.HTTP_200_OK)
