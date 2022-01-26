class Solution(object):
    def sortSentence(self, s):
        words=""
        sentence=s.split(" ")
        sorted_sentence=[0 for i in range(len(sentence))]
        for i in range(len(sentence)):
            current_word=sentence[i]
            for word in sentence[i]:
                if(word!=current_word[-1]):
                    words+=word
                else:
                    x=int(word)-1
                    sorted_sentence[x]=words
            
            words=""
        return " ".join(sorted_sentence)
        
