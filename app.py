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
    give_local = request.form['local']
    give_food = request.form['food']
    print(give_food)
    print(give_local)
    receive = list(db.realFood.find({'local' : give_local, 'food' : give_food}, {'_id': False}))
    return jsonify({'result': 'success', 'msg': 'POST 연결되었습니다!', 'receive': receive})

# 주문 목록보기(Read) API

@app.route('/pasta', methods=['GET'])
def get_pasta():
    foodList = list(db.foodList.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'msg': 'GET 연결되었습니다!', 'foodList': foodList})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)