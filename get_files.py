import subprocess
import requests
import os
import json
import sys


def run_katana(url, katana_path):
    """
    Runs the Katana tool on a given URL to extract related links.

    :param url: The URL to be scanned by Katana.
    :type url: str
    :param katana_path: The path to the Katana executable.
    :type katana_path: str
    :return: A list of URLs extracted by Katana.
    :rtype: list[str]
    :raises subprocess.CalledProcessError: If the Katana tool fails to run.
    """
    try:
        result = subprocess.run(
            [katana_path, "-u", url], capture_output=True, text=True, check=True
        )
        print("Katana Output:\n", result.stdout)
        return result.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return []


def download_html(url, output_dir="downloaded_html"):
    """
    Downloads the HTML content of a given URL and saves it to a specified directory.

    :param url: The URL to download.
    :type url: str
    :param output_dir: The directory where the downloaded HTML file will be stored.
                       Defaults to 'downloaded_html'.
    :type output_dir: str, optional
    :return: The filename of the downloaded HTML file, or None if the download fails.
    :rtype: str or None
    :raises requests.RequestException: If the download fails due to network issues.
    """
    os.makedirs(output_dir, exist_ok=True)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"Downloaded: {url} -> {filepath}")
        return filename
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")
        return None


def save_url_mapping(mapping, output_dir="downloaded_html"):
    """
    Saves a URL-to-filename mapping as a JSON file.

    :param mapping: A dictionary mapping filenames to URLs.
    :type mapping: dict
    :param output_dir: The directory where the JSON file will be saved.
                       Defaults to 'downloaded_html'.
    :type output_dir: str, optional
    """
    mapping_file = os.path.join(output_dir, "url_mapping.json")
    with open(mapping_file, "w", encoding="utf-8") as f:
        json.dump(mapping, f, ensure_ascii=False, indent=4)
    print(f"URL mapping saved to {mapping_file}")


def main():
    """
    Main function that orchestrates the Katana run, HTML downloads, and saving
    of the URL mapping. Expects the Katana path as a command-line argument.

    :raises SystemExit: If the Katana path is not provided as a command-line argument.
    """
    if len(sys.argv) < 2:
        print("Usage: python3 get_files.py <katana_path>")
        sys.exit(1)

    katana_path = sys.argv[1]
    urls = run_katana("nu-msr.github.io", katana_path)
    url_mapping = {}

    for url in urls:
        if url.startswith("http") and url.endswith("html"):
            filename = download_html(url)
            if filename:
                url_mapping[filename] = url

    save_url_mapping(url_mapping)


if __name__ == "__main__":
    main()
