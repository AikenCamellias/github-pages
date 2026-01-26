#!/usr/bin/env python3
"""
Fetch upcoming events from Google Calendar and write to _data/events.yml.

Requires:
    - GOOGLE_API_KEY environment variable
    - CALENDAR_ID environment variable (defaults to contact@aikencamellias.org)
    - Google Calendar must be public or have public event details enabled
"""

import os
import yaml
from datetime import datetime, timedelta, timezone
from googleapiclient.discovery import build


def fetch_events():
    api_key = os.environ.get('GOOGLE_API_KEY')
    if not api_key:
        raise ValueError('GOOGLE_API_KEY environment variable is required')

    calendar_id = os.environ.get('CALENDAR_ID', 'contact@aikencamellias.org')

    service = build('calendar', 'v3', developerKey=api_key)

    now = datetime.now(timezone.utc)
    time_min = now.isoformat()
    time_max = (now + timedelta(days=30)).isoformat()

    events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=time_min,
        timeMax=time_max,
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

    output = {
        'last_updated': datetime.now(timezone.utc).isoformat(),
        'events': events
    }

    os.makedirs('_data', exist_ok=True)
    with open('_data/events.yml', 'w') as f:
        yaml.dump(output, f, default_flow_style=False, allow_unicode=True)

    print(f'Wrote {len(events)} events to _data/events.yml')


if __name__ == '__main__':
    fetch_events()
