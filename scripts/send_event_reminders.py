#!/usr/bin/env python3
"""
Send email reminders for all events occurring in the next 2 weeks.

Requires:
    - GOOGLE_API_KEY environment variable
    - BREVO_API_KEY environment variable
    - CALENDAR_ID environment variable (defaults to contact@aikencamellias.org)
"""

import os
import requests
from datetime import datetime, timedelta, timezone
from googleapiclient.discovery import build


BREVO_LIST_ID_PROD = 4  # "Email Form" list (production)
BREVO_LIST_ID_TEST = 5  # Test list (manual dispatch)
BREVO_SENDER_EMAIL = "contact@aikencamellias.org"
BREVO_SENDER_NAME = "Aiken Camellia Society"


def fetch_events_for_date_range(service, calendar_id, start_date, end_date):
    """Fetch events within a specific date range."""
    events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=start_date.isoformat(),
        timeMax=end_date.isoformat(),
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    
    events = []
    for event in events_result.get('items', []):
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        events.append({
            'title': event.get('summary', 'Untitled Event'),
            'start': start,
            'end': end,
            'location': event.get('location', ''),
            'description': event.get('description', '')
        })
    return events


def format_event_date(date_str):
    """Format event date for display."""
    try:
        if 'T' in date_str:
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            return dt.strftime('%A, %B %d, %Y at %I:%M %p')
        else:
            dt = datetime.strptime(date_str, '%Y-%m-%d')
            return dt.strftime('%A, %B %d, %Y')
    except Exception:
        return date_str


def format_short_date(date_str):
    """Format event date for subject line."""
    try:
        if 'T' in date_str:
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        else:
            dt = datetime.strptime(date_str, '%Y-%m-%d')
        return dt.strftime('%b %d')
    except Exception:
        return date_str


def create_email_html(events):
    """Create HTML email content for event reminders."""
    html = """
    <html>
    <head>
        <style>
            body { font-family: 'Lato', Arial, sans-serif; color: #333; line-height: 1.6; }
            h1 { color: #2e7d32; font-family: 'Libre Baskerville', Georgia, serif; }
            h2 { color: #1b5e20; font-family: 'Libre Baskerville', Georgia, serif; }
            .event { background: #f5f5f5; padding: 20px; margin: 15px 0; border-left: 4px solid #2e7d32; }
            .event-title { font-size: 1.2em; font-weight: bold; color: #1b5e20; }
            .event-details { margin-top: 10px; }
            .label { font-weight: bold; color: #555; }
            .footer { margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; font-size: 0.9em; color: #666; }
        </style>
    </head>
    <body>
        <h1>Aiken Camellia Society - Upcoming Events</h1>
        <p>Here are the upcoming events for the next two weeks:</p>
    """
    
    for event in events:
        location_html = f'<p><span class="label">Location:</span> {event["location"]}</p>' if event["location"] else ''
        description_html = f'<p><span class="label">Details:</span> {event["description"]}</p>' if event["description"] else ''
        
        html += f"""
        <div class="event">
            <div class="event-title">{event["title"]}</div>
            <div class="event-details">
                <p><span class="label">Date:</span> {format_event_date(event["start"])}</p>
                {location_html}
                {description_html}
            </div>
        </div>
        """
    
    html += """
        <div class="footer">
            <p>We hope to see you there!</p>
            <p>Follow us on <a href="https://www.facebook.com/aikencamelliasociety/">Facebook</a> and 
            <a href="https://www.instagram.com/theaikencamelliasociety">Instagram</a> to connect with fellow enthusiasts.</p>
            <p>Aiken Camellia Society<br>
            <a href="https://aikencamellias.org">aikencamellias.org</a></p>
        </div>
    </body>
    </html>
    """
    return html


def create_email_text(events):
    """Create plain text email content for event reminders."""
    text = "AIKEN CAMELLIA SOCIETY - UPCOMING EVENTS\n\n"
    text += "Here are the upcoming events for the next two weeks:\n\n"
    
    for event in events:
        text += f"---\n"
        text += f"{event['title']}\n"
        text += f"Date: {format_event_date(event['start'])}\n"
        if event["location"]:
            text += f"Location: {event['location']}\n"
        if event["description"]:
            text += f"Details: {event['description']}\n"
        text += "\n"
    
    text += "---\n\n"
    text += "We hope to see you there!\n\n"
    text += "Aiken Camellia Society\n"
    text += "https://aikencamellias.org\n"
    
    return text


def send_brevo_email(events, brevo_api_key, test_mode=False):
    """Send email via Brevo API to the Email Form list."""
    list_id = BREVO_LIST_ID_TEST if test_mode else BREVO_LIST_ID_PROD
    mode_label = "[TEST] " if test_mode else ""
    
    # Create subject with event count and date range
    event_count = len(events)
    first_date = format_short_date(events[0]['start'])
    last_date = format_short_date(events[-1]['start'])
    
    if first_date == last_date:
        date_range = first_date
    else:
        date_range = f"{first_date} - {last_date}"
    
    subject = f"{mode_label}Upcoming Events: {event_count} event{'s' if event_count > 1 else ''} ({date_range})"
    
    url = "https://api.brevo.com/v3/emailCampaigns"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "api-key": brevo_api_key
    }
    
    payload = {
        "name": f"{mode_label}Weekly Event Reminder - {datetime.now().strftime('%Y-%m-%d')}",
        "subject": subject,
        "sender": {
            "name": BREVO_SENDER_NAME,
            "email": BREVO_SENDER_EMAIL
        },
        "recipients": {
            "listIds": [list_id]
        },
        "htmlContent": create_email_html(events),
        "textContent": create_email_text(events)
    }
    
    print(f"Using {'TEST' if test_mode else 'PRODUCTION'} list (ID: {list_id})")
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 201:
        campaign_id = response.json().get("id")
        print(f"Created email campaign {campaign_id}")
        
        send_url = f"https://api.brevo.com/v3/emailCampaigns/{campaign_id}/sendNow"
        send_response = requests.post(send_url, headers=headers)
        
        if send_response.status_code == 204:
            print(f"Successfully sent weekly event reminder email")
            return True
        else:
            print(f"Failed to send campaign: {send_response.status_code} - {send_response.text}")
            return False
    else:
        print(f"Failed to create campaign: {response.status_code} - {response.text}")
        return False


def main():
    google_api_key = os.environ.get('GOOGLE_API_KEY')
    if not google_api_key:
        raise ValueError('GOOGLE_API_KEY environment variable is required')
    
    brevo_api_key = os.environ.get('BREVO_API_KEY')
    if not brevo_api_key:
        raise ValueError('BREVO_API_KEY environment variable is required')
    
    calendar_id = os.environ.get('CALENDAR_ID', 'contact@aikencamellias.org')
    test_mode = os.environ.get('TEST_MODE', 'false').lower() == 'true'
    
    if test_mode:
        print("Running in TEST MODE - emails will be sent to test list (ID: 5)")
    
    service = build('calendar', 'v3', developerKey=google_api_key)
    
    now = datetime.now(timezone.utc)
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    two_weeks_end = today_start + timedelta(days=14)
    
    events = fetch_events_for_date_range(service, calendar_id, today_start, two_weeks_end)
    
    print(f"Found {len(events)} event(s) in the next 2 weeks")
    
    if events:
        send_brevo_email(events, brevo_api_key, test_mode)
    else:
        print("No events found for the next 2 weeks - no email sent")


if __name__ == '__main__':
    main()
