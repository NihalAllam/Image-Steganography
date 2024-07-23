from PIL import Image

image_path = "E:\Internship\msd.jpg"

# Open the image
image = Image.open(image_path, 'r')
newimage = image.copy()

if image is None:
    print("Image not found. Check the file path and make sure the image exists.")
    exit()

# Get the dimensions of the image
width, height = image.size

# Prompt the user to input the secret message
msg = input("Enter secret message: ") # For example, Enter "Thala for a reason"

# Prompt the user to input the password
password = input("Enter a passcode: ") # For example, Enter 7

# Convert the length of the message to a string and prepend it to the message
msg = str(len(msg)).zfill(3) + msg

# Initialize dictionaries for mapping characters to their ASCII values and vice versa
d = {}
c = {}

# Fill the dictionaries with ASCII values (0-255)
for i in range(256):
    d[chr(i)] = i  # Character to ASCII
    c[i] = chr(i)  # ASCII to character

k = 0
for i in range(height-1, -1, -1):
    for j in range(width-1, -1, -1):
        if k < len(msg):
            # Get the current pixel value
            r, g, b = image.getpixel((j, i))
            # Encode the character into the red channel of the pixel
            new_b = (b + int(password) + d[msg[k]]) % 256
            # Update the pixel value in the new image
            newimage.putpixel((j, i), (r, g, new_b))
            k += 1
        else:
            break
    if k >= len(msg):
        break

# Save the modified image to a new file
new_image_name = "E:\\Internship\\thala.png"
newimage.save(new_image_name, str(new_image_name.split(".")[1].upper()))

print("Image created.")
