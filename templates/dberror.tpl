{% extends "base.tpl" %}
{% block body %}
{% if message == True %}
<p>Connection to the database has been successfully re-established, you will be sent to your page in a few seconds.</p>
<meta http-equiv="refresh" content="6">
{% else %}
<p>Something went wrong with the database. Apologies for the trouble.</p>
<p>Error message: {{ message }} </p>
{% endif %}
{% endblock body %}