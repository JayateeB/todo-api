from todo_app import app,db
from flask import jsonify,abort,make_response,request
from todo_app.models import Tasks
import json

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
@app.route('/')
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    tasks = Tasks.query.all()
    l = list(map(lambda t: t.to_json(), tasks))
    return jsonify({'tasks_added': l})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    task = Tasks.query.get(task_id)
    if not task:
        abort(404)
    return jsonify({f'task with id {task_id}':task.to_json()})


@app.errorhandler(404)
def not_found_404(error):
    return make_response(jsonify({'error':'not found'}),404)


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def add_task():
    if not request.json or not request.json['title']:
        abort(400)
    task = Tasks(title=request.json['title'],description=request.json.get('description',""))
    db.session.add(task)
    db.session.commit()
    return jsonify({'task':task.title}), 201


@app.route('/todo/api/v1.0/tasks', methods=['PUT'])
def update_task():
    if not request.json or not request.json.get('id',''):
        abort(400)
    task_id = request.json['id']
    task_to_update = Tasks.query.get(task_id)
    if not task_to_update:
        abort(404)
    task_to_update.title = request.json.get('title',task_to_update.title)
    task_to_update.description = request.json.get('description', task_to_update.description)
    task_to_update.done = request.json.get('done', task_to_update.done)
    db.session.commit()
    return jsonify({f'Updating task with id {task_id}':'Successful'})


@app.route('/todo/api/v1.0/tasks', methods=['DELETE'])
def delete_task():
    if not request.json or not request.json.get('id',''):
        abort(400)
    task_id = request.json['id']
    task_to_delete = Tasks.query.get(task_id)
    if not task_to_delete:
        abort(404)
    db.session.delete(task_to_delete)
    db.session.commit()
    return jsonify({f'Deletion of task with id {task_id}':'Successful'})






# if __name__ == '__main__':
#     app.run(debug = True)

