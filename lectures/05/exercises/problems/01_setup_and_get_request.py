import requests

URL = "https://jsonplaceholder.typicode.com/todos/1"


def main() -> None:
    try:
        response = requests.get(URL)
        response.raise_for_status()

        status_code = response.status_code
        content_type = response.headers.get("Content-Type")
        raw_body = response.text
        parsed_json = response.json()

        id_ = parsed_json.get("id")
        title = parsed_json.get("title")
        completed = parsed_json.get("completed")

        print(f"Status code: {status_code}")
        print(f"Content-Type: {content_type}")
        print(f"Raw body: {raw_body}")
        print(f"Parsed JSON: {parsed_json}")
        print(f"id: {id_}")
        print(f"title: {title}")
        print(f"completed: {completed}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")


if __name__ == "__main__":
    main()
