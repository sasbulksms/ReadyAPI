# Links externos e Artigos

**ReadyApi** tem uma grande comunidade em crescimento constante.

Existem muitas postagens, artigos, ferramentas e projetos relacionados ao **ReadyApi**.

Aqui tem uma lista, incompleta, de algumas delas.

!!! tip "Dica"
    Se você tem um artigo, projeto, ferramenta ou qualquer coisa relacionada ao **ReadyApi** que ainda não está listada aqui, crie um <a href="https://github.com/khulnasoft/readyapi/edit/master/docs/external-links.md" class="external-link" target="_blank">_Pull Request_ adicionando ele</a>.

## Artigos

### Inglês

{% if external_links %}
{% for article in external_links.articles.english %}

* <a href="{{ article.link }}" class="external-link" target="_blank">{{ article.title }}</a> by <a href="{{ article.author_link }}" class="external-link" target="_blank">{{ article.author }}</a>.
{% endfor %}
{% endif %}

### Japonês

{% if external_links %}
{% for article in external_links.articles.japanese %}

* <a href="{{ article.link }}" class="external-link" target="_blank">{{ article.title }}</a> by <a href="{{ article.author_link }}" class="external-link" target="_blank">{{ article.author }}</a>.
{% endfor %}
{% endif %}

### Vietnamita

{% if external_links %}
{% for article in external_links.articles.vietnamese %}

* <a href="{{ article.link }}" class="external-link" target="_blank">{{ article.title }}</a> by <a href="{{ article.author_link }}" class="external-link" target="_blank">{{ article.author }}</a>.
{% endfor %}
{% endif %}

### Russo

{% if external_links %}
{% for article in external_links.articles.russian %}

* <a href="{{ article.link }}" class="external-link" target="_blank">{{ article.title }}</a> by <a href="{{ article.author_link }}" class="external-link" target="_blank">{{ article.author }}</a>.
{% endfor %}
{% endif %}

### Alemão

{% if external_links %}
{% for article in external_links.articles.german %}

* <a href="{{ article.link }}" class="external-link" target="_blank">{{ article.title }}</a> by <a href="{{ article.author_link }}" class="external-link" target="_blank">{{ article.author }}</a>.
{% endfor %}
{% endif %}

## Podcasts

{% if external_links %}
{% for article in external_links.podcasts.english %}

* <a href="{{ article.link }}" class="external-link" target="_blank">{{ article.title }}</a> by <a href="{{ article.author_link }}" class="external-link" target="_blank">{{ article.author }}</a>.
{% endfor %}
{% endif %}

## Palestras

{% if external_links %}
{% for article in external_links.talks.english %}

* <a href="{{ article.link }}" class="external-link" target="_blank">{{ article.title }}</a> by <a href="{{ article.author_link }}" class="external-link" target="_blank">{{ article.author }}</a>.
{% endfor %}
{% endif %}

## Projetos

Últimos projetos no GitHub com o tópico `readyapi`:

<div class="github-topic-projects">
</div>
