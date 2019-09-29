# from flask import Flask,jsonify,abort,make_response,request
#
# app = Flask(__name__)
#
# tasks = [
#     {
#         'id':1,
#         'title':'Learning RestAPI',
#         'description':'Learning restful API using Python Flask framework',
#         'Done':False
#     },
#
#     {
#         'id':2,
#         'title':'Studying Clean Code',
#         'description':'Learning coding practices to produce clean, efficient and readable code',
#         'Done':False
#     },
#     {
#         'id': 3,
#         'title': 'Practicing coding',
#         'description': 'Solving problems on hackerrank website',
#         'Done': False
#     }
#
#
# ]
#
#
# @app.route('/todo/api/v1.0/tasks', methods=['GET'])
# def get_tasks():
#     return jsonify({'tasks_added':tasks})
#
#
# @app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
# def get_task_by_id(task_id):
#     task = [task for task in tasks if task['id'] == task_id]
#     if not task:
#         abort(404)
#     return jsonify({f'task with id {task_id}':task})
#
#
# @app.errorhandler(404)
# def not_found_404(error):
#     return make_response(jsonify({'error':'not found'}),404)
#
#
# @app.route('/todo/api/v1.0/tasks', methods=['POST'])
# def add_task():
#     if not request.json or not request.json['title']:
#         abort(404)
#     task = {
#         'id':tasks[-1]['id']+1,
#         'title':request.json['title'],
#         'description':request.json.get('description',""),
#         'done':False
#
#     }
#     tasks.append(task)
#     return jsonify({'task':task},201)
#
#
# if __name__ == '__main__':
#     app.run(debug = True)
#
