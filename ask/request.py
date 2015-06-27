
class Request(object):

    def __init__(self, session, body):
        self._session = session
        self._body = body

    @staticmethod
    def from_json(json):
        return Request()

    @property
    def session(self):
        return self._session

    @session.setter
    def session(self, value):
        self._session = value

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value


class RequestSession(object):

    def __init__(self, is_new, session_id, application_id, attributes, user_id):
        self._is_new = is_new
        self._session_id = session_id
        self._application_id = application_id
        self._attributes = attributes,
        self._user_id = user_id

    @property
    def is_new(self):
        return self._is_new

    @is_new.setter
    def is_new(self, value):
        self._is_new = value

    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value

    @property
    def application_id(self):
        return self._application_id

    @application_id.setter
    def application_id(self, value):
        self._application_id = value

    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, value):
        self._attributes = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


class RequestBody(object):

    def __init__(self, body_type, timestamp, request_id):
        self._body_type = body_type
        self._timestamp = timestamp
        self._request_id = request_id
        
    @property
    def timestamp(self):
        return self._timestamp
    
    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value

    @property
    def request_id(self):
        return self._request_id
    
    @request_id.setter
    def request_id(self, value):
        self._request_id = value

# TODO: various requests