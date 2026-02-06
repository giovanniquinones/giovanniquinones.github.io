---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find my articles on <u><a href="https://scholar.google.com/citations?user=Un02rhgAAAAJ&hl=en">my Google Scholar profile</a>.</u>

<div class="scholar-profile">
  <h2>Google Scholar</h2>
  <div id="scholar-profile">Loading profile...</div>
  <div id="scholar-publications">Loading publications...</div>
</div>

<script>
  const scholarEndpoint = "https://serpapi.com/search.json?engine=google_scholar_author&author_id=Un02rhgAAAAJ&api_key=684876bd9aa453b096534062f770ec86a2f1ebfc708106d23334604a35b6d110";

  fetch(scholarEndpoint)
    .then((res) => res.json())
    .then((data) => {
      const author = data.author || data.author_info || {};
      const name = author.name || "Google Scholar Profile";
      const affiliation = author.affiliation || author.affiliations || "";
      const citedBy = author.cited_by?.value || author.cited_by || "";
      const interests = Array.isArray(author.interests)
        ? author.interests.map((i) => i.title || i).filter(Boolean)
        : [];

      const profileHtml = `
        <div>
          <p><strong>${name}</strong></p>
          ${affiliation ? `<p>${affiliation}</p>` : ""}
          ${citedBy ? `<p>Cited by: ${citedBy}</p>` : ""}
          ${interests.length ? `<p>Interests: ${interests.join(", ")}</p>` : ""}
        </div>
      `;
      document.getElementById("scholar-profile").innerHTML = profileHtml;

      const articles = Array.isArray(data.articles) ? data.articles : [];
      let pubsHtml = "<ul>";
      articles.slice(0, 10).forEach((p) => {
        const authors = Array.isArray(p.authors) ? p.authors.join(", ") : p.authors || "";
        const year = p.year ? ` (${p.year})` : "";
        const link = p.link ? `<a href=\"${p.link}\">${p.title}</a>` : p.title || "Untitled";
        pubsHtml += `<li><strong>${link}</strong><br>${authors}${year}</li>`;
      });
      pubsHtml += "</ul>";
      document.getElementById("scholar-publications").innerHTML = pubsHtml;
    })
    .catch(() => {
      document.getElementById("scholar-profile").innerHTML = "Unable to load profile.";
      document.getElementById("scholar-publications").innerHTML = "Unable to load publications.";
    });
</script>


{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
