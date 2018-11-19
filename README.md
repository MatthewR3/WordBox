# WordBox

WordBox is a simple Amazon Alexa skill for retrieving a few linguistic properties of words. It currently supports:

* Synonyms
* Antonyms
* Parts of Speech
* Rhymes
* Definitions
* Syllables
* Word Frequency

## Usage

Here is how to call it using Alexa:

* Synonym: "Alexa, ask word box for a synonym for {Word}."
* Random Synonym: "Alexa, ask word box for a random synonym for {Word}."
* All Synonyms: "Alexa, ask word box for all synonyms for {Word}."
* Antonym: "Alexa, ask word box for an antonym for {Word}."
* Random Antonym: "Alexa, ask word box for a random antonym for {Word}."
* All Antonyms: "Alexa, ask word box for all antonyms for {Word}."
* Part of Speech: "Alexa, ask word box for the part of speech for {Word}."
* Rhyme: "Alexa, ask word box for a rhyme for {Word}."
* Random Rhyme: "Alexa, ask word box for a random rhyme for {Word}."
* Definition: "Alexa, ask word box for the definition of {Word}."
* All Definitions: "Alexa, ask word box for all definitions of {Word}."
* Syllables: "Alexa, ask word box for the syllables of {Word}."
* Frequency: "Alexa, ask word box for the frequency of {Word}."

## Development

WordBox uses the Alexa development suite to parse the speech requests, then passes them to the AWS lambda function `lambda_function.py` to retrieve the proper response from the Words API.

### Alexa

The `skill.json` file defines the skill's public-facing information for each English dialect that is supported.

The `skill_manifest.json` file defines the intent schema for the skill. This can be imported directly into the Alexa web console and interacted with from there.

In addition to the 3-4 built-in intents, there are 15 custom intents. Each one follows the same constraints, requiring a slot named `WORD` of type `AMAZON.SearchQuery` - this slot type allows free-form speech input to be captured and passed on to the AWS Lambda function.

The `tests` directory contains tests that can be inputted to the Alexa development suite testing console via the "Manual JSON" tab. Note that the tests are not yet comprehensive.

### AWS Lambda

`lambda_function.py` defines the backend logic for the skill. The script is a wrapper on top of the Words API, parsing the request passed in from the Alexa suite and handling API calls. It is deployed on AWS Lambda, with built-in logging via CloudWatch.

To use the script in AWS Lambda, it must be submitted with an environment containing all necessary Python packages - this is contained in the `wordbox_env` directory, which can be zipped and submitted to the AWS Lambda console. Logging through CloudWatch can be implemented by simply printing to stdout.

### Deployment

To ensure a successful deployment, ensure the following:

1. The sample utterances and example phrases for the skills match in the Alexa development suite console.
2. Each intent in `lambda_function.py` returns a proper response both in the AWS Lambda testing console.
3. Each intent returns a proper response in the Alexa development suite testing console.
4. Each intent properly handles incorrect slot values, missing values, and other unexpected usages in the Alexa development suite testing console.
5. The AWS Lambda ARN in the "Endpoint" tab of the Alexa development suite points to the correct version of the WordBox_Dev Lambda function.
6. The "Validation" and "Functional test" tests in the Alexa development suite pass without errors.

## Using the Code

You are free to download and use the code for whatever purposes you desire under the MIT License. If you have any useful changes, feel free to propose a change or submit a pull request. Please see the issues if you wish to contribute; I would be glad to note you as an author!
