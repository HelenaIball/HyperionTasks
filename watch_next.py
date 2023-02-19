#import spacy and the NLP model
import spacy
nlp = spacy.load('en_core_web_md')

#set variables for the desription and a blank list of similarities
planet_Hulk_description = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'
similarities_list = []

#define a function that outputs the most similar film
def find_common_film(description):
    model_sentence = nlp(description)
    #open and read the movies file
    movies = open('movies.txt', 'r')
    #determine similarity of each line and add to the list
    for line in movies:
        similarity = nlp(line).similarity(model_sentence)
        similarities_list.append(similarity)
    #find the index of the highest similarity
    max_index = similarities_list.index(min(similarities_list))

    #read the file again and identify the line corresponding to the maximum similarity
    movies.seek(0)
    movies_read = movies.readlines()
    common_film = movies_read[max_index-1]
    #split the line at the colon to identify just the title
    common_film_split = common_film.split(':')
    #print the result of the most similar movie
    print(f'Based on the description of Planet Hulk, {common_film_split[0]} is the most similar movie from our list that you might enjoy.' )

#call on the function using the planet Hulk description
find_common_film(planet_Hulk_description)