import json
import facebook


def main():
    token = {"Access_Token"}
    graph = facebook.GraphAPI(token)

    fields = ['email, sports, gender']
    profile = graph.get_object('me', fields=fields )

    print(json.dumps(profile, indent=4))



if __name__=="__main__":
    main()
