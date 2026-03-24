"""Problem 03: GET request for HTML content.

Task:
1. Send GET to https://example.com
2. Print:
   - status code
   - Content-Type header
   - HTML body (response.text)
3. Verify content type contains text/html
4. Add raise_for_status()
"""

import requests

URL = "https://example.com"


def main() -> None:
    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()

        print(f"Status Code: {response.status_code}")
        content_type = response.headers.get("Content-Type", "")
        print(f"Content-Type: {content_type}")
        print(f"HTML Body:\n{response.text}")

        if "text/html" in content_type:
            print("Content type is HTML.")
        else:
            print("Content type is not HTML.")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")


if __name__ == "__main__":
    main()
