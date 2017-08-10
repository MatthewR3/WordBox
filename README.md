# WordBox

WordBox is a simple Amazon Alexa skill for retrieving a few linguistic properties of words. It currently supports:

* Synonyms
* Antonyms
* Parts of Speech
* Rhymes
* Definitions
* Syllables
* Word Frequency
* Pronunciation

## Usage

Here is how to call it using Alexa:

* Synonym: "Alexa, ask word box for a synonym for {Word}."
* Antonym: "Alexa, ask word box for an antonym for {Word}."
* Part of Speech: "Alexa, ask word box for the part of speech for {Word}."
* Rhyme: "Alexa, ask word box for a rhyme for {Word}."
* Definition: "Alexa, ask word box for the definition of {Word}."
* Syllables: "Alexa, ask word box for the syllables of {Word}."
* Frequency: "Alexa, ask word box for the frequency of {Word}."
* Pronunciation: "Alexa, ask word box for the pronunciation for {Word}."

## Implementation

WordBox uses `intent_schema.json` and `sample_utterances.json` for its interaction model, and an AWS lambda function `lambda_function.py` for the backend code. The lambda function passes off the Alexa request to one of the four intent functions, where a call is made to the [WordsAPI](https://market.mashape.com/wordsapi/wordsapi) through mashape. Also included in the repository is `wordbox.zip`, which contains the environment I developed in and deployed directly to Amazon AWS Lambda.

## Using the Code

You are free to download and use the code for whatever purposes you desire under the MIT License. If you have any useful changes, feel free to propose a change or submit a pull request.
