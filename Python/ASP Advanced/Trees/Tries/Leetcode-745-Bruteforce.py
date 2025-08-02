class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words

    def f(self, pref: str, suff: str) -> int:
        for i in range(len(self.words) - 1, -1, -1):
            w = self.words[i]
            if len(w) < len(pref) or len(w) < len(suff):
                continue

            j, flag = 0, True
            for c in pref:
                if w[j] != c:
                    flag = False
                    break
                j += 1
            
            if not flag:
                continue

            j = len(w) - len(suff)
            for c in suff:
                if w[j] != c:
                    flag = False
                    break
                j += 1
            
            if flag:
                return i
        
        return -1