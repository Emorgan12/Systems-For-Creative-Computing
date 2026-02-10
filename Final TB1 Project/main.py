import requests
from bs4 import BeautifulSoup
import markovify
import os

with open('lyrics.txt', 'w', encoding='utf-8', errors='ignore') as f:
    f.write('')
# URLs of the target websites
songs = [
    'https://www.azlyrics.com/lyrics/taylorswift/alltoowell.html',
    'https://www.azlyrics.com/lyrics/taylorswift/lovestory.html',
    'https://www.azlyrics.com/lyrics/taylorswift/youbelongwithme.html'
    ]
# Send a GET request to the website
for url in songs:
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        print('Successfully fetched the webpage!')
    else:
        print('Failed to retrieve the page')

    soup = BeautifulSoup(response.text, 'html.parser')

    # AI-Assisted coding used for extraction of lyrics
    div_texts = [d.get_text(separator='\n').strip() for d in soup.find_all('div') if not d.attrs]
    lyrics = ''.join(div_texts).strip()

    # Save the lyrics to a text file (use UTF-8 and skip characters that can't be written)
    with open('lyrics.txt', 'a', encoding='utf-8', errors='ignore') as f:
        lyrics = os.linesep.join([s for s in lyrics.splitlines() if s])
        f.writelines(lyrics)

# Read the lyrics from the file (use UTF-8 and ignore any bad bytes)
with open('lyrics.txt', encoding='utf-8', errors='ignore') as f:
    text = f.read()

textmodel = markovify.Text(text, state_size=1)
for i in range(5):
    print(textmodel.make_short_sentence(200))