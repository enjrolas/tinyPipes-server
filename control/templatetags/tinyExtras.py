from django import template
import phonenumbers

register = template.Library()

#prettily formats a phone number that was in e164 format (or any format, but e164 is mostly what we're dealing with                                              
@register.filter
def formatNumber(value):
	try:
		return phonenumbers.format_number(phonenumbers.parse(value, None), phonenumbers.PhoneNumberFormat.INTERNATIONAL)
	except:  #in the event that there is no country code, phonenumbers freaks out.  Just return the 
		#unformatted number
		return value

#returns the national number(without the country code) for a phone number
@register.filter
def nationalNumber(value):
	try:
		return phonenumbers.parse(value, None).national_number
	except:  #in the event that there is no country code, phonenumbers can't parse the input.  
		#Just return the unformatted number
		return value




