"""
Business Logic Class.

This class handles the API calls to funding sources and any data processing
that is required.
"""
import os
import requests


class FundingOpportunities:
    """
    A class to represent the funding opportunities API client.

    Attributes:
        api_key (str): The API key used for authorization.
        base_url (str): The base URL for the API endpoints.
    """

    def __init__(self, api_key=None):
        """
        Initializes the FundingAPI with the provided API key.

        Args:
            api_key (str, optional): The API key for authorization. If not
                                    provided, will use the environment
                                    variable.
        """
        self.api_key = api_key or os.getenv('API_KEY')
        self.base_url = "https://www.grants.gov/grantsws/rest/opportunities"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def search_funding_opportunities(self, query, timeout=10):
        """
        Search for funding opportunities.

        Args:
            query (str): The search query for funding opportunities.
            timeout (int, optional): Timeout for the API request in seconds.
                                     Defaults to 10 seconds.

        Returns:
            dict: JSON response from the API if the request is successful.

        Raises:
            requests.exceptions.HTTPError: If the request returns a non-200
                                           status code or if an error occurs.
        """
        url = f"{self.base_url}/search"
        params = {
            "keyword": query,
            "eligibility": "municipality"  # Filtering for municipal government
        }

        try:
            response = requests.get(url, headers=self.headers, params=params,
                                    timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise SystemExit(e) from e

    def get_funding_details(self, funding_id, timeout=10):
        """
        Retrieve details for a specific funding opportunity.

        Args:
            funding_id (str): The ID of the funding opportunity.
            timeout (int, optional): Timeout for the API request in seconds.
                                     Defaults to 10 seconds.

        Returns:
            dict: JSON response containing the funding details.

        Raises:
            requests.exceptions.HTTPError: If the request returns a non-200
                                           status code or if an error occurs.
        """
        url = f"{self.base_url}/{funding_id}"

        try:
            response = requests.get(url, headers=self.headers, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise SystemExit(e) from e

    def submit_funding_application(self, application_data, timeout=10):
        """
        Submit an application for a funding opportunity.

        Args:
            application_data (dict): A dictionary containing the application
            data timeout (int, optional): Timeout for the API request in
            seconds. Defaults to 10 seconds.

        Returns:
            dict: JSON response from the API if the submission is successful.

        Raises:
            requests.exceptions.HTTPError: If the request returns a non-200
                                           status code or if an error occurs.
        """
        url = f"{self.base_url}/applications"

        try:
            response = requests.post(url, headers=self.headers,
                                     json=application_data, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise SystemExit(e) from e
