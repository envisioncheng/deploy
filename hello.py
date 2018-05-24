from flask import Flask

app=Flask(__name__)

@app.route('/')
def method_name():
   return 'hello word!'


if  __name__=="__main()__":
    app.run()