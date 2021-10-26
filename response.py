class ApiException(Exception):
    def __init__(self, code, error_message, result=None):
        self.result = result
        self.code = code
        self.error_message = error_message

#SUCCESS MESSAGE
SUCCESS = "SUCCESS"
CREATE_KEYWORD = "CREATE_KEYWORD"
#FAILED MESSAGE
DUPLICATED_KEYWORD = "DUPLICATED_KEYWORD"
FIND_NOT_KEYWORD = "FIND_NOT_KEYWORD"
ALREADY_EXISTS_KEYWORD = "ALREADY_EXISTS_KEYWORD"
INVALID_INPUT_KEYWORD = "INVALID_INPUT_KEYWORD"