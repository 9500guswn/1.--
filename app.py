from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.project


## HTML 화면 보기
@app.route('/')
def my_project():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/receive', methods=['POST'])
def post_receive():
    # local_receive = request.form['local_give']
    # food_recevie = request.form['food_give']
    #
    # db.home_home.insert_one({
    #     'title': title,
    #     'desc': desc,
    #     'image': image,
    #     'c': c
    # })

    return jsonify({'result': 'success', 'msg': 'POST 연결되었습니다!'})


# 주문 목록보기(Read) API
@app.route('/receive', methods=['GET'])
def get_receive():
    receive = list(db.my_project.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'msg': 'GET 연결되었습니다!','receive':receive})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
