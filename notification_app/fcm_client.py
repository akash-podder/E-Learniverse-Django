import firebase_admin
from django.conf import settings
from firebase_admin import credentials, messaging

cred = credentials.Certificate(settings.GOOGLE_APPLICATION_CREDENTIALS)
firebase_admin.initialize_app(cred)

class FCMClient:

    def create_message(self, message_payload, registration_token):
        message = messaging.Message(
            data=message_payload,
            token=registration_token,
        )
        return message

    def create_multicast_message(self, message_payload, fcm_tokens):
        multicast_message = messaging.MulticastMessage(
            data=message_payload,
            tokens=fcm_tokens
        )
        return multicast_message

    def send_message(self, message_payload, registration_token):
        message = self.create_message(message_payload, registration_token)
        messaging.send(message)

    def send_multicast_message(self, payload, fcm_tokens):
        multicast_message = self.create_multicast_message(payload, fcm_tokens)
        batch_response = messaging.send_multicast(multicast_message)
        return batch_response

    def send_all_message(self, messages):
        batch_response = messaging.send_all(messages)
        return batch_response


    def send_push_notification(self, token, title, body, data=None):
        message = messaging.Message(
            notification=messaging.Notification(title=title, body=body),
            token=token,
            data=data
        )

        response = messaging.send(message)
        print('Successfully sent push notification:', response)
