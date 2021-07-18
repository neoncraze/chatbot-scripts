# teppen-lexicon

_(For [TEPPEN Lexicon](http://teppenlexicon.com).)_

Code snippets and usage examples for the various Chatbot providers.
Look for your preferred provider and use them accordingly.

Feel free to open a PR for your chatbot if it isn't currently available.

## Available chatbots

- [Streamlabs Chatbot](#streamlabs-chatbot)
- [StreamElements](#StreamElements)
- [Nightbot](#Nightbot)

---

## Streamlabs chatbot

Not to be confused with Streamlabs **Cloudbot**. This is for the Chatbot software.

Further instructions in its own [subdirectory](Streamlabs).

## StreamElements

Create a custom command with the following response. Enable `reply` under Advanced Settings if you'd like the chatbot to @ reply the user.

Sadly StreamElements does not allow for conditional evaluation, so you will not be able to provide a default usage example in the event that a user does not input any query. The bot would not respond if nothing follows the command.

```
http://teppenlexicon.com/en/cards/?name_contains=${queryescape ${1:}}


# Example
> User: !teppen
>

> User: !teppen kushala daora
> StreamElements: @neoncraze_, http://teppenlexicon.com/en/cards/?name_contains=kushala+daora
```

## Nightbot

```
@$(user) $(eval '$(1)' === 'null' ? 'Usage - !teppen <card name>' : `http://www.teppenlexicon.com/en/cards/?name_contains=$(querystring)`)


# Example
> User: !teppen
> Nightbot: @neoncraze_ Usage - !teppen <card name>

> User: !teppen traitor tyrant
> Nightbot: @neoncraze_ http://www.teppenlexicon.com/en/cards/?name_contains=traitor%20tyrant
```
