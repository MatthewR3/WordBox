import requests
import os
import ast
import random


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to WordBox. Ask for a synonym, an antonym, rhyme, definition, and more for a word by saying something like 'synonym for happy'. Hear all commands by saying 'all commands'."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Ask for a synonym, antonym, part of speech, rhyme, definition, syllables, frequency, or pronunciation!"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

def get_all_commands():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "All Commands"
    speech_output = "You can ask for a synonym, antonym, rhyme, definition, part of speech, syllables, or frequency of a word by saying something like 'synonym for happy'. You can also ask for a random synonym, antonym, definition, or rhyme by saying something like 'random synonym for happy'. If you want all of them, say something like 'all synonyms for happy.'"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Ask for a synonym, antonym, part of speech, rhyme, definition, syllables, or frequency of a word! Or say 'all commands' to get hear all commands."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Bye!"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def get_synonym(intent, session):
    if "value" not in intent["slots"]["WORD"]:
        response = build_speechlet_response("Synonym", "Sorry, I couldn't recognize that word.", None, True)
        return build_response({}, response)
    word = intent["slots"]["WORD"]["value"]
    print("---GETTING SYNONYM OF " + word)
    url = "https://wordsapiv1.p.mashape.com/words/" + word + "/synonyms"
    headers = {
        "X-Mashape-Key": os.environ["MASHAPE_KEY_PRODUCTION"],
        "Accept": "application/json"
    }
    r = requests.get(url, headers = headers)
    if len(ast.literal_eval(r.text)["synonyms"]) == 0:
        speech_output =  "Sorry, I couldn't find any synonyms for " + word + "."
    else:
        speech_output = "A common synonym for " + word + " is " + ast.literal_eval(r.text)["synonyms"][0] + "."
    response = build_speechlet_response("Synonym", speech_output, None, True)
    return build_response({}, response)

def get_random_synonym(intent, session):
    if "value" not in intent["slots"]["WORD"]:
        response = build_speechlet_response("Synonym", "Sorry, I couldn't recognize that word.", None, True)
        return build_response({}, response)
    word = intent["slots"]["WORD"]["value"]
    print("---GETTING RANDOM SYNONYM OF " + word)
    url = "https://wordsapiv1.p.mashape.com/words/" + word + "/synonyms"
    headers = {
        "X-Mashape-Key": os.environ["MASHAPE_KEY_PRODUCTION"],
        "Accept": "application/json"
    }
    r = requests.get(url, headers = headers)
    if len(ast.literal_eval(r.text)["synonyms"]) == 0:
        speech_output =  "Sorry, I couldn't find any synonyms for " + word + "."
    else:
        speech_output = "A synonym for " + word + " is " + random.choice(ast.literal_eval(r.text)["synonyms"]) + "."
    response = build_speechlet_response("Synonym", speech_output, None, True)
    return build_response({}, response)

def get_all_synonyms(intent, session):
    if "value" not in intent["slots"]["WORD"]:
        response = build_speechlet_response("Synonyms", "Sorry, I couldn't recognize that word.", None, True)
        return build_response({}, response)
    word = intent["slots"]["WORD"]["value"]
    print("---GETTING ALL SYNONYMS OF " + word)
    url = "https://wordsapiv1.p.mashape.com/words/" + word + "/synonyms"
    headers = {
        "X-Mashape-Key": os.environ["MASHAPE_KEY_PRODUCTION"],
        "Accept": "application/json"
    }
    r = requests.get(url, headers = headers)
    synonyms_list = ast.literal_eval(r.text)["synonyms"]
    if len(synonyms_list) == 0:
        speech_output =  "Sorry, I couldn't find any synonyms for " + word + "."
    elif len(synonyms_list) == 1:
        speech_output = "The only synonym for " + word + " is " +  synonyms_list[0] + "."
    else:
        speech_output = "The synonyms for " + word + " are " + ", ".join([synonym for synonym in synonyms_list[:-1]]) + ", and " + synonyms_list[-1] + "."
    response = build_speechlet_response("Synonyms", speech_output, None, True)
    return build_response({}, response)

def get_antonym(intent, session):
    if "value" not in intent["slots"]["WORD"]:
        response = build_speechlet_response("Antonym", "Sorry, I couldn't recognize that word.", None, True)
        return build_response({}, response)
    word = intent["slots"]["WORD"]["value"]
    print("---GETTING ANTONYM OF " + word)
    url = "https://wordsapiv1.p.mashape.com/words/" + word + "/antonyms"
    headers = {
        "X-Mashape-Key": os.environ["MASHAPE_KEY_PRODUCTION"],
        "Accept": "application/json"
    }
    r = requests.get(url, headers = headers)
    if len(ast.literal_eval(r.text)["antonyms"]) == 0:
        speech_output = "Sorry, I couldn't find any antonyms for " + word + "."
    else:
        speech_output = "A common antonym for " + word + " is " + ast.literal_eval(r.text)["antonyms"][0] + "."
    response = build_speechlet_response("Antonym", speech_output, None, True)
    return build_response({}, response)

