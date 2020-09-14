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
        self.admin = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImdnQ2dQckVyUEhkTklvLXAwS3VTOCJ9.eyJpc3MiOiJodHRwczovL3ByYW5pdGEtcGQudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNWUzZGFjYzBlNTllMDA3NmYxNzY4ZCIsImF1ZCI6IkNvZGluZ19jb21tYW5kcyIsImlhdCI6MTYwMDA3MjY3OSwiZXhwIjoxNjAwMDc5ODc5LCJhenAiOiJnYVVuM1BOOGp1dDlXWUk3UGZvYlFyelN6ZjZoUDF5QSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOnN1Z2dlc3Rpb25zIiwiZGVsZXRlOmNvbW1hbmRzIiwiZGVsZXRlOnN1Z2dlc3Rpb25zIiwiZ2V0OmNhdGVnb3JpZXMiLCJnZXQ6Y2F0ZWdvcmlzZWQtY29tbWFuZHMiLCJnZXQ6c3VnZ2VzdGlvbnMiLCJwYXRjaDpjb21tYW5kcyIsInBvc3Q6Y29tbWFuZHMiXX0.HuITrGz-UbQ64SCZq4R986TsME7TUOJIui9FXixtn0tV2ig85OtMH0tGVplTujPzd86rZtPLW1-uj-WCdVNiwtbQc6Ta4VeNHNxYuP-YTeGtj49lN5t3Ta4XocNJIEZxJNpHvxpbximoGGpa3_nFPOFd5Yc-JRI0qDlnOjtPJOCGq6hq5xYj4zFox3nUa4_UP5z9RJ2AVtINbbLP_KyYA7m85rbXlbI3_s1jXQmFZ56Lxu-rc-qZNRgv1pdgFWFCPG-WHf88DOLdWra3Qb5Zm1YU2d28oaBeqeZYjrah8Bp7V2t2YTDpKc7tpSlZ83YNXh2A8V_GnklaUkbHIBU5mQ'
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_commands(self):
        res = self.client().get('/commands/')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['all_commands']))

    def test_get_categorised_commands(self):
        res = self.client().get('/commands/2',headers={'Authorization': 'Bearer ' + self.admin})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['commands']))

if __name__ == "__main__":
    unittest.main()