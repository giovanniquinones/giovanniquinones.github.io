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
    <p>
      This section uses a Google Scholar widget. For the most up-to-date manuscript list, please see the <a href="{{ '/cv/' | relative_url }}">CV</a>.
    </p>

    {% assign graph = scholar.cited_by.graph %}
    {% if graph and graph.size > 0 %}
      {% assign graph_max = 1 %}
      {% for g in graph %}{% if g.citations > graph_max %}{% assign graph_max = g.citations %}{% endif %}{% endfor %}
      <figure class="scholar-chart">
        <figcaption class="scholar-chart__title">Citations per year</figcaption>
        <ol class="scholar-chart__bars" role="list">
          {% for g in graph %}
            {% assign pct = g.citations | times: 100.0 | divided_by: graph_max %}
            <li class="scholar-chart__col">
              <span class="scholar-chart__track">
                <span class="scholar-chart__bar" style="height: {{ pct }}%">
                  <span class="scholar-chart__value">{{ g.citations }}</span>
                </span>
              </span>
              <span class="scholar-chart__year">{{ g.year }}</span>
            </li>
          {% endfor %}
        </ol>
      </figure>
    {% endif %}

    {% if metrics and metrics.size >= 3 %}
      <div class="scholar-metrics">
        <h3>Citation metrics</h3>
        <div class="scholar-metrics__grid">
          <div class="scholar-metrics__item">
            <div class="scholar-metrics__label">Citations</div>
            <div class="scholar-metrics__value">{{ metrics[0].citations.all }}</div>
            {% for kv in metrics[0].citations %}{% if kv[0] != "all" %}<div class="scholar-metrics__since">Since {{ kv[0] | remove: "since_" }}: {{ kv[1] }}</div>{% endif %}{% endfor %}
          </div>
          <div class="scholar-metrics__item">
            <div class="scholar-metrics__label">h-index</div>
            <div class="scholar-metrics__value">{{ metrics[1].h_index.all }}</div>
            {% for kv in metrics[1].h_index %}{% if kv[0] != "all" %}<div class="scholar-metrics__since">Since {{ kv[0] | remove: "since_" }}: {{ kv[1] }}</div>{% endif %}{% endfor %}
          </div>
          <div class="scholar-metrics__item">
            <div class="scholar-metrics__label">i10-index</div>
            <div class="scholar-metrics__value">{{ metrics[2].i10_index.all }}</div>
            {% for kv in metrics[2].i10_index %}{% if kv[0] != "all" %}<div class="scholar-metrics__since">Since {{ kv[0] | remove: "since_" }}: {{ kv[1] }}</div>{% endif %}{% endfor %}
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

