import json
from tqdm import tqdm
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

nltk.download('punkt')
nltk.download('stopwords')
data_file = "data/final_data_new.json"
output_file = "data/cleaned_steam.json"
require = ['developer', 'publisher', 'desc', 'requirements', 'popu_tags', 'name', 'type']
stop_words = set(stopwords.words('english'))
 
with open(data_file) as f:
    data = json.load(f)
results = []
for game in tqdm(data):
    if game.get('full_desc') is None:
        continue
    filtered_sentence = []
    try:
        for w in word_tokenize(game['full_desc'].get('desc', '')):
            w = w.lower()
            if w in string.punctuation:
                continue
            if not w in stop_words:
                filtered_sentence.append(w)
        game['desc'] = ' '.join(filtered_sentence)
        game['type'] = game['full_desc'].get('sort', '')
        if len(game['name']) ==0 or len(game['desc'])==0:
            print(game)
    except Exception as e:
        print(f"Error: {e}")
        print(game)
        break

    for key in set(game.keys()):
        if key not in require:
            del game[key]
    results.append(game)
    
with open(output_file, 'w') as output_f:
    json.dump(results, output_f, indent=2)
