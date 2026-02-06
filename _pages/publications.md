---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find my articles on <u><a href="https://scholar.google.com/citations?user=Un02rhgAAAAJ&hl=en">my Google Scholar profile</a>.</u>

<a href="https://scholar.google.com/citations?user=Un02rhgAAAAJ&hl=en">
  <img src="https://scholar.googleusercontent.com/citations?view_op=view_citation_stats&user=Un02rhgAAAAJ&hl=en">
alt="Google Scholar profile statistics showing citation metrics and graphs for the user. The page includes a bar chart displaying citations per year and numerical data summarizing total citations, h-index, and i10-index. The design is clean and professional with a focus on academic achievements."
</a>

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
