---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find my articles on my Google Scholar profile


<div id="scholar-widget"></div>

<script>
fetch("https://serpapi.com/search.json?engine=google_scholar_author&author_id=Un02rhgAAAAJ&api_key=684876bd9aa453b096534062f770ec86a2f1ebfc708106d23334604a35b6d110")
  .then(res => res.json())
  .then(data => {
    let html = "<ul>";
    data.articles.slice(0, 10).forEach(p => {
      html += `<li>
        <strong>${p.title}</strong><br>
        ${p.authors?.join(", ")} (${p.year})
      </li>`;
    });
    html += "</ul>";
    document.getElementById("scholar-widget").innerHTML = html;
  });
</script>

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
