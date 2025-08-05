"""
MockyAPI.
Fake API calls to simulate using with Grants.gov.
"""

import requests


class MockyAPI:
    """
    A class to interact with a mock API using Mocky.

    This class handles GET and POST requests to Mocky API endpoints
    and processes the response.

    Attributes
    ----------
    base_url : str
        The base URL for the Mocky API endpoint.

    Methods
    -------
    get_data(timeout: float = 5.0):
        Sends a GET request to retrieve data from the API.
    post_data(data_payload: dict, timeout: float = 5.0):
        Sends a POST request with the provided payload to the API.
    """

    def __init__(self, base_url):
        """
        Initializes the MockyAPI with a base URL.

        Parameters
        ----------
        base_url : str
            The URL of the Mocky API endpoint.
        """
        self.base_url = base_url

    def get_data(self, timeout=5.0):
        """
        Sends a GET request to the Mocky API and returns the response data.

        Parameters
        ----------
        timeout : float, optional
            The maximum time to wait for a response (in seconds). Default is
            5.0.

        Returns
        -------
        dict
            The parsed JSON response from the API if successful.
        """
        try:
            response = requests.get(self.base_url, timeout=timeout)
            response.raise_for_status()  # Raises error for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return None

    def post_data(self, data_payload, timeout=5.0):
        """
        Sends a POST request to the Mocky API with the provided payload.

        Parameters
        ----------
        data_payload : dict
            The data to be sent in the POST request.
        timeout : float, optional
            The maximum time to wait for a response (in seconds). Default is
            5.0.

        Returns
        -------
        dict
            The parsed JSON response from the API if successful.
        """
        try:
            response = requests.post(self.base_url, json=data_payload,
                                     timeout=timeout)
            response.raise_for_status()  # Raises error for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # URL for a GET request mock endpoint from Mocky
    mocky_get_url = "https://run.mocky.io/v3/2e80c7e2-c793-4754-ada7-2040b8b5a823"

    # Instantiate the MockyAPI class for GET request
    api = MockyAPI(mocky_get_url)

    # Perform GET request with timeout of 3 seconds
    print("GET Request:")
    data = api.get_data(timeout=3.0)
    if data:
        for user in data:
            print(f"ID: {user['id']}, Name: {user['name']}, "
                  f"Email: {user['email']}")

    # URL for a POST request mock endpoint from Mocky
    mocky_post_url = "https://run.mocky.io/v3/b2345678-cdef-890g-hijk-lmnopqrstuv"

    # Instantiate the MockyAPI class for POST request
    api_post = MockyAPI(mocky_post_url)

    # Example payload for POST request
    payload = {
        "name": "Alice Johnson",
        "email": "alice@example.com"
    }

    # Perform POST request with timeout of 4 seconds
    print("\nPOST Request:")
    post_response = api_post.post_data(payload, timeout=4.0)
    if post_response:
        print(f"Success: {post_response}")
