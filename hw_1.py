from flask import Flask


#==============================
#Wrong way to create server.

#from flask import Flask

# app = Flask(__name__)
#
# @app.route("")
# def home():
#     return 'Hello, World!'
#
#
# if __name__ == '__main__':
#     app.run()

#===============================

#Right way

#from flask import Flask

# app = Flask(__name__)
#
# @app.route("/") #Problem was - empty path. If its empty so there is no GET /.
# def home():
#     return 'Hello, World!'
#
#
# if __name__ == '__main__':
#     app.run()

#===============================
#
# app = Flask(__name__)
#
# @app.route("/")
# def hallo():
#     return "Hello from Flask"
#
# if __name__ == "__main__":
#     app.run(debug=True)

#===============================

# app = Flask(__name__)
#
# @app.route("/")
# def hallo():
#     return "Hallo from home!"
#
# @app.route("/user/<name>")
# def hallo_user(name):
#     return f"{name} - Hello from Flask"
#
# if __name__ == "__main__":
#     app.run(debug=True)






