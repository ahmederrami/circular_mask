from PIL import Image, ImageDraw

def create_circular_mask(image_size, circle_diameter, output_filename):
    """
    Creates a circular mask with a transparent background.
    
    :param image_size: Tuple (width, height) of the image
    :param circle_diameter: Diameter of the circular mask
    :param output_filename: Filename to save the output mask
    """
    # Create a new transparent image (RGBA mode) with the specified size
    img = Image.new("RGBA", image_size, (0, 0, 0, 0))  # Fully transparent

    # Create a drawing context
    draw = ImageDraw.Draw(img)

    # Calculate the coordinates for the circle to be centered
    left = (image_size[0] - circle_diameter) / 2
    top = (image_size[1] - circle_diameter) / 2
    right = (image_size[0] + circle_diameter) / 2
    bottom = (image_size[1] + circle_diameter) / 2

    # Draw a white circle (visible part of the mask) on the transparent background
    draw.ellipse((left, top, right, bottom), fill=(255, 255, 255, 255))  # White circle

    # Save the image
    img.save(output_filename, "PNG")
    print(f"Circular mask saved as {output_filename}")

# Example usage
create_circular_mask(image_size=(1920, 1080), circle_diameter=200, output_filename="circular_mask.png")
