import os
import unittest
from todo_app import app,db
import json
from todo_app.models import Tasks

TEST_DB = 'test.db'
basedir = os.path.abspath(os.path.dirname(__file__))


class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                                os.path.join(basedir, TEST_DB)
        self.client = app.test_client()
        db.drop_all()
        db.create_all()

        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    def test_add_task_is_successful(self):
        response = self.client.post('/todo/api/v1.0/tasks',
            data=json.dumps(dict(title='Clean House', description="Dusting the whole house")),
            content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_add_task_non_json_payload(self):
        response = self.client.post('/todo/api/v1.0/tasks')
        self.assertEqual(response.status_code, 400)


    def test_get_all_tasks_is_successful(self):
        response = self.client.post('/todo/api/v1.0/tasks',
                                    data=json.dumps(dict(title='Clean House', description="Dusting the whole house")),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.client.get('/todo/api/v1.0/tasks')
        self.assertEqual(response.status_code, 200)

    def test_get_task_by_id_is_successful(self):
        response = self.client.post('/todo/api/v1.0/tasks',
                                    data=json.dumps(dict(title='Clean House', description="Dusting the whole house")),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.client.get('/todo/api/v1.0/tasks/1')
        self.assertEqual(response.status_code, 200)

    def test_get_task_by_id_handles_unknown_id(self):
        response = self.client.post('/todo/api/v1.0/tasks',
                                    data=json.dumps(dict(title='Clean House', description="Dusting the whole house")),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.client.get('/todo/api/v1.0/tasks/2')
        self.assertEqual(response.status_code, 404)

    def test_update_task_details_is_successful(self):
        response = self.client.post('/todo/api/v1.0/tasks',
                                    data=json.dumps(dict(title='Clean House', description="Dusting the whole house")),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.client.put('/todo/api/v1.0/tasks',
                                    data=json.dumps(dict(id=1, title='Clean Room', description="Dusting the living room")),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_update_task_details_missing_id(self):
        response = self.client.post('/todo/api/v1.0/tasks',
                                    data=json.dumps(dict(title='Clean House', description="Dusting the whole house")),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.client.put('/todo/api/v1.0/tasks',
                                   data=json.dumps(
                                       dict(title='Clean Room', description="Dusting the living room")),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_update_task_details_handles_unknown_task_id(self):
        response = self.client.post('/todo/api/v1.0/tasks',
                                    data=json.dumps(dict(title='Clean House', description="Dusting the whole house")),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.client.put('/todo/api/v1.0/tasks',
                                   data=json.dumps(
                                       dict(id=2, title='Clean Room', description="Dusting the living room")),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_delete_task_by_id_is_successful(self):
        response = self.client.post('/todo/api/v1.0/tasks',
                                    data=json.dumps(dict(title='Clean House', description="Dusting the whole house")),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.client.delete('/todo/api/v1.0/tasks',
                                    data=json.dumps(dict(id=1)),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete_task_by_id_handles_unknown_task_id(self):
        response = self.client.post('/todo/api/v1.0/tasks',
                                    data=json.dumps(dict(title='Clean House', description="Dusting the whole house")),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.client.delete('/todo/api/v1.0/tasks',
                                      data=json.dumps(dict(id=3)),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 404)


    def test_delete_task_by_id_missing_id(self):
        response = self.client.post('/todo/api/v1.0/tasks',
                                    data=json.dumps(dict(title='Clean House', description="Dusting the whole house")),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.client.delete('/todo/api/v1.0/tasks',
                                      data=json.dumps(dict()),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_tasks_class_repr(self):
        db_object = Tasks(title="Organize wardrobe")
        self.assertEquals(str(db_object),"Task: Organize wardrobe")





# if __name__ == "__main__":
#     unittest.main()