import base64 
image = open('Desktop\jay.jpg', 'rb') #open binary file in read mode
image_read = image.read()
image_64_encode = base64.encodestring(image_read)
    
import requests # you have to install this library, with pip for example

paramas = {
  'filename': 'japanhh.jpg',
  'image': image_64_encode
}


response = requests.post('http://skylinelabs.in/alerto/image.php', data=paramas)

print response

# here is the response

