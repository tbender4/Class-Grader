class Grading:
	def __init__(self):
		self.style			#attendance, participation, or score-based grading
		self.weight = -1	#scale of 0.0-1.0 of how much weight this will have on the grade
		self.raw_score = -1	#scale of 0.0-1.0 of the raw score
		
	def attendance_grading(self):
		self.days = [] #array(maybe dict) of days of the week to make the whole school year.
		#make it true/false value
	
	def attendance_generate_grade(self):
		attended = 0		#possibly import and not keep locally
		for day in self.days:
			if day:
				attended += 1
		
		self.raw_score = attended / len(self.days)
	
	def participation_grading(self):
		#teacher-reported grade with preferences
		self.type #0 = daily mandatory, 1 = improve-to-A, 2 = pure extra credit
	#write participation_generate_grade

	def score_grading(self):
		#can be homework or exam based
		self.scores = [] #list of scores. possibly need to import

	def score_generate_grade(self):
		total = 0
		for score in scores:
			score += total
		self.raw_score = total / len(self.scores)
	
	def score_curve_style(self, style):
		if style == 0:		#flat, no change
			curve == 0