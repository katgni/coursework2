import unittest
from treasures import app
from flask import request

class FlaskTestCase(unittest.TestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = self.client.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data)
		
    # Ensure login behaves correctly with correct credentials
    def test_correct_login(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(username="kat", passwd="napier"),
                follow_redirects=True
            )
            self.assertIn(b'You were logged in', response.data)
            self.assertTrue(current_user.name == "kat")
            self.assertTrue(current_user.is_active())
			
			
	    # Ensure login behaves correctly with incorrect credentials
    def test_incorrect_login(self):
        response = self.client.post(
            '/login',
            data=dict(username="wrong", passwd="wrong"),
            follow_redirects=True
        )
        self.assertIn(b'Invalid username or password.', response.data)		
	
	
    # Ensure logout behaves correctly
    def test_logout(self):
        with self.client:
            self.client.post(
                '/login',
                data=dict(username="kat", passwd="napier"),
                follow_redirects=True
            )
            response = self.client.get('/logout', follow_redirects=True)
            self.assertIn(b'You were logged out', response.data)
            self.assertFalse(current_user.is_active())

    # Ensure that logout page requires user login
    def test_logout_route_requires_login(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)
	
	
		
if __name__ == "__main__":
 app.run( host ='0.0.0.0', debug = True )