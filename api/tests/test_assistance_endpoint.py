from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from unittest.mock import patch, Mock
from app.assistance.domain.assistance_request import AssistanceRequest

class AssistanceEndpointTestCase(APITestCase):
    def setUp(self):
        self.assistance_endpoint = reverse('assistance')

    def build_mock_function(self, request):
        def return_mock_channel(req: AssistanceRequest):
            self.assertEqual(req.topic(), request['topic'])
            self.assertEqual(req.description(), request['description'])
            return True
        return return_mock_channel
        
    @patch('app.assistance.application.channel_selector.ChannelSelector.select_channel')
    def test_pricing_channel_is_selected(self, mock_select_channel):
       
        request = {'topic': 'pricing', 'description': 'test question about pricing'}
        
        mock_channel = Mock(emit=self.build_mock_function(request))
        
        mock_select_channel.return_value = mock_channel
        
        response = self.client.post(
            self.assistance_endpoint, 
            request
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mock_select_channel.assert_called_once()

        args, kwargs = mock_select_channel.call_args
        self.assertEqual(args[0], request['topic'])

    @patch('app.assistance.application.channel_selector.ChannelSelector.select_channel')
    def test_sales_channel_is_selected(self, mock_select_channel):
        request = {'topic': 'sales', 'description': 'test question about sales'}
        
        mock_channel = Mock(emit=self.build_mock_function(request))
        mock_select_channel.return_value = mock_channel
        
        response = self.client.post(
            self.assistance_endpoint, 
            request
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mock_select_channel.assert_called_once()

        args, kwargs = mock_select_channel.call_args
        self.assertEqual(args[0], request['topic'])
    
    def test_invalid_topic_returns_bad_request(self):
        response = self.client.post(
            self.assistance_endpoint, 
            data={'topic': 'invalid_topic', 'description': 'test'}
        )
        
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def test_missing_both_fields_returns_bad_request(self):
        response = self.client.post(
            self.assistance_endpoint, 
            data={}
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_description_returns_bad_request(self):
        response = self.client.post(
            self.assistance_endpoint, 
            data={'topic': 'pricing'}
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_topic_returns_bad_request(self):
        response = self.client.post(
            self.assistance_endpoint, 
            data={'description': 'test'}
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)