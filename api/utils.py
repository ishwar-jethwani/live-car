import random
import string

def random_string_generator_event(size=10, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


def unique_drive_id_generator(instance):
	new_id= random_string_generator_event()

	Klass= instance.__class__

	qs_exists= Klass.objects.filter(traveling_id=new_id).exists()
	if qs_exists:
		return unique_drive_id_generator(instance)
	return new_id