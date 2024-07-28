import requests
from .ApplicantSpbpu import ApplicantSpbgu
from ...Applicant import Applicant



def spbpuRating():
    print("как найти id направления показано в readme.md")
    direction_id = input("пидарас введи id направления: ")

    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36"
    RATING_URL = "https://enroll.spbstu.ru/applications-manager/api/v1/admission-list/form-rating"
    # RATING_URL = "https://enroll.spbstu.ru/applications-manager/api/v1/admission-list/form-rating?applicationEducationLevel=BACHELOR&directionEducationFormId=2&directionId=2121"
    params = {
        "applicationEducationLevel": "BACHELOR",
        "directionEducationFormId": 2,
        # ивт
        # "directionId": 2121

        # мат обеспечение
        # "directionId": 2199

        "directionId": direction_id
    }

    headers = {
        "User-Agent": USER_AGENT
    }

    resp = requests.get(RATING_URL, params=params, headers=headers)
    # resp = requests.get(RATING_URL)
    resp.raise_for_status()

    data = resp.json()

    # data["list"]

    # абитуриенты бви
    # applicants = list(filter(lambda x: x.withoutExam, map(lambda x: Applicant(**x), data["list"])))

    applicants = filter(lambda x: x.hasOriginalDocuments, map(lambda x: ApplicantSpbgu(**x), data["list"]))

    applicants = list(map(lambda x: x.toApplicant(), applicants))

    ratingg = []

    withoutExam = filter(lambda x: x.withoutExam, applicants)

    for applicant in withoutExam:
        ratingg.append(applicant)

    applicants = list(filter(lambda x: not x.withoutExam, applicants))
    applicants.sort(key=lambda x: x.fullScore, reverse=True)

    for applicant in applicants:
        ratingg.append(applicant)

    for i, applicant in enumerate(ratingg):
        print(f"{i} - {applicant}")
