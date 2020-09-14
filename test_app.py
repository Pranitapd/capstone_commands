import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import db,Commands,Suggestion,Category,setup_db
from auth.auth import AuthError, requires_auth
import datetime


class CapstoneTestCase(unittest.TestCase):
    """This class represents the library test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres','Pranita123','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.admin = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImdnQ2dQckVyUEhkTklvLXAwS3VTOCJ9.eyJpc3MiOiJodHRwczovL3ByYW5pdGEtcGQudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNWUzZGFjYzBlNTllMDA3NmYxNzY4ZCIsImF1ZCI6IkNvZGluZ19jb21tYW5kcyIsImlhdCI6MTYwMDA4MjAyOCwiZXhwIjoxNjAwMDg5MjI4LCJhenAiOiJnYVVuM1BOOGp1dDlXWUk3UGZvYlFyelN6ZjZoUDF5QSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOnN1Z2dlc3Rpb25zIiwiZGVsZXRlOmNvbW1hbmRzIiwiZGVsZXRlOnN1Z2dlc3Rpb25zIiwiZ2V0OmNhdGVnb3JpZXMiLCJnZXQ6Y2F0ZWdvcmlzZWQtY29tbWFuZHMiLCJnZXQ6c3VnZ2VzdGlvbnMiLCJwYXRjaDpjb21tYW5kcyIsInBvc3Q6Y29tbWFuZHMiXX0.Eyc1xTnhwq1kUoi28DUYXHeLKEYJItY5USx_36rJ2qls5bVMEMY5u0DPhtpXX10RLkYkQkeT1YvyuEFp-UjmWEnAkZWDMH5Z2fZcgtEacL_vBQFW7AxMzXcTTzoXOawnxPY3Cspca7dpaH2DS0AFYQSz2hGZADg40GDSjOAFqgWJ174Jb-wH2Amnql-DJ5hy5JM6odYhw56xEawf4UDcXXq-zC5cRZYwR5skjuOCW-brFewgL7taUncxwZnlpVDASXKbT6lxlvAVHEH_JyDc_m68_ko-Bj2GGy-T3eLXWWkEO8sRTwjXdtHn5gUCYFVbf0cBV8T1QNsUdBXqvRPX4w'
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

        self.new_command = {
            'command': ':set list',
            'category': 2,
            'explanation': 'to check the indentations and tab in files'
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_commands(self):
        res = self.client().get('/commands/')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['all_commands']))

    # def test_404_get_commands(self):  #didnt check
    #     res = self.client().get('/commands/')
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)

    def test_get_categorised_commands(self):
        res = self.client().get('/commands/2',headers={'Authorization': 'Bearer ' + self.admin})
        data = json.loads(res.data)
        #print(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['commands']))

    def test_404_get_cotegorised_commands(self):
        res = self.client().get('/commands/10',headers={'Authorization': 'Bearer ' + self.admin})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_get_categories(self):
        res = self.client().get('/categories',headers={'Authorization': 'Bearer ' + self.admin})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['categories']))

    # def test_add_commands(self):  #working
    #     res = self.client().post('/commands',headers={'Authorization': 'Bearer ' + self.admin},json=self.new_command)
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(len(data['new_command']))

    # def test_delete_commands(self):  #working
    #     res = self.client().delete('/commands/7',headers={'Authorization': 'Bearer ' + self.admin})
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(len(data['all_commands']))

    # def test_update_commands(self):  #working
    #     res = self.client().patch('/commands/4',headers={'Authorization': 'Bearer ' + self.admin},json={'command':'SELECT * FROM TABLENAME;'})
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(len(data['updated_command']))
    #     self.assertTrue(len(data['commands']))

    # def test_add_suggestion(self):   #working
    #     res = self.client().post('/suggestions',headers={'Authorization': 'Bearer ' + self.admin},json={'suggestion':'Please add command for maximum value in column','category':4} )
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code,200)
    #     self.assertEqual(data['success'],True)
    #     self.assertTrue(len(data['all_suggestion']))


    def test_get_suggestion(self):
        res = self.client().get('/suggestions',headers={'Authorization': 'Bearer ' + self.admin})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(len(data['suggestions']))

    # def test_delete_suggestion(self): #working
    #     res = self.client().delete('/suggestions/4',headers={'Authorization': 'Bearer ' + self.admin})
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(len(data['suggestions']))

    def test_delete_suggestion_not_found(self):
        res = self.client().delete('/suggestions/7',headers={'Authorization': 'Bearer ' + self.admin})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

if __name__ == "__main__":
    unittest.main()