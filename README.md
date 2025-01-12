# Singapore Reddit Scraper

Simple Python package to scrape Reddit data on Singapore.

## Usage

1. Obtain a Reddit API key from [Reddit Developer Portal](https://www.reddit.com/prefs/apps/)
2. Create a `config.yaml` file with the following:

```yaml
client_id: YOUR_CLIENT_ID
client_secret: YOUR_CLIENT_SECRET
```

Replace `YOUR_CLIENT_ID` and `YOUR_CLIENT_SECRET` with your Reddit API provided credentials.

3. Setup a virtual environment and install the dependencies:

```bash
uv venv
uv pip install -r requirements.txt
```

4. Run the example script:

```bash
uv run example.py
```

5. The data will be saved to `submissions.csv` in the directory.
