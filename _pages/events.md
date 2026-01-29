---
layout: single
title: "Events"
permalink: /events/
---

Stay up to date with Aiken Camellia Society meetings, shows, and events.

## Upcoming Events

{% if site.data.events.events.size > 0 %}
| Date | Time | Event | Location |
|------|------|-------|----------|
{% for event in site.data.events.events %}| {{ event.start | date: "%B %d, %Y" }} | {{ event.start | date: "%I:%M %p" }} - {{ event.end | date: "%I:%M %p" }} | {{ event.title }} | {{ event.location }} |
{% endfor %}

*Last updated: {{ site.data.events.last_updated | date: "%B %d, %Y at %I:%M %p" }} UTC*
{% else %}
*No upcoming events in the next 30 days.*
{% endif %}

---

## 2025 - 2026 Program Schedule

The Aiken Camellia Society meets the second Thursday evening of each month, October through March, from 6:30 PM to 7:30 PM at St. Thaddeus Episcopal Church Stevenson-McClelland Parlor, 125 Pendleton St. SW, Aiken, South Carolina 29801.

| Date | Event |
|------|-------|
| October 9th, 2025 | Mark Crawford: 4 Season of Camellias |
| November 13th, 2025 | Ryan Trustee: Figs in the Garden |
| December 11th, 2025 | Gentry Massey-Williams: Camellias at Magnolia |
| January 8th 2026 | Peggy All |
| February 12th 2026 | Aiken Camellia Society Auction |
| March 12th 2026 | Forrest Latta: Camellias, an International Language |

---

## Calendar

<iframe src="https://calendar.google.com/calendar/embed?src=contact%40aikencamellias.org&ctz=America%2FNew_York" style="border: 0" width="100%" height="600" frameborder="0" scrolling="no"></iframe>

---

### Annual Events

| Event | Date | Location |
|-------|------|----------|
| The Aiken Camellia Show | *The Second Saturday in January* | *First Presbyterian Church* |
| Club Camellia Auction | *February's club meeting* | *St. Thaddeus Episcopal Church* |
| Lookaway Hall Camellia Exhibition | *The first or second Saturday in March, check the calendar for the exact date* | *Lookaway Hall* |

---

*For the most current information, please check back regularly.*

{% include social-footer.html %}
