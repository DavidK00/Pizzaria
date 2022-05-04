def main():
    text = open('book of John text.txt', 'r')
    word_counter = {}
    
    for line in text:
        line = line.strip()
        words = line.split(" ")
        
        for i in words:
            if i in word_counter:
                word_counter[i] = word_counter[i] + 1
            else:
                word_counter[i] = 1
    print(word_counter)
    
main()