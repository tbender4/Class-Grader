import math

class Score:
    # def __init__(self):
    #     self.score_grade = -1
    #     self.curve_grade = -1
    #     self.use_curve = False

    def __init__(self, score_grade=-1, use_curve=False, curve_grade = -1):
        self.score_grade = score_grade
        self.curve_grade = score_grade
        self.use_curve = use_curve

    def score_dict(self):
        return {
            "raw" : self.score_grade,
            "curve" : self.curve_grade,
            "use_curve" : self.use_curve
        }

    def printScore(self):
        print("Raw:", self.score_grade, "Curve", self.curve_grade, "Using Curve:",self.use_curve,end='')

    #apply to self grade
    def score_curve(self, style, variable=100):
        if style == 0:  # flat, no change to score
            return
        if style == 1:  # "waxman curve"
            self.curve_grade = (math.sqrt(self.score_grade) * 10)
        if style == 2:  # decrease full points
            self.curve_grade = self.score_grade / variable  # variable is denominator.
        if style == 3:  # flat increase from variable
            self.curve_grade += variable

    @staticmethod
    def batch_apply_curve(grades=[], style=0, variable=100):
        for grade in grades:
            grade.score_curve(style, variable)

    @staticmethod    
    def score_generate_grade(scores=[], use_curve = False):
        total = 0
        if use_curve == False:
            for score in scores:
                total += score.score_grade
        else:
            for score in scores:
                total += score.curved_score

        return total / len(scores)


class Attendance:
	# status numbers: -1 = unknown, 0 = absent, 1 = present, 2 = late
    
    def __init__(self, day_status=-1):
        self.day_status = day_status

    def edit_day(self, day_status):
        day_status = day_status

    def printAttendance(self):
        print(self.day_status, end='')

    @staticmethod
    def attendance_generate_grade(attendance=[-1], free_miss_days=0, have_max_missed_days=False, max_missed_days=6, late_convert_to_absence=False, late_penalty=0.5):
        attended = 0
        late = 0
        for class_day in attendance:
            if class_day == 1:
                attended += 1
            if class_day == 0:
                max_missed_days -= 1
            if class_day == 2:
                late += late_penalty

        raw_score = attended / len(attendance) - free_miss_days - late

        if have_max_missed_days:
            if max_missed_days < 0:
                return 0	#fail
        if raw_score >= 1:
            return 1	#max points adjusted to max score
        return attended / len(attendance)

