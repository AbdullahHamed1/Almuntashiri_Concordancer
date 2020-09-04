"""

@author: abdullah Almuntashiri
University of Leeds
"""


# Reading files libraries
from os import listdir 
from os.path import isdir, join 
import xml.etree.ElementTree as et # To read and manipulate XML files and Parsing XML Data
import re # For Regular expression
import json # To save files in json formate
# For Natural language processing (NLP)
from nltk.tokenize import WordPunctTokenizer # To break sentences into words 
from nltk.tokenize import sent_tokenize # To break paragraphs into sentences 
from nltk.stem.isri import ISRIStemmer # To get the root of  words
from termcolor import colored





doc_list = [] # It will contain list of all files that we have in our database
word_occurances = {} #our dic which contains keys (words) and values (list of sentences that have the words).
forms_dict = {} # it will contain keys (words) and values (list of words that are from the same root in our files).
arabic_diacritics = re.compile("""
                      ّ    | # Tashdid
                      َّ    | # Fatha
                      ً    | # Tanwin Fath
                      ُ    | # Damma
                      ٌ    | # Tanwin Damm
                      ِ    | # Kasra
                      ٍ    | # Tanwin Kasr
                      ْ    | # Sukun
                     ـ     # Tatwil/Kashida
                       """, re.VERBOSE) # To define the Arabic diacritics 


def build_all_paths_list(dir_name): # To build list of paths
    paths_list = []
    
    all_sub_dir = listdir(dir_name) # To get list of all sub directory 
    
    for sub_dir in all_sub_dir: # To get the directories that are inside the sub directories
        base_path = join(dir_name, sub_dir) # integration function to access the files
        if isdir(base_path): # To check if it directory or not
           for file_name in listdir(base_path): # To get the files' names inside the directory
             if not file_name.startswith("."):
              paths_list.append(join(base_path, file_name))
    return paths_list


def parse_XML(xml_file):
    doc = {} # To save the extracted information from the files
    try:
         xtree = et.parse(xml_file)
         xroot = xtree.getroot() #To get the first tag in our root
    
         doc["name"] = xroot.find("teiHeader").attrib.get("id")
         doc["domain"] = re.split(r"[/\\]", xml_file)[-2]
         
    
         
         doc["sentences"] = [] #To get a list of  all sentences in each file
         for p in xroot.findall(".//body//p"):
             if p.text != None: #  To make sure that P is not empty 
               text = p.text.strip() # To remove the extra spaces
               text = re.sub(arabic_diacritics, "", text) # To exchange arabic_diacritics into empty (Delete)
               text = re.sub(r"(\s)\1+", r"\1", text)  # To remove all repeated spaces
               sentences = sent_tokenize(text.replace("؟", "?")) #To break the paragraph into sentences. and convert the question mark from arabi
               for i, sentence in enumerate (sentences): 
                 sentences[i] =re.sub(r'[^\u0600-\u06FF\s]', '', sentence).strip() #To exchange anything is not aranic into empty (Delete)
               doc["sentences"].extend(sentences)
    except Exception as ex:
        print(ex)
        print(xml_file)


    return doc

def build_all_docs_list(dir_name): # To build our doc list
    paths = build_all_paths_list(dir_name) # Call build_all_paths_list fuction to build list of paths

    for path in paths:
      if path.endswith(".xml"): # To access to XML files 
        doc = parse_XML(path) # Call parse_XML function.
        doc_list.append(doc)

def extract_words():

  st = ISRIStemmer() # To get the root of the words
  tk = WordPunctTokenizer() # To break sentences into words 

  for doc in doc_list: 
      for sentence in doc["sentences"]: # To access to the sentences in each doc
          words = {word for word in tk.tokenize (sentence) if word.isalpha()} # To breake the sent. into words, if the word is Alphabet. 
          

          
          for word in words: 
              if st.stem(word) in forms_dict: # To get and check if the root of the word is in the directory.
                  forms_dict[st.stem(word)].add(word) # Add the word to the list of words that are from the same root
              else:
                  forms_dict[st.stem(word)] = {word} # Add the word (root) to the new list 
                  
              if word in word_occurances: # To check if the word is from the words that are in the sentences
                   word_occurances[word].append((sentence, doc["domain"]))  # Add the sentence that include the word to the list
              else:
                   word_occurances[word] = [(sentence, doc["domain"])] # Add the sentence that include the word to new list
                       
  return word_occurances

  
