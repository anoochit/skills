import sys
import urllib.parse
import json

def generate_chart_url(config_str):
    try:
        # Load the config from string to validate JSON
        config = json.loads(config_str)
        # Compact JSON for the URL
        compact_json = json.dumps(config, separators=(',', ':'))
        encoded_config = urllib.parse.quote(compact_json)
        return f"https://quickchart.io/chart?c={encoded_config}"
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON configuration provided: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 chart_gen.py '<json_config>'")
        sys.exit(1)
    
    # Combine all arguments into a single string for JSON parsing
    # This handles cases where spaces might split the JSON if not perfectly quoted
    config_input = " ".join(sys.argv[1:])
    
    url = generate_chart_url(config_input)
    print(url)
