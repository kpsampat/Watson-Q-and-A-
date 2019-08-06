
import math
from collections import Counter
def get_cosine(vec1, vec2):
    common = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in common])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()]) 
    sum2 = sum([vec2[x]**2 for x in vec2.keys()]) 
    denominator = math.sqrt(sum1) * math.sqrt(sum2) 
    if not denominator:
        return 0.0 
    else:
        return float(numerator) / denominator
    
def text_to_vector(text): 
    word = text.lower()
    words = word.split()
    return Counter(words)

def text(text1,text2):
    vec1 = text_to_vector(text1)
    vec2 = text_to_vector(text2) 
    cosine = get_cosine(vec1, vec2)
    #print(cosine)
    return cosine
def main():
    with open('C:\\Users\\User\\Desktop\\user_input.txt', 'r') as file1:

        with open('C:\\Users\\User\\Desktop\\final_input.txt', 'r') as file2:

            for x in file1:
                #print(text1)
                pass
                for y in file2:
                    #print(text2)
                    break
            print(text(x,y))    
            return text(x,y)

main()






