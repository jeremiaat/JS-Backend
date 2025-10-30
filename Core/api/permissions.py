# api/permissions.py
from rest_framework.permissions import BasePermission

class JoinedTelegramPermission(BasePermission):
    message = "You must join the Telegram channel to view this."

    def has_permission(self, request, view):
        telegram_user_id = request.query_params.get('telegram_user_id')
        if not telegram_user_id:
            return False

        # Replace with real joined user IDs or DB check
        allowed_users = ["1786951273", "1234567890"]
        return telegram_user_id in allowed_users
