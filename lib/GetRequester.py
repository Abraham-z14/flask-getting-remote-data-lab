import json

import requests


class GetRequester:
    """Retrieve remote data from a URL and convert JSON responses."""

    def __init__(self, url):
        """Store the remote URL used for requests."""
        self.url = url

    def get_response_body(self):
        """Send an HTTP GET request and return the raw response body."""
        response = requests.get(self.url)

        return response.content

    def load_json(self):
        """Retrieve the response body and convert JSON into Python data."""
        response_body = self.get_response_body()

        return json.loads(response_body)