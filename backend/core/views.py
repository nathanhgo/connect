from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

@extend_schema(
    summary="Teste de Conexão (Ping:Pong)",
    description="Endpoint simples para validar se a API e o App Mobile estão se comunicando corretamente.",
    responses={200: dict}
)
@api_view(['GET'])
def ping_pong_test(request):
    return Response({
        "status": "Genial!", 
        "message": "Backend Django conectado através do App Core (via DRF)!"
    })