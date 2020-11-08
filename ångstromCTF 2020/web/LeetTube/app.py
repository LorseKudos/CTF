#!/usr/bin/env python
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import os

videos = []
for file in os.listdir('videos'):
    os.chmod('videos/'+file, 0o600)
    videos.append({'title': file.split(
        '.')[0], 'path': 'videos/'+file, 'content': open('videos/'+file, 'rb').read()})
published = []
for video in videos:
    if video['title'].startswith('UNPUBLISHED'):
        # make sure you can't just guess the filename
        os.chmod(video['path'], 0)
    else:
        published.append(video)


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/videos/'):
            self.path = self.path.replace('%20', ' ')
            try:
                video = open('videos/'+self.path[8:], 'rb', 0)
            except OSError:
                self.send_response(404)
                self.end_headers()
                return
            reqrange = self.headers.get('Range', 'bytes 0-')
            ranges = list(int(i) for i in reqrange[6:].split('-') if i)
            if len(ranges) == 1:
                ranges.append(ranges[0]+65536)
            try:
                video.seek(ranges[0])
                content = video.read(ranges[1]-ranges[0]+1)
            except:
                self.send_response(404)
                self.end_headers()
                return
            self.send_response(206)
            self.send_header('Accept-Ranges', 'bytes')
            self.send_header('Content-Type', 'video/mp4')
            self.send_header(
                'Content-Range', f'bytes {ranges[0]}-{ranges[0]+len(content)-1}/{os.path.getsize("videos/"+self.path[8:])}')
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(f"""
<style>
body {{
    background-color: black;
    color: #00e33d;
    font-family: monospace;
    max-width: 30em;
    font-size: 1.5em;
    margin: 2em auto;
}}
</style>
<h1>LeetTube</h1>
<p>There are <strong>{len(published)}</strong> published video{'s' if len(published) > 1 else ''} and <strong>{len(videos)-len(published)}</strong> unpublished video{'s' if len(videos)-len(published) > 1 else ''}.</p>
{''.join(f'<h2>{video["title"]}</h2><video controls src="{video["path"]}"></video>' for video in published)}
""".encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()


httpd = ThreadingHTTPServer(('', 8000), RequestHandler)
httpd.serve_forever()
