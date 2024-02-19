import tkinter as tk

def decrypt_caesar(ciphertext, shift):
    """Decrypts a Caesar cipher encrypted text."""
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr(((ord(char) - ascii_offset - shift) % 26) + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

def decrypt_text():
    """Decrypts the ciphertext and displays the plaintext."""
    ciphertext = entry_cipher.get()
    shift = int(entry_shift.get())
    plaintext = decrypt_caesar(ciphertext, shift)
    output_label.config(text="Decrypted text: " + plaintext)

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher Decryptor")

# Create labels
label_cipher = tk.Label(root, text="Enter ciphertext:")
label_cipher.pack()

label_shift = tk.Label(root, text="Enter shift value:")
label_shift.pack()

output_label = tk.Label(root, text="")
output_label.pack()

# Create entry widgets
entry_cipher = tk.Entry(root, width=50)
entry_cipher.pack()

entry_shift = tk.Entry(root)
entry_shift.pack()

# Create decrypt button
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.pack()

# Start the GUI event loop
root.mainloop()
