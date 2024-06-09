def text_to_binary(text):
    """
    Convert a text string to binary representation.

    Args:
        text (str): The input text to convert.

    Returns:
        str: Binary representation of the input text.
    """
    return ''.join(format(ord(c), '08b') for c in text)


def binary_to_text(binary):
    """
    Convert a binary string to text representation.

    Args:
        binary (str): The input binary string.

    Returns:
        str: Text representation of the input binary string.
    """
    chars = [binary[i:i + 8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(b, 2)) for b in chars)


def count_ones(binary_string):
    """
    Count the number of ones in a binary string.

    Args:
        binary_string (str): The input binary string.

    Returns:
        int: The number of ones in the binary string.
    """
    return binary_string.count('1')


def encrypt(text):
    """
    Encrypt a text string using column and row transposition.

    Args:
        text (str): The input text to encrypt.

    Returns:
        tuple: A tuple containing the encrypted binary text, the key for decryption, and the number of columns for transposition.
    """
    binary_text = text_to_binary(text)
    num_ones = count_ones(binary_text)

    num_columns = len(text)

    transposed_text = transpose_columns(text, num_columns)

    transposed_text = transpose_rows(transposed_text, num_columns)

    shifted_text = ''.join(chr((ord(c) + num_ones) % 256) for c in transposed_text)

    encrypted_binary = text_to_binary(shifted_text)
    return encrypted_binary, num_ones, num_columns


def decrypt(encrypted_binary, key, num_columns):
    """
    Decrypt an encrypted binary string.

    Args:
        encrypted_binary (str): The encrypted binary string.
        key (int): The key for decryption.
        num_columns (int): The number of columns for transposition.

    Returns:
        str: The decrypted text string.
    """
    shifted_text = binary_to_text(encrypted_binary)

    transposed_text = ''.join(chr((ord(c) - key) % 256) for c in shifted_text)

    transposed_text = reverse_transpose_rows(transposed_text, num_columns)

    decrypted_text = reverse_transpose_columns(transposed_text, num_columns)

    return decrypted_text


def transpose_columns(text, num_columns):
    """
    Transpose the columns of a text string.

    Args:
        text (str): The input text to transpose.
        num_columns (int): The number of columns for transposition.

    Returns:
        str: The transposed text string.
    """
    padded_text = text.ljust((len(text) + num_columns - 1) // num_columns * num_columns)
    transposed = ''.join(
        padded_text[i::num_columns] for i in range(num_columns)
    )
    return transposed


def transpose_rows(text, num_columns):
    """
    Transpose the rows of a text string.

    Args:
        text (str): The input text to transpose.
        num_columns (int): The number of columns for transposition.

    Returns:
        str: The transposed text string.
    """
    num_rows = (len(text) + num_columns - 1) // num_columns
    padded_text = text.ljust(num_rows * num_columns)
    transposed = ''.join(
        padded_text[i * num_columns:(i + 1) * num_columns] for i in range(num_rows)
    )
    return transposed


def reverse_transpose_columns(text, num_columns):
    """
    Reverse the transposition of columns in a text string.

    Args:
        text (str): The input text with transposed columns.
        num_columns (int): The number of columns for transposition.

    Returns:
        str: The text string with columns in their original order.
    """
    num_rows = (len(text) + num_columns - 1) // num_columns
    transposed = [''] * num_rows
    for i, c in enumerate(text):
        transposed[i % num_rows] += c
    return ''.join(transposed)


def reverse_transpose_rows(text, num_columns):
    """
    Reverse the transposition of rows in a text string.

    Args:
        text (str): The input text with transposed rows.
        num_columns (int): The number of columns for transposition.

    Returns:
        str: The text string with rows in their original order.
    """
    num_rows = (len(text) + num_columns - 1) // num_columns
    transposed = [''] * num_columns
    for i, c in enumerate(text):
        transposed[i // num_columns] += c
    return ''.join(transposed)


def main():
    """
    Main function to handle user input and execute encryption/decryption.
    """
    while True:
        command = input("Enter a command (encrypt, decrypt, exit): ").strip().lower()

        if command == 'encrypt':
            text = input("Enter the text to encrypt: ")
            encrypted_binary, key, num_columns = encrypt(text)
            print("Encrypted text (binary):", encrypted_binary)
            print("Key for decryption:", key)
            print("Number of columns/rows for transposition:", num_columns)

        elif command == 'decrypt':
            encrypted_binary = input("Enter the encrypted binary text: ")
            key = int(input("Enter the key for decryption: "))
            num_columns = int(input("Enter the number of columns/rows for transposition: "))
            decrypted_text = decrypt(encrypted_binary, key, num_columns)
            print("Decrypted text:", decrypted_text)

        elif command == 'exit':
            print("Exiting...")
            break

        else:
            print("Invalid command. Please enter 'encrypt', 'decrypt', or 'exit'.")


if __name__ == "__main__":
    main()
