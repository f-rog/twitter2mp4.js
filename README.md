# twitter2mp4.js
Web version of my repo twitter2mp4, using Python and Javascript.
## Setup

1) Clone the repository

```
$ git clone https://github.com/f-rog/twitter2mp4.js.git
```

2) Install the dependencies

```
$ cd twitter2mp4.js
$ pip install -r requirements.txt
```

3) Run the Bottle server (see [Usage](#usage) below for more detail)

```
$ python index.py
```
## Usage
Use it however you want!
- You can either use the HTML UI i included or simply use the Bottle server from your terminal
Example:

```
$ python
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> req = requests.get('http://localhost:8000/get-video/{id}'.format(id=<<<TWITTER VIDEO ID>>>))
>>> print(req.text)
{"success": "true", "result": "https://video.twimg.com/ext_tw_video/<<<EXAMPLE>>>"}
```
## Compatibility

Tested on Python 2.7 and Python 3.7 on Linux and Windows. Feel free to [open an issue] if you have bug reports or questions. If you want to collaborate, you're welcome.

[open an issue]: https://github.com/f-rog/twitter2mp4.js/issues/new
