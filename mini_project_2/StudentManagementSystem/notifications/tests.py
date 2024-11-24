from django.test import TestCase
from notifications.tasks import send_bulk_notifications

class BulkNotificationCeleryTaskTest(TestCase):
    def test_send_bulk_notifications(self):
        emails = ["user1@example.com", "user2@example.com", "user3@example.com"]
        message = "This is a test notification"
        
        result = send_bulk_notifications.apply(args=[emails, message])

        self.assertTrue(result.successful())

        self.assertEqual(result.result, f"Sent to {len(emails)} recipients")