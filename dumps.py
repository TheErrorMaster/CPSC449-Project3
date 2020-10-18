import sys
import requests


def dump_jsons(p_url):
    response = requests.get(p_url)
        info = response.json()["keys"] # puts keys in a list
        # prints all keys values here
        for i in info:
            print(requests.get(_url(p_url,i)).json())
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


if __name__ == "__main__":
    dump_jsons(sys.argv[1])
