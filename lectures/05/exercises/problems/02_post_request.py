"""Problem 02: POST request to JSONPlaceholder.

Task:
1. Send POST to https://jsonplaceholder.typicode.com/posts
2. Send JSON payload with fields: title, body, userId
3. Print:
   - status code
   - raw body
   - parsed JSON
4. Confirm response includes your data + id

Note: JSONPlaceholder simulates writes; data is not truly persisted.
"""

import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def main() -> None:
    payload = {
        "title": "My Post Title",
        "body": "This is the body of my post.",
        "userId": 123,
    }

    try:
        response = requests.post(URL, json=payload, timeout=5)
        response.raise_for_status()

        print(f"Status Code: {response.status_code}")
        print(f"Raw Body: {response.text}")

        json_response = response.json()
        print(f"Parsed JSON: {json_response}")

        assert json_response.get("title") == payload["title"]
        assert json_response.get("body") == payload["body"]
        assert json_response.get("userId") == payload["userId"]
        assert "id" in json_response

        print("Response includes sent data and an id.")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except AssertionError:
        print("Response does not include expected data.")


if __name__ == "__main__":
    main()
