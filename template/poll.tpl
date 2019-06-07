<form form action='/poll' method='get'>
Offset: <input value='{{offset}}' name='offset' type='text'/> <input value='Load' type='submit'/>
</form>
% import src.poll
{{! src.poll.get_valid_polls(cursor, offset)}}