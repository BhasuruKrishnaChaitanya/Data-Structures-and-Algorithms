#https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, st: str) -> int:
        dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i=0
        s=0
        while i < len(st):
            if i+1 !=len(st) and dic.get(st[i]) < dic.get(st[i+1]):
                t = dic.get(st[i+1]) - dic.get(st[i])
                s += t
                i += 2
            else:
                s += dic.get(st[i])
                i += 1
        return s
