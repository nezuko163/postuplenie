import requests
from .ApplicantSpbgu import ApplicantSpbgu

URL = "https://application.spbu.ru/enrollee_lists/list-view-lists"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36"

params = {
    # мат обеспечение
    "id": 49
}

headers = {
    "User-Agent": USER_AGENT
}

def spbguRating() -> dict:
    resp = requests.get(URL, headers=headers, params=params)
    resp.raise_for_status()

    data = resp.json()

    applicant = ApplicantSpbgu.from_dict(data["list"][0])

    applicants = filter(lambda x: x.withoutExam,map(lambda x: ApplicantSpbgu.from_dict(x), data["list"]))


    lst = list(applicants)

    print(lst.__len__())