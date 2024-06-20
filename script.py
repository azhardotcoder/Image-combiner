from PIL import Image

def combine_images_vertically(image1_path, image2_path, output_path):
    # Open the images
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Check if the widths are the same, otherwise resize
    if image1.width != image2.width:
        raise ValueError("The widths of the images must be the same.")

    # Create a new image with the combined height
    combined_height = image1.height + image2.height
    combined_image = Image.new('RGB', (image1.width, combined_height))

    # Paste the images into the combined image
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, image1.height))

    # Save the combined image
    combined_image.save(output_path)

# Combine img1.jpg and img2.jpg in the same folder
combine_images_vertically('img1.png', 'img2.png', 'combined_image.png')
