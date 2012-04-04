# Script Based Conference Call That Calls Its Participants

This tiny script is based on an idea I had here:
https://twitter.com/#!/torrez/statuses/184683262298427392

* Copy the settings.example.py file to settings.py.
* Get a Twilio account and API credentials. (You can test in developer mode.)
* Run it with some phone numbers as arguments.

usage: conference.py [-h] N [N ...]

Where N is a full phone number:

./conference.py +14155551212 +12125551212 +12135551212 ...