from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import BasePermission,AllowAny
from .serializer import DrawingSerializer, PriceListSerializer
from .models import Drawings,PriceList
from .permissions import JoinedTelegramPermission
import requests
from rest_framework.exceptions import PermissionDenied
from django.conf import settings
# Create your views here.

BOT_TOKEN = "8222393995:AAFfW_59J-5OTbsSl-9NJz7DDcXeTZHKRms"
CHANNEL_USERNAME = "@Jaredrawing"


class DrawingListView(generics.ListAPIView):
    queryset = Drawings.objects.all()
    serializer_class = DrawingSerializer
    

class PriceListView(generics.ListAPIView):
    queryset = PriceList.objects.all()
    serializer_class = PriceListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        telegram_user_id = self.request.query_params.get("telegram_user_id")
        if not telegram_user_id:
            raise PermissionDenied("Telegram user ID is required")

        # 1️⃣ Check membership from Telegram
        telegram_channel_username = "@Jaredrawing"  # e.g. "@Jaredrawing"
        bot_token = settings.TELEGRAM_BOT_TOKEN

        url = f"https://api.telegram.org/bot{bot_token}/getChatMember"
        params = {"chat_id": telegram_channel_username, "user_id": telegram_user_id}
        response = requests.get(url, params=params)

        if response.status_code != 200:
            raise PermissionDenied("Telegram verification failed")

        data = response.json()

        # 2️⃣ Check membership status
        status = data.get("result", {}).get("status", "")
        if status not in ["member", "administrator", "creator"]:
            raise PermissionDenied("User is not a member of the channel")

        # ✅ Return all price list items if joined
        return PriceList.objects.all()