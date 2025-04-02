
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.assistance import AssistanceSerializer
from app.assistance.application.assistance_request_service import AssistanceRequestService
from app.assistance.application.channel_selector import ChannelSelector
from rest_framework import serializers
from app.common.container import Container

class AssistanceView(APIView):
    def post(self, request):
        data = AssistanceSerializer(data=request.data)
        if not data.is_valid():
            raise serializers.ValidationError(data.errors)
        
        #Convert serializer data to domain model
        assistance_request = data.to_domain_model()
        #Instantiate service
        service = Container.assistance_request_service()
        #Send assistance request
        response = service.handle(assistance_request)

        return Response({'ok':True, 'message': response})
    

    def get(self, request):
        test = {
            'topic': 'sales',
            'description': 'This is a test description'
        }
        return Response(test)
