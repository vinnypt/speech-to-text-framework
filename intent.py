import spacy

nlp = spacy.load("en_core_web_sm")

def get_intent(command):
    doc = nlp(command.lower())
    lemmas = [token.lemma_ for token in doc]

    if "light" in lemmas and "on" in lemmas:
        return "lights_on"
    if "light" in lemmas and "off" in lemmas:
        return "lights_off"
    if "weather" in lemmas:
        return "weather"
    if "music" in lemmas or ("play" in lemmas and "song" in lemmas):
        return "music"
    return None