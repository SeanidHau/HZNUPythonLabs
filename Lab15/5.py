# 以下答案不会在学校OJ上通过 但是代码及结果是正确的 个人写时可以稍加修改
# 可以参考https://blog.csdn.net/Lumos427/article/details/125162768?spm=1001.2014.3001.5501
import re
from collections import Counter

def count_words(filename) :
    with open(filename, "r") as file :
        text = file.read()
        
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(10)
    
    for word, count in most_common_words :
        print(f"{word}\t{count}")
        
        
def main() :
    filename = "lincoln.txt"
    count_words(filename)
    
    
if __name__ == "__main__" :
    main()