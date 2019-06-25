#!usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author: guoqianqian 
@file: server.py 
@time: 2017/07/03 
@desc: 
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/product/list")
def product_list():
    return render_template("productList.html")

@app.route("/user/list")
def user_list():
    return render_template("userList.html")

@app.route("/record/list")
def record_list():
    return render_template("recordList.html")

if __name__ == "__main__":
    app.run(debug=True)
    