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
from datetime import datetime, timedelta, timezone, date
from googleapiclient.discovery import build


def format_event_display(start, end, all_day):
    """Return (display_date, display_time) strings for an event."""
    if all_day:
        start_date = date.fromisoformat(start)
        # Google Calendar API end dates for all-day events are exclusive
        end_date = date.fromisoformat(end) - timedelta(days=1)

        if start_date == end_date:
            display_date = start_date.strftime('%B %-d')
        elif start_date.month == end_date.month:
            display_date = f"{start_date.strftime('%B %-d')} - {end_date.day}"
        else:
            display_date = f"{start_date.strftime('%B %-d')} - {end_date.strftime('%B %-d')}"

        return display_date, '[See Calendar](/events/#calendar)'
    else:
        dt_start = datetime.fromisoformat(start)
        dt_end = datetime.fromisoformat(end)
        display_date = dt_start.strftime('%B %-d, %Y')
        display_time = f"{dt_start.strftime('%I:%M %p')} - {dt_end.strftime('%I:%M %p')}"
        return display_date, display_time


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
        all_day = 'date' in event['start']

        display_date, display_time = format_event_display(start, end, all_day)

        events.append({
            'title': event.get('summary', 'Untitled Event'),
            'start': start,
            'end': end,
            'all_day': all_day,
            'display_date': display_date,
            'display_time': display_time,
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
