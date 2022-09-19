# Dog Phone
A 1-button alarm system for Raspberry Pi and cell phone hat. Dog presses button -> SMSes sent to emergency contacts

# Purpose

A service dog can be trained to press a button to call for help when a person with a disability needs help but can’t get to the phone. If you know your service dog can call for help, you feel more confident and secure, especially if you can customise who gets contacted, when, in what order, and what information they receive.

The purpose of this software is to reliably, transparently and configurably do this.

# Hardware

Here's the hardware we already have:

- Raspberry Pi 4 Model B 4GB
- [Waveshare 4G HAT for Raspberry Pi (LTE Cat-4/4G/3G/2G/GNSS)](https://core-electronics.com.au/waveshare-4g-hat-for-raspberry-pi-lte-cat-4-4g-3g-2g-gnss.html) with Aldi Mobile Sim
- Big normally-open momentary switch that can be wired to a GPIO pin of the RPi
- Speaker with line in

# Feature Specification

## Minimum Requirements
- on button press:
  - play countdown.wav on speaker(opportunity for user to cancel)
  - send alert_message by SMSes to contacts in specified order after specified delays (announce each action on speaker); and
  - loop waiting.wav on speaker; while
  - listen for reply SMS from contacts, and on receiving message containing 
