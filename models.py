import json

from constants import LIKERT_LOOKUP, QUESTION_TEXT


class VoterInfo:
    """
    define a VoterInfo class to capture demographic and values information about the voter
    and then a FlaskForm that uses VoterInfo as a model and captures those fields

    """
    likert_choices = [
        "housing",
        "economy",
        "environment",
        "immigration",
        "income_inequality",
        "transportation",
        "education",
        "healthcare",
        "public_safety",
        "taxation",
    ]

    def __init__(self):
        self.street_address = None
        self.city = None
        self.state = None
        self.address_zip_code = None
        self.party_affiliation = None
        self.political_issues = None
        self.housing = None
        self.economy = None
        self.environment = None
        self.immigration = None
        self.income_inequality = None
        self.transportation = None
        self.education = None
        self.healthcare = None
        self.public_safety = None
        self.taxation = None

    @classmethod
    def from_vals(cls, **kwargs):
        """
        alternative constructor that can take a dict of values and populate the fields

        :param kwargs:
        :return:
        """
        instance = cls()
        for k, v in kwargs.items():
            setattr(instance, k, v)
        return instance

    def for_llm(self):
        """
        output contents as a json-structured string we can feed to the llm.

        for all the likert fields, convert the numeric value to the corresponding string value,
        based on the LIKERT_CHOICES mapping.
        :return: str
        """
        fields = self.__dict__
        for likert_val in self.likert_choices:
            numeric_val = fields[likert_val]
            if numeric_val in LIKERT_LOOKUP:
                fields[likert_val] = {
                    'question': QUESTION_TEXT[likert_val],
                    'response': LIKERT_LOOKUP[numeric_val]
                }
        return json.dumps(fields)


class VoterInfoEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, VoterInfo):
            return obj.__dict__
        return super().default(obj)


class VoterInfoDecoder(json.JSONDecoder):
    def decode(self, json_str, **kwargs):
        data = json.loads(json_str)
        voter_info = VoterInfo()
        voter_info.__dict__.update(data)
        return voter_info
