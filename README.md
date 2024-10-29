# NU MSR Website Search Engine

This repository contains two main components:

1. HTML Scraper: A program that scrapes all HTML files from [nu-msr.github.io](https://nu-msr.github.io/) and downloads them as lookup files for further use.

2. Web Server with Search Functionality: A local web server that allows users to search through the downloaded HTML pages and redirects them to the corresponding links on the original nu.msr.github.io site where the search term is found.

Additionally, the interface includes a checkbox (enabled by default) to filter out results related to ROS1.

## Demo

Here is a demo of the search features

<video src="https://github.com/user-attachments/assets/61b24ad3-68f4-4503-975a-c7feb5c4b626" controls="controls" style="max-width: 100%; height: auto;">
    Your browser does not support the video tag.
</video>

## Self-Hosting Instructions

Follow these steps to self-host the NU MSR search engine:

### 1. Clone the Repository  
Clone the repository from your preferred source or download the code.

```
git clone https://github.com/KhachDavid/nu-msr-search-engine.git
```

### 2. Set up a Virtual Environment  
To manage dependencies, create and activate a virtual environment.

```bash
python3 -m venv venv

source venv/bin/activate  # On macOS/Linux
# For Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Start the Server
```
python3 serve_files.py
```

This runs on your 8000 port.

Now you can access http://localhost:8000/

## Updating Lookup HTML files

1. **Install Katana**  
   Follow the installation instructions from the [Katana GitHub repository](https://github.com/projectdiscovery/katana?tab=readme-ov-file).  
   Ensure you have the path to the Katana binary available (e.g., `/home/<your_username>/katana_lib/katana`).

2. **Set up Virtual Environment (if not already done)**  

   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run `get_files.py`

    ```bash
    python3 get_files.py /path/to/katana
    ```
