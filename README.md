import requests

def process(url):
    return {
        "title": "Sample Video",
        "caption": "Sample caption from the platform.",
        "videos": [
            {"quality": "SD", "url": "https://example.com/sd.mp4"},
            {"quality": "HD", "url": "https://example.com/hd.mp4"}
        ]
    }
