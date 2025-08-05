"""Views"""

from flask import Blueprint, request, jsonify
# Fixing the correct import
# from .business_logic import FundingOpportunities
from app.services.mocky_api import MockyAPI

# Create a blueprint for organizing routes
main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/search', methods=['GET'])
def search():
    """
    Handle GET requests to search for funding opportunities based on a query.

    This route expects a 'query' parameter to be passed via the URL. It calls
    the `search_funding_opportunities` function to perform the search based on
    the query, and returns the results in JSON format. If no query is provided,
    or if an error occurs during the search, an appropriate error message and
    status code are returned.

    Returns:
        Response: A JSON response containing either the search results with
                  a 200 status code, or an error message with an appropriate
                  status code.

    Possible Error Responses:
        - 400: If the 'query' parameter is missing or if invalid input is
          provided.
        - 500: If a runtime error occurs or for any unexpected errors such as
          TypeError or KeyError.
    """
    query = request.args.get('query', '')
    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400

    try:
        # results = FundingOpportunities(query)
        results = MockyAPI(query)  # Fake API Call
        return jsonify(results), 200
    except ValueError as e:
        return jsonify({'error': 'Invalid input: ' + str(e)}), 400
    except RuntimeError as e:
        return jsonify({'error': 'Runtime error: ' + str(e)}), 500
    except (TypeError, KeyError) as e:
        return (jsonify({'error': 'An unexpected error occurred: ' + str(e)}),
                500)
