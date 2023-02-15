def get_pins(observed):
    adjacent_digits = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['2', '1', '3', '5'],
        '3': ['3', '2', '6'],
        '4': ['4', '1', '5', '7'],
        '5': ['5', '2', '4', '6', '8'],
        '6': ['6', '3', '5', '9'],
        '7': ['7', '4', '8'],
        '8': ['8', '0', '5', '7', '9'],
        '9': ['9', '6', '8']
    }
    variations = ['']
    for digit in observed:
        new_variations = []
        for variation in variations:
            for adjacent_digit in adjacent_digits[digit]:
                new_variations.append(variation + adjacent_digit)
        variations = new_variations
    return variations
