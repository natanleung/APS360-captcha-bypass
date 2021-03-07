from captcha.image import ImageCaptcha
import random

# Initialization
generator = ImageCaptcha()
characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # Only numeric right now
frequency = {}
count = 2000 # Number of items in dataset, roughly, might be conflicts in generation
captcha_size = 5 # Size of captchas 

for character in characters:
    frequency.update({ character: 0 })

for i in range(count):

    captcha_elements = []

    # Uniform probability selection of each character in captcha
    for j in range(captcha_size):
        index = random.randint(0, len(characters) - 1)
        captcha_elements.append(characters[index])
        
        # Update frequency for dataset statistics
        old_frequency = frequency.get(characters[index])
        frequency.update({ characters[index]: old_frequency + 1 })
    
    # Create actual captcha image
    text = "".join(captcha_elements)
    generator.write(text, f"./dataset/{text}.png")

# Print out some dataset statistics
print("Generated dataset frequency statistics: ")
for character in characters:
    print(f"{character}: {frequency.get(character)}")
