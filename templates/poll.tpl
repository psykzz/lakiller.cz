{% extends "base.tpl" %}
{% block body %}
<form form action='/poll' method='get'>
Offset: <input value='{{offset}}' name='offset' type='text'/> <input value='Load' type='submit'/>
</form>
{{ poll.get_valid_polls(cursor, offset) }}
{% endblock body %}