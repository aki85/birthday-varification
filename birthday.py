from random import randrange
import re

class BirthdayVerification(object):

    def __init__(self, days=365, count=23):
        self.set(days, count)
        self.results = []

    def set(self, days, count):
        self.days = days
        self.count = count
        self.size = count

    def checkDuplicate(self, list):
        setLen = len(set(list))
        print('duplicated' if self.days != setLen else 'not duplicated')
        
    def __checkDuplicate(self, nums):
        self.results[-1]['days'] = self.days
        self.results[-1]['count'] = self.count
        reslist = list(set(nums))
        reslist.sort()
        self.results[-1]['reslist'] = reslist
        setLen = len(set(nums))
        self.results[-1]['hitCount'] = self.size - len(set(nums))
        self.results[-1]['duplicated'] = (self.size != setLen)

    def birthdayAttack(self, days, count):
        return [randrange(days) for _ in range(count)]

    def run(self):
        self.results.append({})
        result = self.birthdayAttack(self.days, self.count)
        result.sort()
        self.results[-1]['list'] = result
        self.__checkDuplicate(self.results[-1]['list'])
        print('duplicated' if self.results[-1]['duplicated'] else 'not duplicated')

    def log(self, num):
        print('-----------')
        print(re.sub(r' {16}', '','''attacked to {res[days]} ...
                {res[hitCount]} / {res[count]} hit
                {res[list]}
                {res[reslist]}
            '''.rstrip().format(res = self.results[num])))
        print('-----------')


if __name__ == '__main__':
    ba = BirthdayVerification(365, 23)
    ba.run()
    ba.log(0)