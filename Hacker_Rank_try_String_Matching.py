def ApproximateMatcher(text,PrefixString,SuffixString):
    prefstr = ""
    suffstr = ""
    brk_yn = False
    ls_text = list(text)
    ls_prf  = list(PrefixString)
    ls_suff = list(SuffixString)
#KMP algorithm used to match strings
    #print(ls_text)
    for i in range(0,len(ls_text)):
        #print(i)
        for j in range(0,len(ls_prf)):
            #print(j)
            if ls_text[i] == ls_prf[j]:
                prefstr = prefstr + ls_prf[j]
                i = i + 1
            else:
                brk_yn = True
                break
        if brk_yn:
            break

    for i in range(0,len(ls_suff)):
        for j in range(0,len(ls_text)):
            if ls_suff[i] == ls_text[j]:
                suffstr = suffstr + ls_suff[i]
                i += 1
            else:
                i = 0
            if len(ls_suff) == i:
                brk_yn = True
                break
        if brk_yn:
            break
    return prefstr + suffstr

if __name__ == "__main__":
    print(ApproximateMatcher("nothing","notall","hingenius"))
