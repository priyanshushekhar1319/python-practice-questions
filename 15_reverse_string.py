def reverse_loop(text):
    result = ""
    for ch in text:
        result = ch + result
    return result

def reverse_slice(text):
    return text[::-1]

text = input("Enter text: ")
print("Using loop:", reverse_loop(text))
print("Using slicing:", reverse_slice(text))
