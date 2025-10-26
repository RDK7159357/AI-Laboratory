from nltk.stem import PorterStemmer, LancasterStemmer
from nltk.stem import SnowballStemmer

words = ['running', 'runs', 'ran', 'easily', 'fairly', 'playing', 'played', 
         'player', 'connection', 'connections', 'connecting', 'connected']

ps = PorterStemmer()
ls = LancasterStemmer()
ss = SnowballStemmer('english')

print("Stemming Results:")
print(f"{'Word':<15} {'Porter':<12} {'Lancaster':<12} {'Snowball':<12}")
print("-" * 55)

for word in words:
    print(f"{word:<15} {ps.stem(word):<12} {ls.stem(word):<12} {ss.stem(word):<12}")
