{% extends "base.tpl" %}
{% block body %}
<h2>Error {{ error.code }}</h2>
<p>{{ error.description }}</p>
{% endblock body %}