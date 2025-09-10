from generate_image import generate_test_image
from encrypt_image import encrypt_image

if __name__ == "__main__":
    # Step 1: generate test image
    generate_test_image()

    # Step 2: encrypt using different AES modes
    encrypt_image()
