import subprocess
import requests
import os
import json


def run_katana(url):
    try:
        # Run Katana and get URLs from the output
        result = subprocess.run(
            ["/home/david/misc/katana_lib/katana", "-u", url],
            capture_output=True, text=True, check=True
        )
        print("Katana Output:\n", result.stdout)
        return result.stdout.splitlines()  # Extract lines as URLs
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return []


def download_html(url, output_dir="downloaded_html"):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    try:
        # Fetch the HTML content
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad responses

        # Extract the filename from the URL
        filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
        filepath = os.path.join(output_dir, filename)

        # Save the HTML content to a file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"Downloaded: {url} -> {filepath}")
        return filename  # Return the filename for mapping
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")
        return None


def save_url_mapping(mapping, output_dir="downloaded_html"):
    mapping_file = os.path.join(output_dir, "url_mapping.json")
    with open(mapping_file, "w", encoding="utf-8") as f:
        json.dump(mapping, f, ensure_ascii=False, indent=4)
    print(f"URL mapping saved to {mapping_file}")


def main():
    # Run Katana on the target URL
    urls = run_katana("nu-msr.github.io")
    url_mapping = {}

    # Download HTML for each URL found by Katana
    for url in urls:
        if url.startswith("http") and url.endswith('.html'):  # Basic validation of URLs
            filename = download_html(url)
            if filename:  # Check if the download was successful
                url_mapping[filename] = url  # Map filename to original URL

    # Save the mapping to a JSON file
    save_url_mapping(url_mapping)


if __name__ == "__main__":
    main()
