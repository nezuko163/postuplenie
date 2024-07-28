class Applicant:
    def __init__(self, withoutExam=False, fullScore=-1, needDormitory=False, priority=-1, snils="какого хуя нет"):
        self.withoutExam = withoutExam
        self.fullScore = fullScore
        self.needDormitory = needDormitory
        self.priority = priority
        self.snils = snils

    def toApplicant(self) -> "Applicant":
        return Applicant(
            self.withoutExam,
            self.fullScore,
            self.needDormitory,
            self.priority,
            self.snils
        )

    def toString(self):
        return (f"Applicant(бви={self.withoutExam}, "
                f"баллы={self.fullScore}, "
                f"нужна ли общага={self.needDormitory}, "
                f"приоритет зачисления={self.priority}, "
                f"снилс={self.snils})")

    def __str__(self):
        return self.toString()