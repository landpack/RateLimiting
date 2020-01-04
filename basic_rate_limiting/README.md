# Basic Rate Limiting

It's inspire by [redislab](https://redislabs.com/redis-best-practices/basic-rate-limiting/)

# Prepare

Install some package here.

    pip install flask
    pip install redis

Run your redis server.


# Test me :)

Run it on your terminal.

    python simple_flask_app.py

Open your terminal or browser visit *http://localhost:5000?key=123*


Check your redis with keys.


    127.0.0.1:6379> keys 123*
    1) "123-26301954"
    2) "123-26301953"

Check the key, see if how much time are left on your key.

    127.0.0.1:6379> ttl "123-26301957"
    (integer) 47
