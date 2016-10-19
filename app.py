from builtins import print
from flask import Flask
import json
app = Flask(__name__)


post1 ={
    "title " : "Gooday",
    "content" :" Today I met a girl. She had black eyes and love ice - creams"
}
post2 ={
    "title" : "Bad day ever",
    "content " : "Baday ever ever ever "
}
print(post1["title "])
print(post2["title"])
posts =[post1,post2]
@app.route('/')
def hello_world():
    return json.dumps(posts)


if __name__ == '__main__':
    app.run()
