---
layout: single
title: "2026 Camellia Auction"
permalink: /auction/
---

#### Date & Time
Thursday, February 12th, 2026 at 6:30 PM
<hr />

#### Location
<a href="https://maps.app.goo.gl/oMqjJeNov4ZUdryA6"> 
St. Thaddeus Episcopal Church Stevenson-McClelland Parlor     
125 Pendleton St. SW  
Aiken, SC 29801</a>
<hr />

#### Lots
Browse our camellias for auction below!

{% for camellia in site.data.auction %}
<div class="auction-slide">
  <div class="auction-image">
    <img src="{{ '/assets/images/auction/' | append: camellia.id | append: '.jpg' | relative_url }}" alt="{{ camellia.name }}" onerror="this.onerror=null; this.src='{{ '/assets/images/auction/default.jpg' | relative_url }}';">
  </div>
  <div class="auction-details">
    <div class="auction-header">
      <h2 class="auction-name">Lot {{ forloop.index}}: {{ camellia.name }}</h2>
      {% if camellia.species and camellia.species != "" %}
      <span class="auction-species">{{ camellia.species }}</span>
      {% endif %}
    </div>
    
    <div class="auction-attributes">
      {% if camellia.color and camellia.color != "" %}
      <div class="auction-attr">
        <span class="attr-label">Color:</span>
        <span class="attr-value">{{ camellia.color }}</span>
      </div>
      {% endif %}
      
      {% if camellia.form and camellia.form != "" %}
      <div class="auction-attr">
        <span class="attr-label">Form:</span>
        <span class="attr-value">{{ camellia.form }}</span>
      </div>
      {% endif %}
      
      {% if camellia.size and camellia.size != "" %}
      <div class="auction-attr">
        <span class="attr-label">Size:</span>
        <span class="attr-value">{{ camellia.size }}</span>
      </div>
      {% endif %}
      
      {% if camellia.season and camellia.season != "" %}
      <div class="auction-attr">
        <span class="attr-label">Season:</span>
        <span class="attr-value">{{ camellia.season }}</span>
      </div>
      {% endif %}
      
      {% if camellia.rate and camellia.rate != "" %}
      <div class="auction-attr">
        <span class="attr-label">Growth Rate:</span>
        <span class="attr-value">{{ camellia.rate }}</span>
      </div>
      {% endif %}
      
      {% if camellia.characteristics and camellia.characteristics != "" %}
      <div class="auction-attr">
        <span class="attr-label">Characteristics:</span>
        <span class="attr-value">{{ camellia.characteristics }}</span>
      </div>
      {% endif %}
      
      {% if camellia.leaf and camellia.leaf != "" %}
      <div class="auction-attr">
        <span class="attr-label">Leaf:</span>
        <span class="attr-value">{{ camellia.leaf }}</span>
      </div>
      {% endif %}
    </div>
    
    <div class="auction-origin">
      {% if camellia.originator and camellia.originator != "" %}
      <div class="auction-attr">
        <span class="attr-label">Originator:</span>
        <span class="attr-value">{{ camellia.originator }}</span>
      </div>
      {% endif %}
      
      {% if camellia.place and camellia.place != "" %}
      <div class="auction-attr">
        <span class="attr-label">Place:</span>
        <span class="attr-value">{{ camellia.place }}</span>
      </div>
      {% endif %}
      
      {% if camellia.year and camellia.year != "" %}
      <div class="auction-attr">
        <span class="attr-label">Year:</span>
        <span class="attr-value">{{ camellia.year }}</span>
      </div>
      {% endif %}
    </div>
    
    {% if camellia.heritage and camellia.heritage != "" %}
    <div class="auction-heritage">
      <span class="attr-label">Heritage:</span>
      <span class="attr-value">{{ camellia.heritage }}</span>
    </div>
    {% endif %}
    
    {% if camellia.other and camellia.other != "" %}
    <div class="auction-other">
      <span class="attr-label">Notes:</span>
      <span class="attr-value">{{ camellia.other }}</span>
    </div>
    {% endif %}
  </div>
</div>
{% endfor %}

{% include social-footer.html %}
