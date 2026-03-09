import urllib.request

def main():
    url = "https://blog.redlinesoft.net/llm.txt"
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                content = response.read().decode('utf-8')
                print(content)
            else:
                print(f"Error: Received status code {response.status}", file=sys.stderr)
    except Exception as e:
        import sys
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
