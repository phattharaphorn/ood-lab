class translator:

   symbol = ('I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M')
   number = (1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000)

   def deciToRoman(self, num):
      i = 12
      str = ''
      while num :
         div = num // self.number[i]
         num %= self.number[i]

         while div :
            str += self.symbol[i]
            div -= 1
         i -= 1
      return str

   def romanToDeci(self, s):
      roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
      i = 0
      num = 0
      while i < len(s):
         if i + 1 < len(s) and s[i:i+2] in roman:
            num += roman[s[i:i+2]]
            i += 2
         else:
            num += roman[s[i]]
            i += 1
      return num

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))
print(translator().romanToDeci(translator().deciToRoman(num)))