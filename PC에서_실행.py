import http.server, socketserver, webbrowser, pathlib, threading
ROOT=pathlib.Path(__file__).resolve().parent
PORT=8765
class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self,*args,**kwargs): super().__init__(*args,directory=str(ROOT),**kwargs)
threading.Timer(0.7,lambda:webbrowser.open(f'http://127.0.0.1:{PORT}/index.html')).start()
with socketserver.TCPServer(('127.0.0.1',PORT),Handler) as server:
    print('게임이 브라우저에서 열립니다. 종료: Ctrl+C')
    server.serve_forever()
