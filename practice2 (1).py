from flask import Flask
from flask import request

# shiv = Flask(__name__)

# @shiv.route("/test1")
# def test1():
#     return "<h1>shivaji is a good boy</h1>"

# @shiv.route(("/test2"))
# def test2():
#     return "<h1> mahabharatha is the greatest epic </h1>"

# @shiv.route("/test3")
# def test3():
#     a = 77 + 88 *55
#     return "<h1> ramayana is the story of warrior prince and his struggles and test of his morality</h1> <b>{}</b>".format(a)

# @shiv.route("/test4")
# def test4():
#     data = request.args.get("x")
#     return "<h1> the mahabharata contains great lesson called as bhagavadgita </h1> {}".format(data)

# if __name__ == "__main__":
#     shiv.run(host = "0.0.0.0")


nagaraj = Flask(__name__)

@nagaraj.route("/index1")
def index1():
    a = 770 + 99 * 7 - 1290 
    return "<h1> shankar is the good boy and has done some good work </h1> {}".format(a)

@nagaraj.route("/index2")
def index2():
    data = request.args.get("b")
    return  "<h2>this kalyug is very horryfiying to live in </h2> {}".format(data)

if __name__ == "__main__":
    nagaraj.run(host = "0.0.0.0")
