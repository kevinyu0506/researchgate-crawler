import requests


def get_reference(uid='319879823', offset='5'):
    headers = {
        'authority': 'www.researchgate.net',
        'content-length': '0',
        'accept': 'text/html',
        'rg-request-token': 'aad-r2ot7153OSBz4sxXyzKLnWJK0iXVS3/h+YnCcFs22ouAxpM1/qqdnuoQnJVjuMd3kclPKhZ6EdZ7wSVOQNxTM9KPlcDnJHXf9DSgspXnpXfkOLTtMnaRei6dA85lYXL9XryhQTTujM30J5QFbujeaa89MtwlGKIFUjePGg1IXJSk/FnJ2pZBwUPqEpUmXV/4Li6wKjOhJFN0aQelG4dXXwyZZrFzmhFgIDTCUfTl5frJFM3YUnrwUE6y6VBcBdEOZ1KXv6DJTIq1IQQXxzg=',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'content-type': 'application/json',
        'origin': 'https://www.researchgate.net',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.researchgate.net/publication/319879823_Quantification_of_histochemical_staining_by_color_deconvolution',
        'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
        'cookie': 'did=vjRyRJZbedvZQLFCKBuv1YpgBR5S8Q9hJQly7N7u9o4S8HAbkBjtde3EgxAhx057; ptc=RG1.6749038922759709122.1600151195; _ga=GA1.2.584583719.1600151196; rghfp=true; __cfduid=d133d4635e1ddc3dacb85215b40c27f651606742182; _gid=GA1.2.1981096394.1606742186; __gads=ID=1c27639bd5e7d898:T=1600151214:R:S=ALNI_MZsL7p_odQKVFc_23pjdDf-qMY3LQ; _pbjs_userid_consent_data=3524755945110770; SKpbjs-unifiedid=%7B%22TDID%22%3A%220bebe803-2b3a-4ff6-bb71-cb39ca6c792e%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222020-10-30T13%3A16%3A35%22%7D; SKpbjs-unifiedid_last=Mon%2C%2030%20Nov%202020%2013%3A16%3A35%20GMT; SKpbjs-id5id=%7B%22created_at%22%3A%222020-11-30T16%3A17%3A26.695Z%22%2C%22id5_consent%22%3Atrue%2C%22original_uid%22%3A%22ID5-ZHMOUu-1Mf44ga9Pt-tvEjmX2pzEIdtgzv3Q0VUJ7w%22%2C%22universal_uid%22%3A%22ID5-ZHMONd98_wBogEhlmNHSs6N5n-BA0B7os-4P8cQugw%22%2C%22signature%22%3A%22ID5_AeV0LFxVhIjjzWseyarDrWHYlE1lHVcxS3_aNQG92rFrlPh5P7h1Pl5fbP3zliDzfu_0k9e9126v0bBLQMaJ0mc%22%2C%22link_type%22%3A2%2C%22cascade_needed%22%3Atrue%7D; SKpbjs-id5id_last=Mon%2C%2030%20Nov%202020%2016%3A17%3A27%20GMT; id5id.1st_212_nb=2; GED_PLAYLIST_ACTIVITY=W3sidSI6IlNnM1AiLCJ0c2wiOjE2MDY3NTYzMTEsIm52IjoxLCJ1cHQiOjE2MDY3NDIxOTAsImx0IjoxNjA2NzU2MzExfV0.; chseen=1; ciiir=1; cf_clearance=2583ad47c568d2a037902e1d5f6c877aa9720d1a-1606757132-0-250; sid=p2Er7uoLmLdYg9FzzMPQLSoSuK7f1yFWRIxdtQ6i0NVnIwwKX0nQdsR89M6qKmT01j7ihNQ0jiQyXmG7PGm0FHDUZchJmNko7KtINpBqU8DH4PABkSZd057XH4fToa1a; captui=ZjQ2ZWQ2ZjEwZmNjZDU2OWQ2ZGI4ZWNkYTMzN2FiM2QwNjdlYzZmZTkxYWJmYzE0ZDM2YzlmMTk4MjI3NTU2MF9LMVFMeVBXZEdodXU1NHJPaXdoZnZBcnZDOFJRUVFZb05Jelk%3D; _gat_UA-58591210-1=1',
    }

    params = (
        ('publicationUid', uid),
        ('offset', offset),
    )

    response = requests.post('https://www.researchgate.net/lite.PublicationDetailsLoadMore.getReferencesByOffset.html', headers=headers, params=params)

    return response