def get_random_antonym(intent, session):
    if "value" not in intent["slots"]["WORD"]:
        response = build_speechlet_response("Antonym", "Sorry, I couldn't recognize that word.", None, True)
        return build_response({}, response)
    word = intent["slots"]["WORD"]["value"]
    print("---GETTING RANDOM ANTONYM OF " + word)
    url = "https://wordsapiv1.p.mashape.com/words/" + word + "/antonyms"
    headers = {
        "X-Mashape-Key": os.environ["MASHAPE_KEY_PRODUCTION"],
        "Accept": "application/json"
    }
    r = requests.get(url, headers = headers)
    if len(ast.literal_eval(r.text)["antonyms"]) == 0:
        speech_output = "Sorry, I couldn't find any antonyms for " + word + "."
    else:
        speech_output = "An antonym for " + word + " is " + random.choice(ast.literal_eval(r.text)["antonyms"]) + "."
    response = build_speechlet_response("Antonym", speech_output, None, True)
    return build_response({}, response)

def get_all_antonyms(intent, session):
    if "value" not in intent["slots"]["WORD"]:
        response = build_speechlet_response("Antonyms", "Sorry, I couldn't recognize that word.", None, True)
        return build_response({}, response)
    word = intent["slots"]["WORD"]["value"]
    print("---GETTING ALL ANTONYMS OF " + word)
    url = "https://wordsapiv1.p.mashape.com/words/" + word + "/antonyms"
    headers = {
        "X-Mashape-Key": os.environ["MASHAPE_KEY_PRODUCTION"],
        "Accept": "application/json"
    }
    r = requests.get(url, headers = headers)
    antonyms_list = ast.literal_eval(r.text)["antonyms"]
    if len(antonyms_list) == 0:
        speech_output = "Sorry, I couldn't find any antonyms for " + word + "."
    elif len(antonyms_list) == 1:
        speech_output = "The only antonym for " + word + " is " +  antonyms_list[0] + "."
    else:
        speech_output = "The antonyms for " + word + " are " + ", ".join([antonym for antonym in antonyms_list[:-1]]) + ", and " + antonyms_list[-1] + "."
    response = build_speechlet_response("Antonyms", speech_output, None, True)
    return build_response({}, response)

def get_pos(intent, session):
    if "value" not in intent["slots"]["WORD"]:
        response = build_speechlet_response("Part of Speech", "Sorry, I couldn't recognize that word.", None, True)
        return build_response({}, response)
    word = intent["slots"]["WORD"]["value"]
    print("---GETTING PART OF SPEECH OF " + word)
    url = "https://wordsapiv1.p.mashape.com/words/" + word
    headers = {
        "X-Mashape-Key": os.environ["MASHAPE_KEY_PRODUCTION"],
        "Accept": "application/json"
    }
    r = requests.get(url, headers = headers)
    speech_output = word + " is a " + ast.literal_eval(r.text)["results"][0]["partOfSpeech"] + "."
    response = build_speechlet_response("Part of Speech", speech_output, None, True)
    return build_response({}, response)

def get_rhyme(intent, session):
    if "value" not in intent["slots"]["WORD"]:
        response = build_speechlet_response("Rhyme", "Sorry, I couldn't recognize that word.", None, True)
        return build_response({}, response)
    word = intent["slots"]["WORD"]["value"]
    print("---GETTING RHYME OF " + word)
    url = "https://wordsapiv1.p.mashape.com/words/" + word + "/rhymes"
    headers = {
        "X-Mashape-Key": os.environ["MASHAPE_KEY_PRODUCTION"],
        "Accept": "application/json"
    }
    r = requests.get(url, headers = headers)
    if len(ast.literal_eval(r.text)["rhymes"]) == 0:
        speech_output = "Sorry, I couldn't find anything that rhymes with " + word + "."
    else:
        speech_output = "A common rhyme for " + word + " is " + ast.literal_eval(r.text)["rhymes"]["all"][0] + "."
    response = build_speechlet_response("Rhyme", speech_output, None, True)
    return build_response({}, response)

