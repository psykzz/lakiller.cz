{% extends "base.tpl" %}
{% block body %}
<div class='left'>
<p><b>Information about poll ID {{pollid}}:</b></p>
{{ poll.handle_polltype(pollid) }}
</div>
{% endblock body %}