class Solution:
    def intToRoman(self, num: int) -> str:
        out = ""
        ky =["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        val=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        for i in range(13):
            if num//val[i]>=0:
                out +=ky[i]*((num)//val[i])
                num=num%val[i]

        return out 
            
