from dependency_injector import containers, providers
from app.assistance.application.channel_selector import ChannelSelector 
from app.assistance.infrastructure.emitters.slack_channel_emitter import SlackChannelEmitter
from app.assistance.infrastructure.emitters.email_channel_emitter import EmailChannelEmitter
from app.assistance.infrastructure.emitters.celery_channel_emitter import CeleryChannelEmitterDecorator
from app.assistance.infrastructure.clients.slack_client import SlackClient
from app.assistance.domain.topic import Topic
from app.assistance.application.assistance_request_service import AssistanceRequestService
from dotenv import load_dotenv
import os

load_dotenv()

class Container(containers.DeclarativeContainer):
        
    #Now all services can be singleton 
    slack_client = providers.Singleton(SlackClient, token=os.getenv('SLACK_TOKEN'))

    slack_channel_emitter_internal = providers.Singleton(SlackChannelEmitter, client=slack_client)
    email_channel_emitter_intenral = providers.Singleton(EmailChannelEmitter)

    CeleryWrapper = False 

    slack_channel_emitter = providers.Singleton(CeleryChannelEmitterDecorator, emitter=slack_channel_emitter_internal) if CeleryWrapper else slack_channel_emitter_internal
    email_channel_emitter = providers.Singleton(CeleryChannelEmitterDecorator, emitter=email_channel_emitter_intenral) if CeleryWrapper else email_channel_emitter_intenral

    channel_mapping = providers.Dict(
        sales = slack_channel_emitter,   
        pricing = email_channel_emitter
    )

    channel_selector = providers.Singleton(ChannelSelector, channel_mapping=channel_mapping)

    assistance_request_service = providers.Factory(AssistanceRequestService, channel_selector=channel_selector)
