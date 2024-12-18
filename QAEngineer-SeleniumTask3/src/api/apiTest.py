
import requests

BASE_URL = "https://api.example.com"  # Replace with your API base URL

def test_get_endpoint(self):
    url = f"{self.BASE_URL}/endpoint"
    response = requests.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertIn("expected_key", response.json())

def test_post_endpoint(self):
    url = f"{self.BASE_URL}/endpoint"
    payload = {
        "key1": "value1",
        "key2": "value2"
    }
    response = requests.post(url, json=payload)
    self.assertEqual(response.status_code, 201)
    self.assertIn("expected_key", response.json())

def test_put_endpoint(self):
    url = f"{self.BASE_URL}/endpoint/1"
    payload = {
        "key1": "new_value1",
        "key2": "new_value2"
    }
    response = requests.put(url, json=payload)
    self.assertEqual(response.status_code, 200)
    self.assertIn("expected_key", response.json())

def test_delete_endpoint(self):
    url = f"{self.BASE_URL}/endpoint/1"
    response = requests.delete(url)
    self.assertEqual(response.status_code, 204)

def test_new_endpoint(self):
    url = f"{self.BASE_URL}/new_endpoint"
    response = requests.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertIn("expected_key", response.json())
