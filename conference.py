#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from twilio.rest import TwilioRestClient
import settings 


client = TwilioRestClient(settings.API_KEY, settings.API_TOK)

parser = argparse.ArgumentParser(description='Call some people for a conference. Be sure you’ve set up your Twilio dealio.')
parser.add_argument('numbers', metavar='N', type=str, nargs='+',
                   help='Phone numbers to call into a conference.')

args = parser.parse_args()
numbers = vars(args)['numbers']

for number in numbers:
	call = client.calls.create(to=number,  
	                           from_=settings.FROM_NUMBER,
	                           url=settings.CONFERENCE_URL)	
