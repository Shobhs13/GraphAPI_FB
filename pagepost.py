import json
import facebook


def main():
    token = {"Access_token"}
    graph = facebook.GraphAPI(token)

    fields = ['id', 'name', 'about', 'posts', 'likes']
    fields = ','.join(fields)

    page = graph.get_object('tedxtiet', fields=fields)

    print(json.dumps(page, indent=4))

if __name__=="__main__":
    main()
