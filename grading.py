import math


class Grading:
    def __init__(self):
		self.style  # attendance, participation, or score-based grading
		self.weight = -1  # scale of 0.0-1.0 of how much weight this will have on the grade
		self.grade = -1  # scale of 0.0-1.0 of the raw grade

	# def override_grade(self, entry)
	# try: self.grade = entry
	# except:

    def attendance_grading(self):
	    # array(maybe dict) of days of the week to make the whole school year.
	    self.days = []
		# make it true/false value if attended

    def attendance_generate_grade(self):
		attended = 0  # possibly import and not keep locally
		for class_day in self.days:
			if class_day:
				attended += 1

		self.grade = attended / len(self.days)

    def participation_grading(self):
		# teacher-reported grade with preferences
		self.type  # 1 = weight from grade A to B = pure extra credit
	# write participation_generate_grade

    def score_grading(self):
		# can be homework or exam based
		self.scores = []  # list of scores. possibly need to import

    def score_generate_grade(self):
		total = 0
		for score in scores:
			score += total
		self.raw_score = total / len(self.scores)
		self.curved_score = self.score_curve(
		    0, self.raw_score)  # 0 means no influence

    def score_curve(self, style, raw_score, variable=100):
		if style == 0:  # flat, no change to score
			return raw_score
		if style == 1:  # "waxman curve"
		    return (math.sqrt(raw_score) * 10)
		if style == 2:  # decrease full points
			return raw_score / variable  # variable is denominator.
		if style == 3:  # flat increase
			return raw_score + variable


class Attendance:
	# status numbers: -1 = unknown, 0 = absent, 1 = present, 2 = late
	def __init__(self):
		self.day_status = -1

	@staticmethod
	def attendance_generate_grade(attendance=[-1], free_miss_days=0,
									have_max_missed_days=False, max_missed_days=6,
									late_convert_to_absence=False, late_penalty=0.5):
		attended = 0
        late = 0
		for class_day in attendance:
			if class_day == 1:
				attended += 1
            if class_day == 0:
				max_missed_days -= 1
            if class_day == 2:
                late += late_penalty

		
		raw_score = attended / len(attendance) - free_miss_days


		if have_max_missed_days:
			if max_missed_days < 0:
				return 0	#fail
		if raw_score >= 1:
			return 1	#max points adjusted to 1 if user attended all possible classes
		return attended / len(attendance)

