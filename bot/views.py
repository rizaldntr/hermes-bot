import os
import logging

from pathlib import Path
from dotenv import load_dotenv

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from .models import ScheduleDetail, TrackDetail, TransportDetail

load_dotenv(dotenv_path='.env')
logger = logging.getLogger(__name__)

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
parser_api = WebhookParser(os.getenv('LINE_CHANNEL_SECRET'))

DEFAULT_MESSAGE_COMMAND_NOT_FOUND = "Perintah tidak ditemukan!"

def check_all_transport():
    transports = TransportDetail.objects.all()
    text = ""
    for transport in transports:
        text = text + transport.transport_name + "\n"
    return text

def check_track_by_transport(transport, args):
    try:
        transport = TransportDetail.objects.filter(transport_name=transport).first()
        schedules = transport.schedules.all()
        text = ""
        for schedule in schedules:
            text = text + schedule.name + "\n"
        return text
    except TransportDetail.DoesNotExist:
        return "Rute tidak ditemukan"

def parser_check_command(text, args):
    if text == "rute":
        return check_track_by_transport(args[2], args)
    elif text == "all":
        return check_all_transport()

def parser(event):
    try:
        reply_text = DEFAULT_MESSAGE_COMMAND_NOT_FOUND
        if isinstance(event, MessageEvent):
            if isinstance(event.message, TextMessage):
                argums = event.message.text.split(" ")
                if len(argums) <= 1:
                    reply_text = DEFAULT_MESSAGE_COMMAND_NOT_FOUND
                elif argums[0] == "/check":
                    reply_text = parser_check_command(argums[1], argums)
    except Exception as e:
        print(e)
        
    try:
        line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=reply_text)
            )         
    except Exception as e:
        logger.error(e)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser_api.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:    
            parser(event)

        return HttpResponse()
    else:
        return HttpResponseBadRequest()