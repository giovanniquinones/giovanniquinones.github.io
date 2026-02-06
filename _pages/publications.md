---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find my articles on <u><a href="https://scholar.google.com/citations?user=Un02rhgAAAAJ&hl=en">my Google Scholar profile</a>.</u>

<a href="https://scholar.google.com/citations?user=Un02rhgAAAAJ&hl=en">
  <img src="https://scholar.google.com/citations?user=Un02rhgAAAAJ&hl=en">
</a>

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
