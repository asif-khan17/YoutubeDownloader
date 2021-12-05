from flask import Blueprint , request, jsonify
from pytube import YouTube, Search

routes = Blueprint("routes", __name__, static_folder="static", template_folder="templates")

@routes.route('/download', methods=['POST'])
def download_video():
    try:
        url = request.form.get('url')
        format = request.form.get('format')
        yt = YouTube(url)
        if format == 'mp3':
            stream = yt.streams.filter(only_audio=True).first()
            return { "file_size" : stream.filesize , "title" : stream.title , "url": stream.url }
        else:
            stream = yt.streams.filter(file_extension=format).first()
            return { "file_size" : stream.filesize , "title" : stream.title , "url": stream.url }
    except Exception as e:
        raise e

@routes.route('/search', methods=['POST'])
def search_videos():
    try:
        key = request.form.get('key')
        s = Search(key)
        searchResults = []
        results = s.results
        searchResults = [ { "url": yt.watch_url, "title": yt.title , "thumbnail":f"https://img.youtube.com/vi/{yt.video_id}/maxresdefault.jpg" } for yt in results]
        return jsonify(searchResults)

    except Exception as e:
        raise e
