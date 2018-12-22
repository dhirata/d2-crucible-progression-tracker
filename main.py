import secrets
import requests
import json


MEMBERSHIP_TYPES = {
    "xbox": 1,
    "psn": 2,
    "pc": 4
}

ENDPOINT = "https://www.bungie.net/Platform"

HEADER = {"X-API-Key":secrets.BUNGIE_KEY}


def get_membership_id(display_name, membership_type):
    if(membership_type == MEMBERSHIP_TYPES["pc"]):
        display_name = display_name.replace("#", "%23") # work around for poundsign in bliz accts
    url = "{}/Destiny2/SearchDestinyPlayer/{}/{}/".format(ENDPOINT, membership_type, display_name)
    request = requests.get(url, headers=HEADER)
    response_json = json.loads(request.text)
    memberships = response_json["Response"]
    if(len(memberships) < 1):
        raise ValueError("No account was found with the given parameters. Check your spelling \
            and platform type")
    elif(len(memberships) > 1):
        raise ValueError("Multiple accounts were found for the given parameters. ¯\\_(ツ)_/¯")
    else:
        return memberships[0]["membershipId"]


# def get_historical_stats(membership_type, membership_id):
#     url = "{}/Destiny2/{}/Account/{}/Stats/".format(ENDPOINT, membership_type, membership_id)
#     request = requests.get(url, headers=HEADER)
#     response = json.loads(request.text)
#     return response


def main():
    id1 = get_membership_id("Japain#11485", MEMBERSHIP_TYPES["pc"])
    id2 = get_membership_id("LeftoversAgain", MEMBERSHIP_TYPES["psn"])
    # stat = get_historical_stats(MEMBERSHIP_TYPES["pc"], id1)
    print(id1)
    print(id2)
    # print(stat)


if __name__ == "__main__":
    main()
