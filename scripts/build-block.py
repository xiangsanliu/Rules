import os
import re
import urllib.request

AWAVENUE_URL = "https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/Filters/AWAvenue-Ads-Rule-Clash.yaml"
PCDN_URL = "https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/discretion/pcdn.txt"

def download_content(url):
    print(f"Downloading: {url}")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        raise

def parse_awavenue(content):
    domains = set()
    in_payload = False
    for line in content.splitlines():
        line_str = line.strip()
        if not line_str:
            continue
        if line_str.startswith('payload:'):
            in_payload = True
            continue
        if in_payload:
            if line_str.startswith('-'):
                # Extract domain, strip '-' and single/double quotes
                domain = line_str.lstrip('-').strip().strip("'\"")
                if domain:
                    domains.add(domain)
    print(f"Parsed {len(domains)} rules from AWAvenue.")
    return domains

def parse_pcdn(content):
    domains = set()
    for line in content.splitlines():
        line_str = line.strip()
        if not line_str or line_str.startswith('#'):
            continue
        domain = line_str.split('#')[0].strip()
        if domain:
            domains.add(domain)
    print(f"Parsed {len(domains)} rules from PCDN.")
    return domains

def parse_local_block():
    domains = set()
    block_path = 'block.txt'
    if not os.path.exists(block_path):
        block_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'block.txt')
    
    if os.path.exists(block_path):
        print(f"Reading local block list from: {block_path}")
        with open(block_path, 'r', encoding='utf-8') as f:
            for line in f:
                line_str = line.strip()
                if not line_str or line_str.startswith('#'):
                    continue
                domain = line_str.split('#')[0].strip()
                if domain:
                    domains.add(domain)
        print(f"Parsed {len(domains)} rules from local block.txt.")
    else:
        print(f"Warning: Local block list not found at {block_path}")
    return domains

def main():
    merged_domains = set()
    
    # 1. Download and parse AWAvenue rules
    try:
        awavenue_content = download_content(AWAVENUE_URL)
        merged_domains.update(parse_awavenue(awavenue_content))
    except Exception as e:
        print(f"Skipping AWAvenue rules due to error: {e}")
        
    # 2. Download and parse PCDN rules
    try:
        pcdn_content = download_content(PCDN_URL)
        merged_domains.update(parse_pcdn(pcdn_content))
    except Exception as e:
        print(f"Skipping PCDN rules due to error: {e}")
        
    # 3. Read and parse local block.txt
    try:
        merged_domains.update(parse_local_block())
    except Exception as e:
        print(f"Skipping local block.txt rules due to error: {e}")
        
    print(f"Total merged unique rules: {len(merged_domains)}")
    
    # 4. Sort and write to block_merged.yaml
    sorted_domains = sorted(list(merged_domains))
    output_path = 'block_merged.yaml'
    print(f"Writing merged rules to: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("payload:\n")
        for domain in sorted_domains:
            f.write(f"  - '{domain}'\n")
            
    print("Done!")

if __name__ == '__main__':
    main()
