import requests

def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)
        
        
save_html(r.content, 'google_com')

def open_html(path):
    with open(path, 'rb') as f:
        return f.read()
    
    
html = open_html('google_com')