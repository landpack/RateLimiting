import time
import redis
from flask import Flask
from flask import request
from flask import abort
from flask import render_template

r = redis.Redis()
app = Flask(__name__)


@app.errorhandler(429)
def rate_limit_exceeded(e):
    return render_template('error_429.html'), 429


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
            abort(429)
            
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
