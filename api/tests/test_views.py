from .test_setup import TestSetUp
from ..models import User


class TestViews(TestSetUp):
    def test_invalid_login(self):
        res = self.client.post(self.login_url, {'email_address': 'test@test.com', 'password': 'wrongpassword'})
        self.assertEqual(res.status_code, 400)

    def test_valid_login(self):
        res = self.client.post(self.login_url, {'email_address': 'harry@harry.com', 'password': 'test'})
        self.assertEqual(res.status_code, 200)

    def test_logout(self):
        res = self.client.post(self.login_url, {'email_address': 'harry@harry.com', 'password': 'test'})
        self.assertEqual(res.status_code, 200)
        self.client.logout()
        res = self.client.get('/login')
        self.assertEqual(res.status_code, 200)

    def test_create_user(self):
        # Arrange
        new_user_data = {
                    'first_name': 'Demo124',
                    'last_name': 'Doez',
                    'email_address': 'Demo123@jexample.com',
                    'phone_number': '5551111234',
                    'street_address1': '123 Main St.',
                    'city': 'Demo123',
                    'state': 'CA',
                    'zip_code': '12345'
                }


        # Act
        res = self.client.post('https://xntg7p1h47.execute-api.us-east-1.amazonaws.com/UAT/first', data=new_user_data)

        # Assert
        #self.assertEqual(res.status_code, 200)
        pass


    def test_create_user2(self):
        # Arrange
        new_user_data = {

                    "first_name": "*",
                    "last_name": "*",
                    "email_address": ".",
                    "phone_number": "-",
                    "street_address1": "#",
                    "city": "+",
                    "state": "2",
                    "zip_code": "-2"
                }


        # Act
        res = self.client.post('https://xntg7p1h47.execute-api.us-east-1.amazonaws.com/UAT/first', data=new_user_data)

        # Assert
        #self.assertEqual(res.status_code, 200)
        pass
       

    def requ_id_status(self):
        # Arrange
        new_user_data = {
                  "request_id": "a02f325c-9f79-448b-9755-3d8000286b1f"
                }



        # Act
        res = self.client.post('https://7wdf6k3w65.execute-api.us-east-1.amazonaws.com/UAT', data=new_user_data)

        # Assert
        self.assertEqual(res.status_code, 200)
       
    
    def assign_sales_rep(self):
        # Arrange
        new_user_data = {
                      "request_id_list": ["0cd22713-857d-41c0-a79a-4c6cbaacaa17", "1778c13e-73ce-4ae3-9f81-d53986aaa422"],
                      "sales_rep_id": "999999999"
                    }


        # Act
        res = self.client.post('https://045zhv1hwl.execute-api.us-east-1.amazonaws.com/UAT', data=new_user_data)

        # Assert
        self.assertEqual(res.status_code, 200)
       
    
    
    def list_cust_of_sales_rep(self):
        # Arrange
        new_user_data = {
                      "sales_rep_id": "999999999"
                    }

        # Act
        res = self.client.post('https://lwwzhr7ifi.execute-api.us-east-1.amazonaws.com/UAT', data=new_user_data)

        # Assert
        self.assertEqual(res.status_code, 200)


    def list_cust_of_sales_rep2(self):
        new_user_data = {
            "sales_rep_id": "-2"
        }

        res = self.client.post("https://lwwzhr7ifi.execute-api.us-east-1.amazonaws.com/UAT", data=new_user_data)

        self.assertEqual(res.status_code, 200)


    def list_cust_of_sales_rep3(self):
        new_user_data = {
            "sales_rep_id": "0"
        }

        res = self.client.post("https://lwwzhr7ifi.execute-api.us-east-1.amazonaws.com/UAT", data=new_user_data)

        self.assertEqual(res.status_code, 200)
       
    def test_get_users(self):

            # Act
            res = self.client.get('https://h0pt17fv6g.execute-api.us-east-1.amazonaws.com/UAT')

            # Assert
            #self.assertEqual(res.status_code, 200)
            pass