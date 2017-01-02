# WordWorks

WordWorks is a simple Amazon Alexa skill for retrieving a few linguistic properties of words. It currently supports:

* Synonyms
* Antonyms
* Parts of Speech
* Rhymes

## Usage

Here is how to call it using Alexa:

* Synonym: "Alexa, ask word works for a synonym for {Word}."
* Antonym: "Alexa, ask word works for an antonym for {Word}."
* Part of Speech: "Alexa, ask word works for the part of speech for {Word}."
* Rhyme: "Alexa, ask word works for a rhyme for {Word}."

## Implementation

WordWorks uses `intent_schema.json` and `sample_utterances.txt` for its interaction model, and an AWS lambda function `lambda_function.py` for the backend code. The lambda function passes off the Alexa request to one of the four intent functions, where a call is made to the [WordsAPI](https://market.mashape.com/wordsapi/wordsapi) through mashape. Also included in the repository is `wordworks.zip`, which contains the environment I developed in and deployed directly to Amazon.

## Using the Code

You are free to download and use the code for whatever purposes you desire under the MIT License. If you have any useful changes, feel free to propose a change or submit a pull request.
