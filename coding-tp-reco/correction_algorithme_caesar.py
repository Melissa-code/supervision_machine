"""Caesar algorithm

Copyright (c) 2021 Thierry P.G. DECKER
All Rights Reserved.
Released under the MIT license

"""


def encode_caesar_v0(text, offset):
    """Caesar encoding

    Args:
        text (str): The string to encode
        offset (int): The offset ey apply
    Returns:
        The cyphered string
    """
    #
    # Display the initial string and
    # wait for user input to continue
    #
    print("Initial string", text)
    input("Pause, press a key to continue...")
    #
    # Create an empty list
    #
    cypher = []
    #
    # Add each character of the text to the list
    #
    for car in text:
        cypher.append(car)
    print('Step 1:', cypher)
    input("Pause, press a key to continue...")
    #
    # Iterate other the elements of the list and
    # replace it with it's code : ord() builtin function
    #
    for index, car in enumerate(cypher):
        cypher[index] = ord(cypher[index])
    print('Step 2:', cypher)
    input("Pause, press a key to continue...")
    #
    # Iterate other the elements of the list and
    # replace it with it's code + the offset
    # and taking it's modulus
    #
    # Note that the unicode codes are between 0 and 1.114.111
    # meaning 1.114.112 character code, thus the modulus we use
    #
    for index, car in enumerate(cypher):
        cypher[index] = (cypher[index] + offset) % 1114112
    print('Step 3:', cypher)
    input("Pause, press a key to continue...")
    #
    # Iterate other the elements of the list and
    # replace it with the corresponding unicode character : chr() builtin
    # function
    #
    for index, car in enumerate(cypher):
        cypher[index] = chr(cypher[index])
    print('Step 4:', cypher)
    input("Pause, press a key to continue...")
    #
    # Convert the list into a string
    #
    cypher = "".join(cypher)
    print('Step 5:', cypher)
    input("Pause, press a key to continue...")
    #
    # Return the cyphered string
    #
    return cypher


def encode_caesar_v1(text, offset):
    """Caesar encoding

    Args:
        text (str): The string to encode
        offset (int): The offset ey apply
    Returns:
        The cyphered string
    """
    cypher = []
    for car in text:
        cypher.append(car)
    for index, car in enumerate(cypher):
        cypher[index] = ord(cypher[index])
        cypher[index] = (cypher[index] + offset) % 1114112
        cypher[index] = chr(cypher[index])
    cypher = "".join(cypher)
    return cypher


def encode_caesar_v2(text, offset):
    """Caesar encoding

    Args:
        text (str): The string to encode
        offset (int): The offset ey apply
    Returns:
        The cyphered string
    """
    cypher = []
    for car in text:
        cypher.append(car)
    for index, car in enumerate(cypher):
        cypher[index] = chr((ord(cypher[index]) + offset) % 1114112)
    cypher = "".join(cypher)
    return cypher


def encode_caesar_vfinal(text, offset):
    """Caesar encoding

    Args:
        text (str): The string to encode
        offset (int): The offset ey apply
    Returns:
        The cyphered string
    """
    return "".join([chr((ord(car) + offset) % 1114112) for car in text])


def main():
    """The main function
    """
    while True:
        text = input('Enter the text to encode or e(X)it: ')
        if text.upper() == 'X':
            break
        while True:
            offset = input('Enter the offset or e(X)it: ')
            if offset.upper() == 'X':
                break
            if not offset.isdigit():
                print('Invalid offset !')
                continue
            else:
                cypher = encode_caesar_v0(text=text, offset=int(offset))
                print(f'Cypher: {cypher}')


if __name__ == '__main__':
    main()