def save_all_wordsـjson(): #Save list of words in JSON formate
   with open ("words.json", "w", encoding='utf8') as file:
    json.dump(list(word_occurances.keys()), file, ensure_ascii=False)
    
    

def save_all_words_txt(): #Save list of words in TXT formate
   with open ("words.txt", "w") as file:
    for word in word_occurances:
      file.write(word + "\n")
      
      

def fine_sentences (word): # To present the whole sentence
   st = ISRIStemmer()
   word = st.stem(word)
   
   sentences = set() 
   if word in word_occurances: 
      for sent in word_occurances[word]:
          sentences.add(sent)
          print(sent)
          print("--" * 100)

   return list(sentences)


def find_part_of_sentence(word):
   st = ISRIStemmer() # To get the root of the words
   tk = WordPunctTokenizer() # To break sentences into words 

   
   quots = set() # Creating a set of sentences that include the word that entered.
   if word in word_occurances: # To of the word is on the corpus 
     for i, oocur in enumerate (word_occurances[word]): # for each sentence in word_occurances dict
         sentence, domain = oocur  
         words_bag = [token for token in tk.tokenize(sentence)] # To convert the sentences to words, in order to find its index
         idx = words_bag.index(word) # To reture the index of the word.
         print("                             "f"[{i+1}]", end="") # Print the onther form of the words
         print()
         print()
         print("The domain of the concordance is : ", colored(domain, "magenta"))
         print(end="\t")
         quot = ""

         if idx>= 8:
             
             for token in tk.tokenize(sentence)[idx - 8: idx + 8]:
                
                 if token == word:
                      print(colored(token, "cyan"), end=" ")
                 else:
                     print (token, end=" ")
                 quot += token + " "
         else:
             for token in tk.tokenize(sentence)[: idx + 8]:
                 if token == word:
                     print(colored(token, "cyan"), end=" ")
                 else:
                     print (token, end=" ")
                     
                 quot += token + " "
                     
                     
         quots.add((domain, quot))
         
         print()
         print()
         print("--" * 69)
     print_other_forms(word) # To call the root fuction
         
   else:
         print("   لا توجد أمثلة لهذه الكلمه ",  " \n There is on concordances for this word") 
         
   
   return list(quots)  



def print_other_forms(word):
    st = ISRIStemmer()
    
    
    root = st.stem(word) 
   # print ("The root of " + word + " is"+ root)
    print()
    print()
    print ("  ","جذر كلمة " + word+ " هو : "+ colored(root, "white"))
    print ("  ","The root of  " + word+ " is : "+ colored(root, "white"))
    
    if root in forms_dict:
        print("\n\n\n   أشكال أخرى لكلمات من نفس الجذر", "\n Other forms of the words : ", )
        
        for i, form in enumerate(forms_dict[root]): # for each root of words in forms_dict
            print("  "f"]{i+1}[ {form:20s}", end="") # Print the onther form of the words
            if (i+1) % 4 == 0:
                print()
        return [root] + list (forms_dict[root])
    else:
         print ("\n There is no other forms")
         
     

#build_all_docs_list("resources") # To call the function and give the folder that have the files
#extract_words() # To call the function to extract the words from doc list
#save_all_wordsـjson()
#save_all_words_txt()


#while True: # Loop
# word = input (" Entre a word, or (e) to exit: ")
# print()
# print("--- %s seconds ---" % (time.time() - start_time))
# if word == 'e': # break the loop.
#     print ("\n Thank you .")
#     break
     
# result = find_part_of_sentence(word)
