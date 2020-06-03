import math
import datetime

attendance_date_template = []
#TODO: 5/28: It may be easier if I just ask for dates to be created upon initialization and not have change.
#We can start with asking frequency of the class and then add another code for "Not counted" date.

homework_size = 0   #Number of homeworks assigned for specific class
quiz_size = 0
exam_size = 0
#TODO: Have the count be compared to the size of the array. If need be, create dummy values for ungraded Scores.
# Focus on implementing this after properly implementin attendance. (have attendance be fixed)


def attendance_date_range_dryrun(checkmark_list, from_date_str=datetime.datetime.now(), to_date_str=datetime.datetime.now()+datetime.timedelta(days = 180)):
    #checkmark_list: [1, 0, 1, 0, 0, 0, 1] -> monday, tuesday, saturday

    #if returns true, it is a valid range. Output is just whatever text may appear if clicked on "validate" instead of Apply/OK
    #date: mm/dd/yy
    #TODO: Need to sanitize (maybe in gui?)

    dates = []

    try:
        from_date = datetime.datetime.strptime(date_string=from_date_str, format='%m/%d/%y')
        to_date = datetime.datetime.strptime(date_string=to_date_str, format='%m/%d/%y')
        delta = to_date - from_date
    except ValueError:
        return (False, "Incorrect formatting.")
    except:
        return (False, "Unknown Error")
    
    if delta.days <= 0:
        return (False, "ERROR: Invalid range.")

    #TODO: inefficient method of iterating every date. Could use a speedup.
    date_i = from_date
    count = 0
    while date_i != to_date + datetime.timedelta(days=1):
        if checkmark_list[date_i.weekday()]:
            count += 1
            #        attendance_date_template.append(date_i.strftime("%m/%d/%y"))
        date_i = date_i + datetime.timedelta(days=1)



    
    if count == 0:
        return (False, "Too short of a range.")
    
    return (True, "From {} to {} will be {} days of class.".format(from_date.strftime("%B %e, %Y"), to_date.strftime("%B %e %Y"), count))


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
    #
    def __init__(self, day_status=-1, date = datetime.datetime.now()):
        self.day_status = day_status
        self.date = date
        self.printAttendance()

    def edit_day(self, day_status):
        self.day_status = day_status

    def printAttendance(self):
        print(self.day_status, self.date.today(), end='')

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

