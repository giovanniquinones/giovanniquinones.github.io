---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find my articles on <u><a href="https://scholar.google.com/citations?user=Un02rhgAAAAJ&hl=en">my Google Scholar profile</a>.</u>

{% assign scholar = site.data.scholar %}
{% assign author = scholar.author | default: scholar.author_info %}

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
  {% else %}
    <p>Scholar profile data not available yet.</p>
  {% endif %}

  {% if scholar.articles %}
    <ul>
      {% for p in scholar.articles limit:10 %}
        <li>
          <strong>
            {% if p.link %}
              <a href="{{ p.link }}">{{ p.title }}</a>
            {% else %}
              {{ p.title | default: "Untitled" }}
            {% endif %}
          </strong>
          <br>
          {% if p.authors %}
            {% if p.authors.size %}
              {{ p.authors | join: ", " }}
            {% else %}
              {{ p.authors }}
            {% endif %}
          {% endif %}
          {% if p.year %} ({{ p.year }}){% endif %}
        </li>
      {% endfor %}
    </ul>
  {% else %}
    <p>Scholar publications not available yet.</p>
  {% endif %}
</div>


{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
