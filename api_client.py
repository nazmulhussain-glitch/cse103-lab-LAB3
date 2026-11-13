"""Fetch, validate, and summarize users from the JSONPlaceholder API.

This example uses only Python's standard library. A successful run saves the
raw API response to users.json in the current project directory.
"""

import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

API_URL = "https://jsonplaceholder.typicode.com/users"
TIMEOUT_SECONDS = 15


def fetch_users(url: str = API_URL) -> list[dict]:
    """Request user records and return the decoded JSON array.

    Raises HTTPError or URLError for request failures and ValueError when
    the server response is not the expected JSON array.
    """
    request = Request(url, headers={"User-Agent": "CSE103-Lab3/1.0"})

    with urlopen(request, timeout=TIMEOUT_SECONDS) as response:
        if response.status != 200:
            raise RuntimeError(f"Unexpected HTTP status: {response.status}")

        response_text = response.read().decode("utf-8")

    data = json.loads(response_text)

    if not isinstance(data, list):
        raise ValueError("Expected the API response to be a JSON array.")

    return data


def summarize_users(users: list[dict]) -> list[dict]:
    """Extract selected fields from each user record.

    The .get() method is used so that a missing optional field does not
    immediately cause a KeyError.
    """
    summaries = []

    for user in users:
        address = user.get("address") or {}
        summaries.append({
            "id": user.get("id"),
            "name": user.get("name"),
            "username": user.get("username"),
            "email": user.get("email"),
            "city": address.get("city"),
        })

    return summaries


def save_users(users: list[dict], filename: str = "users.json") -> None:
    """Save the complete API response as readable JSON."""
    with open(filename, "w", encoding="utf-8") as output_file:
        json.dump(users, output_file, indent=2, ensure_ascii=False)


def main() -> None:
    """Run the API example and display a short summary."""
    try:
        users = fetch_users()
        summaries = summarize_users(users)

        print(f"Total users received: {len(summaries)}")
        for user in summaries:
            print(
                f'{user["id"]}. {user["name"]} '
                f'(@{user["username"]}) — {user["email"]}'
            )

        save_users(users)
        print("Saved raw API response to users.json")

    except HTTPError as error:
        print(f"HTTP error: {error.code} — {error.reason}")
        print("The API server returned an unsuccessful response.")
    except URLError as error:
        print(f"Network error: {error.reason}")
        print("Check your internet connection and try again.")
    except (TimeoutError, json.JSONDecodeError, ValueError, RuntimeError) as error:
        print(f"API request failed: {error}")
        print("Check the response and try again.")


if __name__ == "__main__":
    main()
