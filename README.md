# youtube_transcript_download


## Setup

```bash
conda create -n youtube_transcript_download python=3.9
conda activate youtube_transcript_download
pip install -r requirements.txt
```


## Usage

usage: download.py [-h] [-o OUTPUT_FILE] [-t] [-nc] url

Download the transcript of a youtube video

positional arguments:
  url                   The url of the youtube video

```
    optional arguments:
    -h, --help            show this help message and exit
    -o OUTPUT_FILE, --output_file OUTPUT_FILE
                            The filename to save the transcript to
    -t, --text            Get the transcript as plain text (defaults to JSON)
    -nc, --no_cache       Don't use the cache
```

Examples:
```
    python download.py https://www.youtube.com/watch?v=WEP5ubPMGDU --output_file transcript.json
    python download.py https://www.youtube.com/watch?v=WEP5ubPMGDU --output_file transcript.txt --text
```
