{% extends "base.tpl" %}
{% block body %}
<div class='left'>
<p><b>Information about poll ID {{pollid}}:</b></p>
{{ poll.handle_polltype(cursor, pollid) }}
</div>
{% endblock body %}