def get_random_rhyme(intent, session):
    if "value" not in intent["slots"]["WORD"]:
        response = build_speechlet_response("Rhyme", "Sorry, I couldn't recognize that word.", None, True)
        return build_response({}, response)
    word = intent["slots"]["WORD"]["value"]
    print("---GETTING RANDOM RHYME OF " + word)
    url = "https://wordsapiv1.p.mashape.com/words/" + word + "/rhymes"
    headers = {
        "X-Mashape-Key": os.environ["MASHAPE_KEY_PRODUCTION"],
        "Accept": "application/json"
    }
    r = requests.get(url, headers = headers)
    if len(ast.literal_eval(r.text)["rhymes"]) == 0:
        speech_output = "Sorry, I couldn't find anything that rhymes with " + word + "."
    else:
        speech_output = "A rhyme for " + word + " is " + random.choice(ast.literal_eval(r.text)["rhymes"]["all"]) + "."
    response = build_speechlet_response("Rhyme", speech_output, None, True)
    return build_response({}, response)

def get_definition(intent, session):
    if "value" not in intent["slots"]["WORD"]:
        response = build_speechlet_response("Definition", "Sorry, I couldn't recognize that word.", None, True)
        return build_response({}, response)
    word = intent["slots"]["WORD"]["value"]
    print("---GETTING DEFINITION OF " + word)
    url = "https://wordsapiv1.p.mashape.com/words/" + word + "/definitions"
    headers = {
        "X-Mashape-Key": os.environ["MASHAPE_KEY_PRODUCTION"],
        "Accept": "application/json"
    }
    r = requests.get(url, headers = headers)
    if len(ast.literal_eval(r.text)["definitions"]) == 0:
        speech_output = "Sorry, I couldn't find any definitions for " + word + "."
    else:
        speech_output = "The most popular definition for " + word + " is " + ast.literal_eval(r.text)["definitions"][0]["definition"] + "."
    response = build_speechlet_response("Definition", speech_output, None, True)
    return build_response({}, response)

def get_random_definition(intent, session):
    if "value" not in intent["slots"]["WORD"]:
        response = build_speechlet_response("Definition", "Sorry, I couldn't recognize that word.", None, True)
        return build_response({}, response)
    word = intent["slots"]["WORD"]["value"]
    print("---GETTING RANDOM DEFINITION OF " + word)
    url = "https://wordsapiv1.p.mashape.com/words/" + word + "/definitions"
    headers = {
        "X-Mashape-Key": os.environ["MASHAPE_KEY_PRODUCTION"],
        "Accept": "application/json"
    }
    r = requests.get(url, headers = headers)
    if len(ast.literal_eval(r.text)["definitions"]) == 0:
        speech_output = "Sorry, I couldn't find any definitions for " + word + "."
    else:
        speech_output = "A definition for " + word + " is " + random.choice(ast.literal_eval(r.text)["definitions"])["definition"] + "."
    response = build_speechlet_response("Definition", speech_output, None, True)
    return build_response({}, response)

def get_all_definitions(intent, session):
    if "value" not in intent["slots"]["WORD"]:
        response = build_speechlet_response("Definitions", "Sorry, I couldn't recognize that word.", None, True)
        return build_response({}, response)
    word = intent["slots"]["WORD"]["value"]
    print("---GETTING ALL DEFINITIONS OF " + word)
    url = "https://wordsapiv1.p.mashape.com/words/" + word + "/definitions"
    headers = {
        "X-Mashape-Key": os.environ["MASHAPE_KEY_PRODUCTION"],
        "Accept": "application/json"
    }
    r = requests.get(url, headers = headers)
    definitions_list = ast.literal_eval(r.text)["definitions"]
    if len(definitions_list) == 0:
        speech_output = "Sorry, I couldn't find any definitions for " + word + "."
    elif len(definitions_list) == 1:
        speech_output = "The only definition for " + word + " is " +  definitions_list[0] + "."
    else:
        speech_output = word + " has " + str(len(definitions_list)) + " definitions. It could mean " + ", ".join([definition["definition"] for definition in definitions_list[:-1]]) + ", or " + definitions_list[-1]["definition"] + "."
    response = build_speechlet_response("Definitions", speech_output, None, True)
    return build_response({}, response)

def get_syllables(intent, session):
    if "value" not in intent["slots"]["WORD"]:
        response = build_speechlet_response("Syllables", "Sorry, I couldn't recognize that word.", None, True)
        return build_response({}, response)
    word = intent["slots"]["WORD"]["value"]
    print("---GETTING SYLLABLES OF " + word)
    url = "https://wordsapiv1.p.mashape.com/words/" + word + "/syllables"
    headers = {
        "X-Mashape-Key": os.environ["MASHAPE_KEY_PRODUCTION"],
        "Accept": "application/json"
    }
    r = requests.get(url, headers = headers)
    if not ast.literal_eval(r.text)["syllables"]:
        speech_output = "Sorry, I couldn't find any syllables for " + word + "."
    else:
        speech_output = "There are " + str(ast.literal_eval(r.text)["syllables"]["count"]) + " syllables in " + word + ". They are: " + ", ".join(ast.literal_eval(r.text)["syllables"]["list"]) + "."
    response = build_speechlet_response("Syllables", speech_output, None, True)
    return build_response({}, response)

