from typing import Optional, Dict

from src.Applicant import Applicant


class ApplicantSpbgu(Applicant):
    def __init__(self, id: int, created_at: str, updated_at: str, list_date: str, competitive_group_id: int,
                 order_number: int, user_id: Optional[int], user_code: str, trials_type: str, without_trials: bool,
                 score_overall: int, score_trials: int, score_achievements: int, preemptive_right: bool,
                 original_document: bool, contract_concluded: bool, admission_recommended: bool,
                 admission_order: Optional[int], average_grade_point: Optional[float],
                 average_profile_point: Optional[float], trial1_name: Optional[str], trial2_name: Optional[str],
                 trial3_name: Optional[str], trial4_name: Optional[str], trial5_name: Optional[str],
                 trial1_score: Optional[int], trial2_score: Optional[int], trial3_score: Optional[int],
                 trial4_score: Optional[int], trial5_score: Optional[int], without_trials_basis: Optional[str],
                 target_organization: Optional[str], priority_number: int, control_passed: bool, comment: str):
        super().__init__(
            withoutExam=without_trials,
            fullScore=score_overall,
            needDormitory=False,
            priority=priority_number,
            snils=user_code
        )
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.list_date = list_date
        self.competitive_group_id = competitive_group_id
        self.order_number = order_number
        self.user_id = user_id
        self.user_code = user_code
        self.trials_type = trials_type
        self.without_trials = without_trials
        self.score_overall = score_overall
        self.score_trials = score_trials
        self.score_achievements = score_achievements
        self.preemptive_right = preemptive_right
        self.original_document = original_document
        self.contract_concluded = contract_concluded
        self.admission_recommended = admission_recommended
        self.admission_order = admission_order
        self.average_grade_point = average_grade_point
        self.average_profile_point = average_profile_point
        self.trial1_name = trial1_name
        self.trial2_name = trial2_name
        self.trial3_name = trial3_name
        self.trial4_name = trial4_name
        self.trial5_name = trial5_name
        self.trial1_score = trial1_score
        self.trial2_score = trial2_score
        self.trial3_score = trial3_score
        self.trial4_score = trial4_score
        self.trial5_score = trial5_score
        self.without_trials_basis = without_trials_basis
        self.target_organization = target_organization
        self.priority_number = priority_number
        self.control_passed = control_passed
        self.comment = comment

    @classmethod
    def from_dict(cls, data: Dict[str, Optional[any]]) -> 'ApplicantSpbgu':
        return cls(
            id=data.get('id'),
            created_at=data.get('created_at'),
            updated_at=data.get('updated_at'),
            list_date=data.get('list_date'),
            competitive_group_id=data.get('competitive_group_id'),
            order_number=data.get('order_number'),
            user_id=data.get('user_id'),
            user_code=data.get('user_code'),
            trials_type=data.get('trials_type'),
            without_trials=data.get('without_trials'),
            score_overall=data.get('score_overall'),
            score_trials=data.get('score_trials'),
            score_achievements=data.get('score_achievements'),
            preemptive_right=data.get('preemptive_right'),
            original_document=data.get('original_document'),
            contract_concluded=data.get('contract_concluded'),
            admission_recommended=data.get('admission_recommended'),
            admission_order=data.get('admission_order'),
            average_grade_point=data.get('average_grade_point'),
            average_profile_point=data.get('average_profile_point'),
            trial1_name=data.get('trial1_name'),
            trial2_name=data.get('trial2_name'),
            trial3_name=data.get('trial3_name'),
            trial4_name=data.get('trial4_name'),
            trial5_name=data.get('trial5_name'),
            trial1_score=data.get('trial1_score'),
            trial2_score=data.get('trial2_score'),
            trial3_score=data.get('trial3_score'),
            trial4_score=data.get('trial4_score'),
            trial5_score=data.get('trial5_score'),
            without_trials_basis=data.get('without_trials_basis'),
            target_organization=data.get('target_organization'),
            priority_number=data.get('priority_number'),
            control_passed=data.get('control_passed'),
            comment=data.get('comment')
        )

    def toString(self) -> str:
        return (f"ApplicantSpbgu(\n"
                f"  id={self.id!r},\n"
                f"  created_at={self.created_at!r},\n"
                f"  updated_at={self.updated_at!r},\n"
                f"  list_date={self.list_date!r},\n"
                f"  competitive_group_id={self.competitive_group_id!r},\n"
                f"  order_number={self.order_number!r},\n"
                f"  user_id={self.user_id!r},\n"
                f"  user_code={self.user_code!r},\n"
                f"  trials_type={self.trials_type!r},\n"
                f"  without_trials={self.without_trials!r},\n"
                f"  score_overall={self.score_overall!r},\n"
                f"  score_trials={self.score_trials!r},\n"
                f"  score_achievements={self.score_achievements!r},\n"
                f"  preemptive_right={self.preemptive_right!r},\n"
                f"  original_document={self.original_document!r},\n"
                f"  contract_concluded={self.contract_concluded!r},\n"
                f"  admission_recommended={self.admission_recommended!r},\n"
                f"  admission_order={self.admission_order!r},\n"
                f"  average_grade_point={self.average_grade_point!r},\n"
                f"  average_profile_point={self.average_profile_point!r},\n"
                f"  trial1_name={self.trial1_name!r},\n"
                f"  trial2_name={self.trial2_name!r},\n"
                f"  trial3_name={self.trial3_name!r},\n"
                f"  trial4_name={self.trial4_name!r},\n"
                f"  trial5_name={self.trial5_name!r},\n"
                f"  trial1_score={self.trial1_score!r},\n"
                f"  trial2_score={self.trial2_score!r},\n"
                f"  trial3_score={self.trial3_score!r},\n"
                f"  trial4_score={self.trial4_score!r},\n"
                f"  trial5_score={self.trial5_score!r},\n"
                f"  without_trials_basis={self.without_trials_basis!r},\n"
                f"  target_organization={self.target_organization!r},\n"
                f"  priority_number={self.priority_number!r},\n"
                f"  control_passed={self.control_passed!r},\n"
                f"  comment={self.comment!r})")

    def __str__(self) -> str:
        return self.toString()

    def __repr__(self) -> str:
        return self.toString()
