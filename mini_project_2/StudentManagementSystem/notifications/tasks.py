from celery import shared_task

@shared_task
def send_bulk_notifications(emails, message):
    for email in emails:
        print(f"Notification sent to {email}: {message}")
    return f"Sent to {len(emails)} recipients"