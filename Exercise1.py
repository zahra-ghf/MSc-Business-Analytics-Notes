
def isPalindrome(s, start, end) :
    if start<0 or end>=len(s) or start>end :
        raise Exception("Error : start<0 or end>=len(s) or start>end")
    else:
        i=start
        j=end
        while i<j :
            if s[i]!=s[j] :
                return False

            i+=1
            j-=1

        return True

def main() :
    s="abcdeffedcquipopz"

    print("isPalindrome(\"" + s +"\", start=" + str(5) +", end=" + str(6) +") = ", isPalindrome(s, start=5, end=6))
    print("isPalindrome(\"" + s +"\", start=" + str(13) +", end=" + str(15) +") = ", isPalindrome(s, start=13, end=15))
    print("isPalindrome(\"" + s +"\", start=" + str(3) +", end=" + str(8) +") = ", isPalindrome(s, start=3, end=8))
    print("isPalindrome(\"" + s +"\", start=" + str(2) +", end=" + str(4) +") = ", isPalindrome(s, start=2, end=4))
    print("isPalindrome(\"" + s +"\", start=" + str(3) +", end=" + str(9) +") = ", isPalindrome(s, start=3, end=9))

if __name__=="__main__" :
    main()
