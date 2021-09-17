from flask import Flask, request, jsonify
from  maio import get_room
app = Flask(__name__)
# app.debug = True


@app.route('/')
def index():
    return '1'



@app.route('/get/AutoInfoList', methods=['POST'])
def get_auto_info():
    if not request.form:
        return jsonify(code=False, msg='没参数，请求给锤子')
    roomid = request.form['name']
    data = get_room(roomid)
    return jsonify(code=True,data=data)



if __name__ == '__main__':
    app.run(debug=True)
