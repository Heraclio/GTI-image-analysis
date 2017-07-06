from PIL import Image
import math

dictionary = {
  '.-'  :'A', '-...':'B', '-.-.':'C', '-..' :'D', '.'   :'E',
  '..-.':'F', '--.' :'G', '....':'H', '..'  :'I', '.---':'J',
  '-.-':'K', '.-..' : 'L', '--' :'M', '-.' :'N', '---':'O',
  '.--.' : 'P', '--.-' : 'Q', '.-.':'R', '...':'S', '-'  :'T',
  '..-':'U', '...-' : 'V', '.--':'W', '-..-' : 'X', '-.--' : 'Y',
  '--..' : 'Z', '.----' : '1', '..---' : '2', '...--' : '3', 
  '....-' : '4', '.....' : '5', '-....' : '6', '--...' : '7', 
  '---..' : '8','----.' : '9','-----' : '0',
  '-...-' : '=', '.-.-':'~', '.-...' :'<AS>', '.-.-.' : '<AR>', '...-.-' : '<SK>',
  '-.--.' : '<KN>', '..-.-' : '<INT>', '....--' : '<HM>', '...-.' : '<VE>',
  '.-..-.' : '\\', '.----.' : '\'', '...-..-' : '$', '-.--.' : '(', '-.--.-' : ')', 
  '--..--' : ',', '-....-' : '-', '.-.-.-' : '.', '-..-.' : '/', '---...' : ':', 
  '-.-.-.' : ';', '..--..' : '?', '..--.-' : '_', '.--.-.' : '@', '-.-.--' : '!'
}

def decode(morse):
    if(morse in dictionary):
        return dictionary[morse]
    else:
		return ' '

def main():
	with Image.open('image.png') as image:
	    pixels = list(image.getdata())
	    offsetFromLastWhitePixel = 0
	    morse = []
	    message = []
	    for pixel in pixels:
	      if(pixel > 0):
		      morse.append(str(unichr(offsetFromLastWhitePixel)))
		      offsetFromLastWhitePixel = 0
	      offsetFromLastWhitePixel += 1
	    morse = ''.join(morse)
	    for code in morse.split(' '):
	    	decoded = decode(code)
	    	message.append(decoded)
    	message = ''.join(message)
    	print(message)
main()