from aws_lambda_powertools.event_handler import AppSyncResolver
from typing import TypedDict, List
import requests, json

# Index - rules
# ---> gets data from /api/graphql and returns it to the frontend
# /api/graphql
# ---> 
# ---> introspection query and graphql injection leaks other URLs and password
# ---> 

class CtfPage(TypedDict, total=False):
    id: str  # required for GraphQL
    page_name: str
    page_content: str
    
rules_html = """<html>
    <body>
        <h1>CTF Rules</h1>
        <ul>
            <li>anything under ctf.paris.systems is fair game</li>
            <li>no DoS / DDoS</li>
        </ul>
    </body>
</html>"""
    
ctf_pages = [
    CtfPage(id="1", page_name="index", page_content=rules_html),
    CtfPage(id="2", page_name="welcome", page_content="redirect to welcome-to-paris translation vulnerability")
]

graphql_api = AppSyncResolver()

def index(event, context):
    query = "{query: getPage(id: \"1\") {page_content}}"
    ctf_index_html = requests.get(f'http://ctf.paris.systems/prod/graphql?query={query}')
    
    http_response = {                                                       # returning it to API gateway request
        "statusCode": 200,                                                  # 200 = success
        "headers": {'Content-Type': 'text/html'},                           # html
        "body": ctf_index_html   # html ^ 
    }

    return http_response

@graphql_api.resolver(type_name="Query", field_name="getPage")
def get_page(id: str = ""):
    print(f"Fetching Page {id}")
    page = ctf_pages[0]
    page.raise_for_status()

    return page

@graphql_api.resolver(type_name="Query", field_name="listPages")
def list_pages():
    return ctf_pages

def graphql_handler(event, _):
    return graphql_api.resolve(event, None)