from bottle import route, run, template, response
import requests
import re
import json

class getVideo():
        def __init__(self,video_id):
                self.log = {}
                sources = {
                        "video_url" : "https://twitter.com/i/videos/tweet/"+video_id,
                        "activation_ep" :'https://api.twitter.com/1.1/guest/activate.json',
                        "api_ep" : "https://api.twitter.com/1.1/statuses/show.json?id="+video_id
                }
                headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0','accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}               
                self.session = requests.Session()
                def send_request(self, url,method,headers):
                        request = self.session.get(url, headers=headers) if method == "GET" else self.session.post(url, headers=headers)
                        if request.status_code == 200:
                                return request.text
                        else:
                                sys.exit("Bad request to {}, status code: {}.\nPlease sumbit an issue in the repo including this info.".format(url,request.status_code))
                # get guest token
                token_request = send_request(self,sources["video_url"],"GET",headers)
                bearer_file = re.findall('src="(.*js)',token_request)
                file_content = send_request(self,str(bearer_file[0]),'GET',headers)
                bearer_token_pattern = re.compile('Bearer ([a-zA-Z0-9%-])+')
                bearer_token = bearer_token_pattern.search(file_content)
                headers['authorization'] = bearer_token.group(0)
                self.log['bearer'] = bearer_token.group(0)
                req2 = send_request(self,sources['activation_ep'],'post',headers)
                headers['x-guest-token'] = json.loads(req2)['guest_token']
                self.log['guest_token'] = json.loads(req2)['guest_token']
                # get link
                self.log['full_headers'] = headers
                api_request = send_request(self,sources["api_ep"],"GET",headers)
                try:
                        videos = json.loads(api_request)['extended_entities']['media'][0]['video_info']['variants']
                        self.log['vid_list'] = videos
                        bitrate = 0
                        for vid in videos:
                                if vid['content_type'] == 'video/mp4':
                                                if vid['bitrate'] > bitrate:
                                                        bitrate = vid['bitrate']
                                                        hq_video_url = vid['url']
                        self.url = hq_video_url
                except:
                        self.url = 'no videos were found.'

@route('/get-video/<id>')
def index(id):
    response.set_header('Access-Control-Allow-Origin', '*')
    result = {'success' : '','result':''}
    if re.match(r'\d{18,20}',id):
        result['result'] = getVideo(id).url
        result['success'] = 'true' if 'http' in result['result'] else 'false'
        return json.dumps(result)
    else:
        response.status = 400
        return '400 Bad Request'

run(host='localhost', port=8000)
