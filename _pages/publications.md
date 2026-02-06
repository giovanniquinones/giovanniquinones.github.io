---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---


{% assign scholar = site.data.scholar %}
{% assign author = scholar.author | default: scholar.author_info %}
{% assign metrics = scholar.cited_by.table %}

<div class="scholar-profile">
  <h2>Google Scholar</h2>

  {% if author %}
    <div>
      <p><strong>{{ author.name | default: "Google Scholar Profile" }}</strong></p>
      {% if author.affiliation %}<p>{{ author.affiliation }}</p>{% endif %}
      {% if author.affiliations %}<p>{{ author.affiliations }}</p>{% endif %}
      {% if author.cited_by and author.cited_by.value %}<p>Cited by: {{ author.cited_by.value }}</p>{% endif %}
      {% if author.cited_by and author.cited_by.total %}<p>Cited by: {{ author.cited_by.total }}</p>{% endif %}
      {% if author.cited_by and author.cited_by %}{% unless author.cited_by.value or author.cited_by.total %}<p>Cited by: {{ author.cited_by }}</p>{% endunless %}{% endif %}

      {% if author.interests %}
        {% assign interests_list = "" %}
        {% for i in author.interests %}
          {% if i.title %}
            {% assign interests_list = interests_list | append: i.title %}
          {% else %}
            {% assign interests_list = interests_list | append: i %}
          {% endif %}
          {% unless forloop.last %}{% assign interests_list = interests_list | append: ", " %}{% endunless %}
        {% endfor %}
        {% if interests_list != "" %}<p>Interests: {{ interests_list }}</p>{% endif %}
      {% endif %}
    </div>

    {% if metrics and metrics.size >= 3 %}
      <div class="scholar-metrics">
        <h3>Citation metrics</h3>
        <div class="scholar-metrics__grid">
          <div class="scholar-metrics__item">
            <div class="scholar-metrics__label">Citations</div>
            <div class="scholar-metrics__value">{{ metrics[0].citations.all }}</div>
            <div class="scholar-metrics__since">Since 2021: {{ metrics[0].citations.since_2021 }}</div>
          </div>
          <div class="scholar-metrics__item">
            <div class="scholar-metrics__label">h-index</div>
            <div class="scholar-metrics__value">{{ metrics[1].h_index.all }}</div>
            <div class="scholar-metrics__since">Since 2021: {{ metrics[1].h_index.since_2021 }}</div>
          </div>
          <div class="scholar-metrics__item">
            <div class="scholar-metrics__label">i10-index</div>
            <div class="scholar-metrics__value">{{ metrics[2].i10_index.all }}</div>
            <div class="scholar-metrics__since">Since 2021: {{ metrics[2].i10_index.since_2021 }}</div>
          </div>
        </div>
      </div>
    {% endif %}
  {% else %}
    <p>Scholar profile data not available yet.</p>
  {% endif %}

  {% if scholar.articles %}
    <div class="scholar-publications">
      <h3>Google Scholar publications</h3>
      <ul class="scholar-publications__list">
        {% for p in scholar.articles %}
          <li class="scholar-publications__item">
            <div class="scholar-publications__title">
              <strong>
                {% if p.link %}
                  <a href="{{ p.link }}">{{ p.title }}</a>
                {% else %}
                  {{ p.title | default: "Untitled" }}
                {% endif %}
              </strong>
            </div>
            <div class="scholar-publications__meta">
              {% if p.authors %}<span>{{ p.authors }}</span>{% endif %}
              {% if p.year %}<span class="scholar-publications__year">({{ p.year }})</span>{% endif %}
            </div>
            {% if p.publication %}
              <div class="scholar-publications__journal">{{ p.publication }}</div>
            {% endif %}
            {% if p.cited_by and p.cited_by.value %}
              <div class="scholar-publications__cites">Cited by: {{ p.cited_by.value }}</div>
            {% endif %}
          </li>
        {% endfor %}
      </ul>
    </div>
  {% else %}
    <p>Scholar publications not available yet.</p>
  {% endif %}
</div>

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

