from builtins import print
from flask import Flask, request
import json

app = Flask(__name__)

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
def hello_world():
    return json.dumps(posts)


@app.route('/addpost',methods = ["POST"])
def add_post():
    args = request.form
    title = args["title"]
    content = args["content"]
    new_post = {"title":title,"content":content}
    print(title,content)
    posts.append(new_post)
    return "OK"
if __name__ == '__main__':
    app.run()
