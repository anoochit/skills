import sys
import urllib.parse

def generate_qr_url(text, size=300):
    encoded_text = urllib.parse.quote(text)
    return f"https://quickchart.io/qr?text={encoded_text}&size={size}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 qr_gen.py '<text>' [size]")
        sys.exit(1)
    
    # Try to parse the last argument as size if it's an integer
    args = sys.argv[1:]
    size = 300
    text = ""
    
    if len(args) > 1 and args[-1].isdigit():
        size = int(args[-1])
        text = " ".join(args[:-1])
    else:
        text = " ".join(args)
        
    url = generate_qr_url(text, size)
    print(url)
