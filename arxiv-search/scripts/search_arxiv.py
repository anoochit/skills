import urllib.request
import xml.etree.ElementTree as ET
import sys
import argparse

def search_arxiv(query, max_results=5):
    """
    Search academic research papers on arXiv.
    """
    base_url = "http://export.arxiv.org/api/query?"
    query_params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max_results
    }
    url = base_url + urllib.parse.urlencode(query_params)
    
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            
        # arXiv returns Atom XML
        root = ET.fromstring(data)
        
        # XML namespaces for Atom
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        
        entries = root.findall('atom:entry', ns)
        
        if not entries:
            print("No papers found for the given query.")
            return

        print(f"--- Top {len(entries)} arXiv papers for: '{query}' ---\n")
        
        for i, entry in enumerate(entries, 1):
            title = entry.find('atom:title', ns).text.strip()
            # Title might have newlines from LaTeX or formatting
            title = " ".join(title.split())
            
            # Use findall for multiple authors
            authors = [author.find('atom:name', ns).text for author in entry.findall('atom:author', ns)]
            author_str = ", ".join(authors)
            
            summary = entry.find('atom:summary', ns).text.strip()
            summary = " ".join(summary.split())
            
            published = entry.find('atom:published', ns).text
            # Primary link
            link = entry.find('atom:id', ns).text
            
            print(f"[{i}] {title}")
            print(f"Authors: {author_str}")
            print(f"Published: {published}")
            print(f"Link: {link}")
            print(f"Summary: {summary[:500]}..." if len(summary) > 500 else f"Summary: {summary}")
            print("-" * 40)
            
    except Exception as e:
        print(f"Error searching arXiv: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search academic papers on arXiv.")
    parser.add_argument("query", help="The search query.")
    parser.add_argument("--max_results", type=int, default=5, help="Maximum number of results to return.")
    
    args = parser.parse_args()
    search_arxiv(args.query, args.max_results)
