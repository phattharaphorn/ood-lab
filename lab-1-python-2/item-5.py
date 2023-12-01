class TorKham :
    
    def __init__(self):
        self.words = []
    
    def restart(self):
       
        self.words = []
        return "game restarted";

    def play(self, word):
        
        if(word == "X"):
            return ""
        elif(len(self.words) == 0):
            self.words.append(word)
        else:
            lastWord = self.words[len(self.words)-1];
            if(lastWord[len(lastWord)-2:len(lastWord)].lower() != word[0:2].lower()):
                return "'" + word + "'" + "->" + "game over"
        
            else:
                self.words.append(word)
        ss = "["
        for i in range(len(self.words)):
                ss += "'" +self.words[i] + "'"
                if(i != len(self.words)-1):
                    ss += ", "
        ss += "]"
        return "'"+ word + "'" + "->" + ss;

torkham = TorKham()
print("*** TorKham HanSaa ***")
s = input("Enter Input : ").split(',')
for i in range(len(s)):
    if(s[i][0].islower()):
        print("'" + s[i] + "'" + "is Invalid Input !!!");
        exit();
    if(s[i][0] == "P"):
        print(torkham.play(s[i][2:]))
    if(s[i][0] == "R"):
        print(torkham.restart());
    if(s[i][0] == "X"):
        print(torkham.play(s[i][0]));