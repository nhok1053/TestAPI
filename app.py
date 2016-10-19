import jsonify as jsonify
import request as request
from builtins import print
from flask import *
import json
from mongoengine import *
from mlab import *


app = Flask(__name__)

class Post(Document):
   title = StringField()
   content = StringField()
   def get_json(self):
       return {"title": self.title, 'content': self.content}

post1 = {
    "title ": "Gooday",
    "content": " Today I met a girl. She had black eyes and love ice - creams"
}
post2 = {
    "title": "Bad day ever",
    "content ": "Baday ever ever ever "
}
print(post1["title "])
print(post2["title"])
posts = [post1, post2]



@app.route('/')
def main():
   posts = Post.objects
   return jsonify([post.get_json() for post in posts])

@app.route('/addpost',methods = ["POST"])
def add_post():
    args = request.form
    title = args["title"]
    content = args["content"]
    p = Post(title=title,content=content)
    p.save()
    return jsonify({"code": 1 , "message": "OK" })

if __name__ == '__main__':
    mlab_connect()
    app.run()
