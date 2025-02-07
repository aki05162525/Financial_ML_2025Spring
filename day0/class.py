class SchoolReport:
    def __init__(self, student_name,
                 math_score,jp_score,en_score):
        self.student_name = student_name
        self.math_score = math_score
        self.jp_score = jp_score
        self.en_score = en_score
        
    def calc_ave_score(self):
        sum_score = (self.math_score
                     +self.jp_score
                     +self.en_score)
        ave_score = sum_score/3
        return ave_score
        

sr_a = SchoolReport('田中 A', 100, 30, 50)
avg_a = sr_a.calc_ave_score()
print(f'Aさんの3教科の平均点：{avg_a}')




