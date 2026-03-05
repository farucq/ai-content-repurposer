
import requests

API_KEY = "AIzaS****************************"

def search_youtube_video(topic):
    try:
        # Improve query
        query = f"{topic} technology explained"

        url = "https://www.googleapis.com/youtube/v3/search"

        params = {
            "part": "snippet",
            "q": query,
            "key": API_KEY,
            "maxResults": 5,
            "type": "video",
            "order": "relevance",
            "relevanceLanguage": "en",
            "safeSearch": "strict"
        }

        response = requests.get(url, params=params)
        data = response.json()

        if "items" in data and len(data["items"]) > 0:
            video = data["items"][0]

            title = video["snippet"]["title"]
            video_id = video["id"]["videoId"]

            return {
                "title": title,
                "link": f"https://www.youtube.com/watch?v={video_id}"
            }

    except Exception as e:
        print("YouTube search error:", e)

    return {
        "title": f"Learn more about {topic}",
        "link": f"https://www.youtube.com/results?search_query={topic}"
    }
