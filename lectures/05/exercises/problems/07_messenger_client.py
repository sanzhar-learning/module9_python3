import requests

TARGET_BASE_URL = "https://shantel-clerical-karma.ngrok-free.dev"
SENDER_NAME = "Sanzhar"


def main() -> None:
    while True:
        try:
            text = input("Enter message: ").strip()

            if not text:
                print("Empty message skipped.")
                continue

            response = requests.post(
                f"{TARGET_BASE_URL}/messages",
                json={
                    "sender": SENDER_NAME,
                    "text": text,
                },
                timeout=5,
            )
            response.raise_for_status()

            print(f"Sent successfully: {response.status_code}")

        except KeyboardInterrupt:
            print("\nSender stopped.")
            break
        except requests.exceptions.RequestException as e:
            print(f"Send failed: {e}")


if __name__ == "__main__":
    main()
