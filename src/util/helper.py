import json
import requests


def parse(fname):
    with open(fname) as f:
        data = json.load(f)

        return data

def get_reference(uid='319879823', offset='5'):

    headers = {
        'authority': 'www.researchgate.net',
        'content-length': '0',
        'accept': 'text/html',
        'rg-request-token': 'aad-PO8We2XyFEq7IY19B8oNNj/a4aUshIutUUGC3mgWq3BsdUQF8tfs96B9TTIoTXGwS9SfebfU7Dkg7fQmQpQTWPhzI3EYSCs9faylpMDkIBxBH1VMiAbbxjH+ftydHhmr9LamkHlNnaoQXgTNZ8lX5PJ8bySqhtRxDSL/9dIaEfxKMCmc99YQO+IROujHo2c4COyuSZpwXH1na4FfryDwgzxRu6hst24Wevuzn+UygilS9acjWlDQtkqVhrkNLU1bEbSVEmECfkIXJCJZYxLgeViYIL+f18FCtC4=',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'content-type': 'application/json',
        'origin': 'https://www.researchgate.net',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.researchgate.net/publication/319879823_Quantification_of_histochemical_staining_by_color_deconvolution',
        'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
        'cookie': 'd=d7e37eb6fe4b8bf0b4765fd1f4e8ae1b81605585347; did=Dreekc0WDMYXrAbcNViNVr8UCjuW7Fg3wdx3cynOByamJR1X2JC6lX8dtp70LySI; ptc=RG1.8911876454667923880.1605585347; _ga=GA1.2.1280472156.1605585351; _pbjs_userid_consent_data=3524755945110770; _pubcid=e2bce89e-159a-4627-93f5-5b9226668778; cto_bidid=n9UaLF9ZQVNDOSUyQkpuRHd0SEpoU0ZxdHdFT3pUOSUyQjlBV2dRTWRibEVNJTJGTXRRbVg0dVlRdEZKOGRPS2VpTnE2dm5SUGRVYm9uVHNNNlpXJTJCRDRnbVRjJTJCZW9oOFElM0QlM0Q; cto_bundle=uH-C9l9iQjhOJTJGTk42MjFzcm5XRnByJTJGajNjcU5FcWd5WldwTE1EZ0RBJTJGVFNpbkNmV2ZDYThwVndkY3RUakluRjFidktxSWJTeE5RUmhMY1UlMkJhQ2xRWVNEVyUyRlczeUI0OWpKUXV0SE1JOWdvZTEyM3I5MnFIdUhkbm0yNG9YdVVMZUhUdlo; pbjs-unifiedid=%7B%22TDID%22%3A%22a86f2d96-5d6d-448d-90f0-c23f628cc43c%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222020-10-17T03%3A55%3A53%22%7D; __gads=ID=ee7b2c56431a61df:T=1605585353:S=ALNI_MYyXIowNaw9sKyTv8fDlUicAosoOQ; sid=oUXQ7Sr3KUs9pl3gRgCJscOlYeErMeiUzIJG1CSOoB248iWk80j4IXwjL0Li8gAvtmKtNB2nV3WJCftwBFWItujWFQ2Q6TlmY8q1m02gCs3D7w3uyROifU3Q88MyW8kG; _gid=GA1.2.3380060.1607004342; SKpbjs-unifiedid=%7B%22TDID%22%3A%22a86f2d96-5d6d-448d-90f0-c23f628cc43c%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222020-11-03T14%3A20%3A49%22%7D; SKpbjs-unifiedid_last=Thu%2C%2003%20Dec%202020%2014%3A20%3A50%20GMT; id5id.1st_212_nb=0; SKpbjs-id5id=%7B%22created_at%22%3A%222020-12-03T14%3A20%3A50.775Z%22%2C%22id5_consent%22%3Atrue%2C%22original_uid%22%3A%22ID5-ZHMOWi06AeEFhKB_CGlGuv-Z67tiyoT9hy34V4mJTg%22%2C%22universal_uid%22%3A%22ID5-ZHMOfjjnwa3ehPlkEY7LcnToCd0zgSDLm9T86AFaag%22%2C%22signature%22%3A%22ID5_AYcwZX15AowM6jIW-0TaeaXGPF5CX_MSbalOTHthh_qLzpFyC4-qGAtE1O88XkZq2QtNEbOnM9Y_yM9TSg9XwLs%22%2C%22link_type%22%3A2%2C%22cascade_needed%22%3Atrue%7D; SKpbjs-id5id_last=Thu%2C%2003%20Dec%202020%2014%3A20%3A50%20GMT; rghfp=true; _gat_UA-58591210-1=1; GED_PLAYLIST_ACTIVITY=W3sidSI6IklwNTciLCJ0c2wiOjE2MDcwMTIzOTIsIm52IjowLCJ1cHQiOjE2MDcwMDQzNDUsImx0IjoxNjA3MDEyMzg3fV0.; _gat=1',
    }

    params = (
        ('publicationUid', uid),
        ('offset', offset),
    )

    response = requests.post('https://www.researchgate.net/lite.PublicationDetailsLoadMore.getReferencesByOffset.html', headers=headers, params=params)

    return response