# NOTE: Not used in production
def get_pronunciation(intent, session):
    if "value" not in intent["slots"]["WORD"]:
        response = build_speechlet_response("Pronunciation", "Sorry, I couldn't recognize that word.", None, True)
        return build_response({}, response)
    word = intent["slots"]["WORD"]["value"]
    print("---GETTING PRONUNCIATION OF " + word)
    url = "https://wordsapiv1.p.mashape.com/words/" + word + "/pronunciation"
    headers = {
        "X-Mashape-Key": os.environ["MASHAPE_KEY_PRODUCTION"],
        "Accept": "application/json"
    }
    r = requests.get(url, headers = headers)
    if not ast.literal_eval(r.text)["pronunciation"]:
        speech_output = "Sorry, I couldn't find any pronunications for " + word + "."
    # Only one pronunciation
    if len(ast.literal_eval(r.text)["pronunciation"]) == 1:
        speech_output = "You can pronounce " + word + " as " + ast.literal_eval(r.text)["pronunciation"]["all"] + "."
    # Multiple pronunications
    elif len(ast.literal_eval(r.text)["pronunciation"]) > 1:
        speech_output = "".join([(("As a" + ("n " if key in ["adjective", "adverb"] else " ") + key + " it's pronounced as " + value + ". ") if key != "all" else "") for key, value in ast.literal_eval(r.text)["pronunciation"].items()])
    response = build_speechlet_response("Pronunciation", speech_output, None, True)
    return build_response({}, response)

def get_frequency(intent, session):
    if "value" not in intent["slots"]["WORD"]:
        response = build_speechlet_response("Frequency", "Sorry, I couldn't recognize that word.", None, True)
        return build_response({}, response)
    word = intent["slots"]["WORD"]["value"]
    print("---GETTING FREQUENCY OF " + word)
    url = "https://wordsapiv1.p.mashape.com/words/" + word + "/frequency"
    headers = {
        "X-Mashape-Key": os.environ["MASHAPE_KEY_PRODUCTION"],
        "Accept": "application/json"
    }
    r = requests.get(url, headers = headers)
    if not ast.literal_eval(r.text)["frequency"]:
        speech_output = "Sorry, I couldn't find the frequency of " + word + "."
    else:
        speech_output = word + " is used about " + str(int(ast.literal_eval(r.text)["frequency"]["perMillion"])) + " times per million words in writing."
    response = build_speechlet_response("Frequency", speech_output, None, True)
    return build_response({}, response)


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    print("---INTENT: " + intent_name)

    # Dispatch to your skill's intent handlers
    try:
        if intent_name == "GetSynonymIntent":
            return get_synonym(intent, session)
        elif intent_name == "GetRandomSynonymIntent":
            return get_random_synonym(intent, session)
        elif intent_name == "GetAllSynonymsIntent":
            return get_all_synonyms(intent, session)
        elif intent_name == "GetAntonymIntent":
            return get_antonym(intent, session)
        elif intent_name == "GetRandomAntonymIntent":
            return get_random_antonym(intent, session)
        elif intent_name == "GetAllAntonymsIntent":
            return get_all_antonyms(intent, session)
        elif intent_name == "GetPOSIntent":
            return get_pos(intent, session)
        elif intent_name == "GetRhymeIntent":
            return get_rhyme(intent, session)
        elif intent_name == "GetRandomRhymeIntent":
            return get_random_rhyme(intent, session)
        elif intent_name == "GetDefinitionIntent":
            return get_definition(intent, session)
        elif intent_name == "GetRandomDefinitionIntent":
            return get_random_definition(intent, session)
        elif intent_name == "GetAllDefinitionsIntent":
            return get_all_definitions(intent, session)
        elif intent_name == "GetSyllablesIntent":
            return get_syllables(intent, session)
        elif intent_name == "GetFrequencyIntent":
            return get_frequency(intent, session)
        elif intent_name == "GetPronunciationIntent":
            return get_pronunciation(intent, session)
        elif intent_name == "GetAllCommandsIntent":
            return get_all_commands()
        elif intent_name == "AMAZON.HelpIntent":
            return get_welcome_response()
        elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
            return handle_session_end_request()
        else:
            response = build_speechlet_response("Error", "Sorry, I don't know that command. I can find definitions, synonyms, antonyms, and more if you say something like 'a synonym for happy'.", None, True)
            return build_response({}, response)

    except:
        response = build_speechlet_response("Error", "Sorry, I don't know that word!", None, True)
        return build_response({}, response)


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" + event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']}, event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
