from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PIL import Image
import numpy as np
import os

def pad(data):
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len]) * pad_len

def encrypt_array(img_array, mode, key, iv=None):
    flat_data = img_array.tobytes()
    cipher = AES.new(key, mode, iv) if iv else AES.new(key, mode)
    encrypted_data = cipher.encrypt(pad(flat_data))
    encrypted_array = np.frombuffer(encrypted_data[:len(flat_data)], dtype=np.uint8)
    return encrypted_array.reshape(img_array.shape)

def encrypt_image(path="images/example.png", output_dir="images"):
    img = Image.open(path).convert("RGB")
    img_array = np.array(img)

    key = get_random_bytes(16)
    iv = get_random_bytes(16)

    modes = {
        "ECB": AES.MODE_ECB,
        "CBC": AES.MODE_CBC,
        "CFB": AES.MODE_CFB,
        "OFB": AES.MODE_OFB,
        "CTR": AES.MODE_CTR
    }

    for name, mode in modes.items():
        if mode == AES.MODE_ECB:
            encrypted = encrypt_array(img_array, mode, key)
        elif mode == AES.MODE_CTR:
            cipher = AES.new(key, mode)
            flat_data = img_array.tobytes()
            encrypted_data = cipher.encrypt(pad(flat_data))
            encrypted = np.frombuffer(encrypted_data[:len(flat_data)], dtype=np.uint8).reshape(img_array.shape)
        else:
            encrypted = encrypt_array(img_array, mode, key, iv)

        enc_img = Image.fromarray(encrypted)
        save_path = os.path.join(output_dir, f"encrypted_{name}.png")
        enc_img.save(save_path)
        print(f"Saved {save_path}")

if __name__ == "__main__":
    encrypt_image()
