from PIL import Image, ImageDraw

def generate_test_image(path="images/example.png"):
    img = Image.new("RGB", (256, 256), "white")
    draw = ImageDraw.Draw(img)

    # Draw some simple shapes
    draw.rectangle([50, 50, 200, 200], fill="black")
    draw.ellipse([80, 80, 170, 170], fill="red")
    draw.line([0, 0, 256, 256], fill="blue", width=5)

    img.save(path)
    print(f"Test image saved at {path}")

if __name__ == "__main__":
    generate_test_image()
