def add_if_set(collection, key, value):

    if value is not None and len(value) > 0:
        collection[key] = value

    return


class Response(object):

    def __init__(self, version, session_attributes, output_speech, card, reprompt, should_end_session):
        self._version = version
        self._session_attributes = session_attributes
        self._output_speech = output_speech
        self._card = card
        self._reprompt = reprompt
        self._should_end_session = should_end_session

    def as_message(self):
        msg = {
            "version": self.version,
            "response": {},
            "shouldEndSession": self.should_end_session
        }

        add_if_set(msg, "sessionAttributes", self.session_attributes)
        add_if_set(msg["response"], "outputSpeech", self.output_speech)
        add_if_set(msg["response"], "card", self.card)
        add_if_set(msg["response"], "reprompt", self.reprompt)

        return msg

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value
    
    @property
    def session_attributes(self):
        return self._session_attributes
    
    @session_attributes.setter
    def session_attributes(self, value):
        self._session_attributes = value

    @property
    def output_speech(self):
        return self._output_speech
    
    @output_speech.setter
    def output_speech(self, value):
        self._output_speech = value

    @property
    def card(self):
        return self._card

    @card.setter
    def card(self, value):
        self._card = value

    @property
    def reprompt(self):
        return self._reprompt

    @reprompt.setter
    def reprompt(self, value):
        self._reprompt = value

    @property
    def should_end_session(self):
        return self._should_end_session
    
    @should_end_session.setter
    def should_end_session(self, value):
        self._should_end_session = value


class OutputSpeech(object):

    def __init__(self, text, type="PlainText"):
        self._text = text
        self._type = type


class Card(object):

    def __init__(self, title, content, type="Simple"):
        self._title = title
        self._content = content
        self._type = type

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def type(self):
        return "Simple"
