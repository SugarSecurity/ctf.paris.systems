from aws_lambda_powertools.event_handler import AppSyncResolver
from typing import TypedDict, List
import requests, json
from pathlib import Path

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

def welcome(event, context):
    print('lambda started...')
    
    # english is the default language
    if event.get('queryStringParameters') is None:
        target_language = 'en'
    else:
        target_language = event['queryStringParameters'].get('lang')
        if target_language is None:
            target_language = "en"

    # checks if "lang" param exists as a file with ".json" extension
    target_lang_dict_path = Path(f"./translations/{target_language}")
    if not target_lang_dict_path.is_file():
        print('file does not exist - returning error - no file found')
        http_response = {                                                       # returning it to API gateway request
            "statusCode": 200,
            "body": json.dumps({'translated_welcome': "ERROR: file not found"})
        }
        return http_response
    
    else:
        # opening file - if not valid json, just return the whole file as error
        with open(target_lang_dict_path, 'r') as translation_file_raw:
            translation_dict_string = translation_file_raw.read()
            try:
                language_dictionary = json.loads(translation_dict_string)
                welcome_text = language_dictionary['welcome']
            except:
                invalid_dictionary = translation_dict_string
                welcome_text = f"ERROR: {invalid_dictionary}"
        
        http_response = {                                                       # returning it to API gateway request
            "statusCode": 200,                                                  # 200 = success
            "body": json.dumps({'translated_welcome': welcome_text})             # json
        }
        
        return http_response

#def index(event, context):
#    #query = "{query: getPage(id: \"1\") {page_content}}"
#    #ctf_index_html = requests.get(f'http://ctf.paris.systems/prod/graphql?query={query}')
#    
#    http_response = {                                                       # returning it to API gateway request
#        "statusCode": 200,                                                  # 200 = success
#        "headers": {'Content-Type': 'text/html'},                           # html
#        "body": ctf_index_html   # html ^ 
#    }#
#
#    return http_response

#@graphql_api.resolver(type_name="Query", field_name="getPage")
#def get_page(id: str = ""):
#    print(f"Fetching Page {id}")
#    page = ctf_pages[0]
#    page.raise_for_status()
#
#    return page
#
#@graphql_api.resolver(type_name="Query", field_name="listPages")
#def list_pages():
#    return ctf_pages
#
#def graphql_handler(event, _):
#    return graphql_api.resolve(event, None)
#
#if __name__ == "__main__":
#    test_response = translate()
#    print(test_response)