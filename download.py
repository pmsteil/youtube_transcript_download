import os
import json
import youtube_transcript_downloader


def get_transcript(url, cache=True):
    """Get the transcript of a youtube video as a dictionary of key/value pairs"""
    cache_folder = "__cache__"
    if cache:
        if not os.path.exists(cache_folder):
            os.makedirs(cache_folder)

    if cache:
        transcript = get_json_transcript_from_cache(url, cache_folder)
    else:
        transcript = get_json_transcript(url)

    if not transcript:
        raise ValueError("Transcript is empty")

    return transcript


def get_json_transcript_from_cache(url, cache_folder, format_as_json=True):
    vid = url.split("v=")[1]
    try:
        if format_as_json:
            with open(f"{cache_folder}/{vid}.json", "r") as f:
                transcript = json.loads(f.read())
        else:
            with open(f"{cache_folder}/{vid}.json", "r") as f:
                transcript = get_text_only(json.loads(f.read()))
    except:
        print("Transcript not found in cache, downloading... error: {e}")
        transcript = get_json_transcript(url)
        if format_as_json:
            with open(f"{cache_folder}/{vid}.json", "w") as f:
                # save the transcript to the cache
                f.write(json.dumps(transcript))
        else:
            with open(f"{cache_folder}/{vid}.json", "w") as f:
                # save the transcript to the cache
                f.write(json.dumps(transcript))

    return transcript

def get_text_only(transcript):
    """Convert the transcript of a youtube video as a plain text string"""
    text = ""
    for value in transcript.values():
        text += value + " "
    return text


def get_json_transcript( url ):
    transcript = youtube_transcript_downloader.get_transcript(url)
    # convert the key, value pairs to a list of dictionaries
    return transcript




def save_transcript(transcript, filename, format_as_json=True):
    """Save the transcript to a file"""
    if transcript is None:
        raise ValueError("Error, no transcript to save")

    with open(filename, "w") as f:
        if format_as_json:
            f.write(json.dumps(transcript))
        else:
            f.write(transcript)




# handle calling from the command line
if __name__ == "__main__":
    # use the parse arg module to handle command line arguments
    import argparse
    parser = argparse.ArgumentParser(description="Download the transcript of a youtube video")
    parser.add_argument("url", help="The url of the youtube video")
    # add optional filename to save the transcript to
    parser.add_argument("-o", "--output_file", help="The filename to save the transcript to")

    # add optional argument to get the transcript as json with key/value or plain text
    # action="store_true" means that if the argument is passed in, it will be set to True else False
    parser.add_argument("-t", "--text", help="Get the transcript as plain text (defaults to JSON)", action="store_true")

    # add optional argument to not use cache
    parser.add_argument("-nc", "--no_cache", help="Don't use the cache", action="store_true")

    args = parser.parse_args()

    # get the arguments passed in...
    url = args.url
    output_file = args.output_file
    format_as_json = False if args.text else True

    if format_as_json:
        transcript = get_transcript(url, not args.no_cache)
    else:
        # do the download and convert to raw text
        transcript = get_text_only( get_transcript(url, not args.no_cache ) )


    if output_file:
        save_transcript(transcript, output_file, format_as_json)
        print(f"Transcript saved to {output_file}")
    else:
        print(transcript)
