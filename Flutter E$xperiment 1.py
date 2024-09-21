def convert_to_words(num):
    if num == 0:
        return "zero"

    # Dictionaries to map number to words
    below_20 = ['','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 
                'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 
                'eighteen', 'nineteen']
    
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    thousands = ['', 'thousand', 'million']

    # Helper function to handle numbers below 1000
    def convert_chunk(n):
        if n == 0:
            return ""
        elif n < 20:
            return below_20[n]
        elif n < 100:
            return tens[n // 10] + (" " + below_20[n % 10] if n % 10 != 0 else "")
        else:
            return below_20[n // 100] + " hundred" + ((" " + convert_chunk(n % 100)) if n % 100 != 0 else "")
    
    # Main function logic
    result = []
    chunk_count = 0

    while num > 0:
        chunk = num % 1000
        if chunk > 0:
            result.append(convert_chunk(chunk) + (" " + thousands[chunk_count] if thousands[chunk_count] else ""))
        num //= 1000
        chunk_count += 1

    return ' '.join(result[::-1]).strip()

# Example usage
num = int(input("Enter a number between 1 and 999,999,999: "))
if 1 <= num <= 999999999:
    print(convert_to_words(num))
else:
    print("Number out of range!")