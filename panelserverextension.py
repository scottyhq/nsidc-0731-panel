from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the notebook panel app with bokeh server"""
    Popen(["panel", "serve", "measures-panel.ipynb", "--allow-websocket-origin=*"])
