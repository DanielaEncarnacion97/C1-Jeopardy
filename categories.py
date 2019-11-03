def get_categories():
    params = {
        
    }
    url = "http://jservice.io/api/clues"
    response = requests.get(url)
    response_json = response.json()
    # response_json[i]["airdate"]res

    # res = json.dumps(response.text, sort_keys = False, indent = 2)
    # pprint.pprint(res)

