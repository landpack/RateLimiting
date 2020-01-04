from flask import Flask
from flask import request
from flask import abort

import redis,time

r = redis.Redis()



app = Flask(__name__)



@app.route("/")
def index():
    """
    
    """
    api_key = request.args.get('key')
    #current minute number
    c_m_n = int(time.time() / 60 ) # minutes 
    print("c_m_n:", c_m_n)
    key = "{}-{}".format(api_key, c_m_n)
    if key:
        if int(r.get(key) or 0) < 20:
            # rate limit
            p = r.pipeline()
            p.incr(key)
            p.expire(key, 59)
            p.execute()
            return "OK"
        else:
            abort(429, 'Rate limit Exceeded')
            
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
