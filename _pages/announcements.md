---
layout: single
title: "Announcements"
permalink: /announcements/
---

Stay informed about the latest news from the Aiken Camellia Society.

## Upcoming Events

{% if site.data.events.events.size > 0 %}
| Date | Time | Event | Location |
|------|------|-------|----------|
{% for event in site.data.events.events %}| {{ event.start | date: "%B %d, %Y" }} | {% if event.all_day %}See calendar{% else %}{{ event.start | date: "%I:%M %p" }} - {{ event.end | date: "%I:%M %p" }}{% endif %} | {{ event.title }} | {{ event.location }} |
{% endfor %}

*Last updated: {{ site.data.events.last_updated | date: "%B %d, %Y at %I:%M %p" }} UTC*
{% else %}
*No upcoming events in the next 30 days. Check the [full calendar](/calendar/) for more.*
{% endif %}

---

## 2025 - 2026 Regular Meetings

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

*Have an announcement to share? Contact us at [contact@aikencamellias.org](mailto:contact@aikencamellias.org).*

{% include social-footer.html %}
