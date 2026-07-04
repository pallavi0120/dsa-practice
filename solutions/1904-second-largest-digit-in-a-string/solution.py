class Solution:
    def secondHighest(self, s: str) -> int:
        largest=-1
        second_largest=-1
        for i in s:
            if i.isdigit():
                if int(i)>largest:
                    second_largest=largest
                    largest=int(i)
                elif int(i)>second_largest and int(i)<largest:
                    second_largest=int(i)
        return second_largest
