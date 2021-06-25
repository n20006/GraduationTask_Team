import os
import sys
import time

import requests

# YouTube API key
YT_API_KEY = "xxxxxxxxxxxxxxx"


# Get activeLiveChatId youtube url
def get_chat_id(yt_url):
    try:
        video_id = yt_url.replace("https://www.youtube.com/watch?v=", "")
        print("video_id : ", video_id)

        url = "https://www.googleapis.com/youtube/v3/videos"
        params = {"key": YT_API_KEY, "id": video_id, "part": "liveStreamingDetails"}
        data = requests.get(url, params=params).json()

        liveStreamingDetails = data["items"][0]["liveStreamingDetails"]
        if "activeLiveChatId" in liveStreamingDetails.keys():
            chat_id = liveStreamingDetails["activeLiveChatId"]
            print("get_chat_id done!")
        else:
            chat_id = None
            print("NOT live")

        return chat_id
    except:
        print("URL not found")
        sys.exit()


# Get chat data
def get_chat(chat_id, pageToken, log_file):
    url = "https://www.googleapis.com/youtube/v3/liveChat/messages"
    params = {
        "key": YT_API_KEY,
        "liveChatId": chat_id,
        "part": "id,snippet,authorDetails",
    }
    if type(pageToken) == str:
        params["pageToken"] = pageToken

    data = requests.get(url, params=params).json()

    try:
        for item in data["items"]:
            channelId = item["snippet"]["authorChannelId"]
            msg = item["snippet"]["displayMessage"]
            usr = item["authorDetails"]["displayName"]
            # supChat   = item['snippet']['superChatDetails']
            # supStic   = item['snippet']['superStickerDetails']
            log_text = "[by {}  https://www.youtube.com/channel/{}]\n  {}\n".format(
                usr, channelId, msg
            )
            os.makedirs("chat_log", exist_ok=True)
            with open(os.path.join("chat_log", log_file), "a") as f:
                f.write(log_text)
            print("{}: {}".format(usr, msg))
        f.close()

    except:
        pass

    return data["nextPageToken"]


# Set get and sleep times
# Write chat log in channelid.txt
def main(yt_url):
    slp_time = 10  # sec
    iter_times = 5  # times
    take_time = slp_time / 60 * iter_times
    chat_id = get_chat_id(yt_url)
    print("End in {} min".format(take_time))
    print("work on {}".format(yt_url))

    log_file = yt_url.replace("https://www.youtube.com/watch?v=", "") + ".txt"
    os.makedirs("chat_log", exist_ok=True)
    with open(os.path.join("chat_log", log_file), "a") as f:
        f.write("Record {}'s log\n".format(yt_url))
        f.close()

    nextPageToken = None
    for _ in range(iter_times):
        # for jj in [0]:
        try:
            print("\n")
            nextPageToken = get_chat(chat_id, nextPageToken, log_file)
            time.sleep(slp_time)
        except:
            break


if __name__ == "__main__":
    yt_url = input("Input YouTube URL > ")
    main(yt_url)
