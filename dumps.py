import sys
import requests


def dump_jsons(p_url):
    try:
        response = requests.get(p_url)
        for item in response.json():
            print(item)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


if __name__ == "__main__":
    dump_jsons(sys.argv[1])
