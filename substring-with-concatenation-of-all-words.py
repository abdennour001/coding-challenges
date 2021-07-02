class Solution(object):
    @staticmethod
    def findSubstring(s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from itertools import permutations, combinations_with_replacement, combinations
        import re

        # print(len(words))
        # for word in words:
        #     if s.find(word) == -1:
        #         print(word)
        #         words.remove(word)
        # print(len(words))
        # combs = list(permutations(words, 7))
        res = []
        len_words = len("".join(words))
        for i in range(len(s)):
            if i+len_words > len(s):
                break
            s_ = s[i:i+len_words]
            curr_len = 0
            prev_len = -1
            words_ = [w for w in words]
            while curr_len <= len_words and prev_len != curr_len:
                prev_len = curr_len
                for word in words_:
                    if s_[curr_len:curr_len+len(word)] == word:
                        print(i, word, curr_len, s_[curr_len:curr_len+len(word)], words_)
                        words_.remove(word)
                        curr_len += len(word)
                        break
            if curr_len == len_words:
                res.append(i)
            # if all([ True if s[i:i+len_words].find(word) >= 0 else False for word in words ]):
            #     res.append(i)
        # for _ in combs[0:2]:
        #     comb = "".join(_)
        #     res += [m.start() for m in re.finditer(f'(?=({comb}))', s)]
            # match = re.search(fr"(?={comb})", s)
            # s_ = s
            # prev_len = 0
            # while match:
            #     print(match)
            #     res.append(match.start()+prev_len)
            #     s_ = s_[match.end():]
            #     prev_len = len(s) - len(s_)
            #     match = re.search(fr"(?={comb})", s_)
        return sorted(list(set(res)))
        # return []


if __name__ == "__main__":
    # print(Solution.findSubstring(
    #     "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel", ["dhvf", "sind", "ffsl", "yekr", "zwzq", "kpeo", "cila", "tfty", "modg", "ztjg", "ybty", "heqg", "cpwo", "gdcj", "lnle", "sefg", "vimw", "bxcb"]))

    print(Solution.findSubstring(
        "barfoothefoobarman", ["foo","bar"]))
