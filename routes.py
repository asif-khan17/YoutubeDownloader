from flask import Blueprint , request, stream_with_context
from pytube import YouTube, request as rq

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

