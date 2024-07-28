from src.Applicant import Applicant


class ApplicantSpbgu(Applicant):
    def __init__(self, applicationEducationLevel, directionEducationForm, directionPaymentForm, directionId, subjects,
                 userFullName, userSnils, userUniqueId, userExternalId, priority, withoutExam, fullScore, subjectScore,
                 hasFeature, hasAgreement, hasOriginalDocuments, achievementScore, achievementScoreExtra,
                 hasSpecialFeature, hasAchievement, hasOlympiad, hasOlympiadReset, hasGovernmentContract, needDormitory,
                 certificateAverage, certificateProfileAverage, state):
        super().__init__(withoutExam, fullScore, needDormitory, state, userSnils)
        self.applicationEducationLevel = applicationEducationLevel
        self.directionEducationForm = directionEducationForm
        self.directionPaymentForm = directionPaymentForm
        self.directionId = directionId
        self.subjects = subjects
        self.userFullName = userFullName
        self.userSnils = userSnils
        self.userUniqueId = userUniqueId
        self.userExternalId = userExternalId
        self.priority = priority
        self.withoutExam = withoutExam
        self.fullScore = fullScore
        self.subjectScore = subjectScore
        self.hasFeature = hasFeature
        self.hasAgreement = hasAgreement
        self.hasOriginalDocuments = hasOriginalDocuments
        self.achievementScore = achievementScore
        self.achievementScoreExtra = achievementScoreExtra
        self.hasSpecialFeature = hasSpecialFeature
        self.hasAchievement = hasAchievement
        self.hasOlympiad = hasOlympiad
        self.hasOlympiadReset = hasOlympiadReset
        self.hasGovernmentContract = hasGovernmentContract
        self.needDormitory = needDormitory
        self.certificateAverage = certificateAverage
        self.certificateProfileAverage = certificateProfileAverage
        self.state = state

    def __str__(self):
        return self.toString()

    def toString(self):
        return (
            f"Applicant(\n"
            f"  applicationEducationLevel='{self.applicationEducationLevel}',\n"
            f"  directionEducationForm={self.directionEducationForm},\n"
            f"  directionPaymentForm={self.directionPaymentForm},\n"
            f"  directionId={self.directionId},\n"
            f"  subjects={self.subjects},\n"
            f"  userFullName='{self.userFullName}',\n"
            f"  userSnils='{self.userSnils}',\n"
            f"  userUniqueId='{self.userUniqueId}',\n"
            f"  userExternalId='{self.userExternalId}',\n"
            f"  priority={self.priority},\n"
            f"  withoutExam={self.withoutExam},\n"
            f"  fullScore={self.fullScore},\n"
            f"  subjectScore={self.subjectScore},\n"
            f"  hasFeature={self.hasFeature},\n"
            f"  hasAgreement={self.hasAgreement},\n"
            f"  hasOriginalDocuments={self.hasOriginalDocuments},\n"
            f"  achievementScore={self.achievementScore},\n"
            f"  achievementScoreExtra={self.achievementScoreExtra},\n"
            f"  hasSpecialFeature={self.hasSpecialFeature},\n"
            f"  hasAchievement={self.hasAchievement},\n"
            f"  hasOlympiad={self.hasOlympiad},\n"
            f"  hasOlympiadReset={self.hasOlympiadReset},\n"
            f"  hasGovernmentContract={self.hasGovernmentContract},\n"
            f"  needDormitory={self.needDormitory},\n"
            f"  certificateAverage={self.certificateAverage},\n"
            f"  certificateProfileAverage={self.certificateProfileAverage},\n"
            f"  state='{self.state}'\n"
            f")"
        )
