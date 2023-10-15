OAKLAND_MAYOR_ISSUES = """
1. *Affordable housing*: Addressing the housing crisis and ensuring the construction of more affordable housing units.
1. *Homelessness:* Developing strategies to reduce homelessness and provide support to those in need.
1. *Public safety*: Balancing support for the police department with advocating for changes to improve public safety.
1. *Violence prevention*: Investing in programs and initiatives to reduce crime and violence in the city.
1. *Infrastructure:* Repairing and maintaining roads, bridges, and other critical infrastructure.
1. *Education:* Supporting and improving the quality of education in Oakland schools.
1. *Economic resilience*: Strengthening the local economy and creating job opportunities.
1. *City budget*: Ensuring responsible management of the city's budget and allocation of resources.
1. *Community engagement*: Encouraging collaboration between city officials, residents, and businesses to address local issues.
1. *Environmental policies*: Supporting environmentally friendly policies and initiatives to combat climate change.
1. *Transportation:* Improving public transportation and addressing traffic congestion.
1. *Police accountability*: Strengthening oversight and accountability of the police department.
1. *City government* collaboration: Encouraging cooperation between the mayor, city council, and other government entities to solve the city's problems.
1. *Social justice*: Addressing issues of social and economic inequality in the city.
"""

OAKLAND_MAYOR_CANDIDATES = [
    """Tyron Jordan
Summary: A paralegal and Army veteran, Jordan wants to fund more rental and mortgage assistance and staff up the public works department to fix roads""",

    """John Reimann
Summary: Reimann is a socialist who believes lasting change can only be achieved if it’s supported by grassroots movement-building""",

    """Allyssa Victory
Summary: A civil rights attorney, Victory aims to ensure Oakland builds more affordable housing, repairs busted roads, and invests in violence prevention""",

    """Treva Reid
Summary: The District 7 councilmember wants to build stronger partnerships with county, state, and federal governments and with private industry to tackle Oakland’s biggest problems""",

    """Sheng Thao
Summary: The District 4 councilmember, who won the election, claims to understand the budget better than any other candidate and plans to invest in affordable housing and violence prevention""",

    """Ignacio De La Fuente
Summary: The former councilmember is coming out of political retirement to run because he feels Oakland’s officials are failing to keep residents and businesses safe""",

    """Loren Taylor
Summary: Taylor, who gave up his District 6 Council seat to run for mayor, said he would continue the reimagining public safety process and establish a City Hall East""",

    """Seneca Scott
Summary: The neighborhood organizer plans to restore the rule of law in Oakland and make the city more economically resilient""",

    """Greg Hodge
Summary: The nonprofit leader and former Oakland school board president said he would improve the culture at City Hall and help The Town heal""",
]

OAKLAND_MAYOR_CANDIDATE_INFO = {
    """Tyron Jordan""": {

        "summary": """A paralegal and Army veteran, Jordan wants to fund more rental and mortgage assistance and 
        staff up the public works department to fix roads""",
    },

    """John Reimann""": {

        "summary": """Reimann is a socialist who believes lasting change can only be achieved if it’s supported by 
        grassroots movement-building""",
    },

    """Allyssa Victory""": {

        "summary": """A civil rights attorney, Victory aims to ensure Oakland builds more affordable housing, 
        repairs busted roads, and invests in violence prevention""",
    },

    """Treva Reid""": {

        "summary": """The District 7 councilmember wants to build stronger partnerships with county, state, 
        and federal governments and with private industry to tackle Oakland’s biggest problems""",
    },

    """Sheng Thao""": {

        "summary": """The District 4 councilmember, who won the election, claims to understand the budget better than 
        any other candidate and plans to invest in affordable housing and violence prevention""",
    },

    """Ignacio De La Fuente""": {

        "summary": """The former councilmember is coming out of political retirement to run because he feels 
        Oakland’s officials are failing to keep residents and businesses safe""",
    },

    """Loren Taylor""": {

        "summary": """Taylor, who gave up his District 6 Council seat to run for mayor, said he would continue the 
        reimagining public safety process and establish a City Hall East""",
    },

    """Seneca Scott""": {

        "summary": """The neighborhood organizer plans to restore the rule of law in Oakland and make the city more 
        economically resilient""",
    },

    """Greg Hodge""": {
        "summary": """The nonprofit leader and former Oakland school board president said he would improve the 
        culture at City Hall and help The Town heal""",

    }
}

INITIAL_RECOMMENDATION_PROMPT = """
    Pretend the date is November 1st, 2022. The 2022 California general election is coming up soon, and Californians are
      trying to decide how to vote in the election for: {race}.

      Californians are reasonable, intelligent, mature adults who want to do their civic duty by voting in a well-educated
      and sensible fashion. But the california ballot has many races, and it can be confusing and time consuming for Californians
      to research each individual race and fully understand the nuance of the issue they're voting on, as well as the
      details of how that outcome of that race impacts their life and which outcome is best aligned with their personal values
      and interests.

      You are acting as a wise voter guide -- your goal is to help voters who come to you decide on a particular candidate or outcome to vote for in
      each race. You want to understand as much as you need to about the voter's life and values in order to help guide them towards
      the conclusion that is best for them. 
      
      You will be provided with information about the candidates in the race, as well as information about the
       candidate's history and stated positions on various issues. Since this is a local election, media resources decicated to covering it
       have been limited, and not all candidates will have been covered in the media or have given complete statements on every position. 
       Nevertheless, the voter must decide on a candidate to vote for, so it is better for you to make informed assumptions about the candidates
       instead of asking the voter to make their own assumptions. But you should be clear about what you're assuming vs. what you know.
       
    You are assisting a voter who lives in the {voter_zip_code} zipcode.

    They've filled out a brief survey about their demographics and preferences, and the results are captured 
    as JSON here:

    ```
    {voter_info_summary}
    ```

    In this case, you're going to make a recommendation in the race for Oakland Mayor.

    Here is a JSON that lists the candidates for Oakland mayor, as well as any explicit information about them and their 
    positions that you've been able to find in the media or online. Prefer to use the information in this JSON over your own assumptions,
    but you can make intelligent assumptions if you need to.

    ```
   {race_info}
   ```

      You will make a specific recommendation, but will make sure to justify the recommendation by citing specific evidence
      about why a particular candidate or outcome is best aligned with the voter's interests and goals.
      
     As a first step towards making a recommendations, you will list each candidate or outcome in this particular 
     race, along with a short summary of their positions on the issues that are most important to the voter.

    Then you will rank the candidates or outcomes in order of how well they reflect the voter's interests and 
    preferences, giving a 1-2 sentence justification for the ranking you gave to each candidate.

    My friend is smart and reasonable and understands that your rankings will not be perfect, so don't hedge and just 
    give it your best shot.

    Give a single overall ranking for each candidate, and list the candidates in order of best to worst (making sure 
    to specifically mention at least the top several candidates).

    Be as specific and concrete as possible, and make sure to address the issues that are most important to the voter. 

    End up by making it very clear which candidate best reflects his interests and preferences.

    Format your answer nicely so that it's easy to read and understand.
    """


MAYOR_SCORING_PROMPT_TEMPLATE = """
    
    The date is November 1st, 2022 (7 days before the 2022 California general election).
    
    The 2022 Oakland Mayoral Election is coming up soon, and Californians are trying to decide how to vote in the election for: 2022 Oakland Mayoral Election.
    
    You are a politically-neutral but diligent and objective political science expert who has been hired to help compile a voter information guide for voters to use in the upcoming 2022 California General Election. You are trying to help a voter figure out how well aligned each canddiate in the race is with their personal values.
    
    You will be provided with a summary of the voter that gives their answers to 10 exemplary questions that are intended to capture their overall values and priorities.
    
    You will be given a summary of information about candidates for Oakland mayor. 
    
    For each field in each data structure for each candidate, you will provide a score from -100 to 100 that reflects whether that aspect of the candidate seems well aligned with the voter's values, priorities, and interests.
    
    A score of -100 should mean that the candidate's values are diametrically opposed to the voter's values -- this candidate would actively pursue policies that are the opposite of what the voter wants.
    
    A score of 100 means that the candidate's values are perfectly aligned with the voter's values -- this candidate would actively pursue policies that are exactly what the voter wants.
    
    For each score, give a detailed justification for why you gave that score. You will sometimes not have as much information as you'd like to make a perfect judgement, but do your best to make an informed judgement based on the information you have. It is okay to draw inferences from what you know about a candidate's background, even if those inferences are not directly supported by the materials you've been provided. If you feel like you really cannot draw any inference or come up with any score, give a score of 0 and explain why you cannot make a judgement.
    
    Key issues:
    ```
    {oakland_mayor_issues}
    ```
    
    And here is the information about the candidate:
    ```
    
    {candidate_summary}
    ```
    
    ```
    
    And here is the information about the voter:
    ```
    {voter_info_json}
    ```
    
    And example output would be:
    
    ```JSON
    {{
   
    "name": Jane Smith,
    "background": {{"score": 80, "reasoning": "Jane Smith's background shows that she has had the type of professional success this voter respects and values"}},
    "platform": {{"score": 50, "reasoning": "Jane Smith's platform is a mix of policies that this voter supports and opposes"}},
    "stance_on_key_issues": {{"score": 100, "reasoning": "Jane Smith's stance on the key issues is perfectly aligned with this voter's values and interests"}},
    "detail_on_key_issues": {{
    "homelessness": {{"score": 100, "reasoning": "Jane Smith's stance on homelessness is perfectly aligned with this voter's values and interests"}},
    "affordable_housing": {{"score": -70, "reasoning": "Jane Smith's stance on affordable housing is diametrically opposed to this voter's values and interests"}},
    }},
    "party_affiliation": {{"score": 0, "reasoning": "Jane Smith's party affiliation is unknown, so it is impossible to make a judgement about how well aligned it is with this voter's values and interests"}},
    "major_donors_and_endorsements": {{"score": 30, "reasoning": "Jane Smith's major donors and endorsements are a mix of people and groups that this voter supports and opposes"}},
    "local_reporting_and_coverage": {{"score": 75, "reasoning": "Jane Smith's local reporting and coverage is uniformly positive, showing that she is liked and respected in the community}},
    "track_record_of_integrity": {{"score": 100, "reasoning": "Jane Smith's track record of personal, professional, and political integrity is perfect, showing that she is a person of high character and integrity"}}
    }}
    ```
    
    """

MAYOR_OVERALL_RECOMMENDATION_PROMPT_TEMPLATE = """

The date is November 1st, 2022 (7 days before the 2022 California general election).

The 2022 Oakland Mayoral Election is coming up soon, and Californians are trying to decide how to vote in the election for: 2022 Oakland Mayoral Election.

You are a politically-neutral but diligent and objective political science expert. You do not care which candidate wins the race, but you do believe that well-informed civic engagement is an intrinsic value and you want to help every voter (regardless of education or ability) make the best possible vote for someone who will represent their values and interests.

 You are speaking to a new immigrant to Oakland, California who has just become a citizen. They're curious and want to become politically active, but they are totally unfamiliar with the USA and california political system. They are going to be voting in their first ever US election.

  The voter has done independent research into each of the candidates and has created a summary of their alignment with each candidate. The summaries score how aligned the voter is each various aspects of each candidate, such as the candidate's background and track record, their platform, their stance on key issues, their party affiliation, their major donors and endorsements, their local reporting and coverage, and their track record of personal, professional, and political integrity.

  Scores of -100 on an attribute mean that the voter feels they are very misaligned with the candidate in that respect. A score of +100 means that the voter feels they are very well aligned.

  Given a set of summaries for each candidate in the race, think step by step and help the voter rank the for 4 candidates (from best to worst) with respect to how well that candidate would represent the interests, priorities, and values of that voter. Give a clear, step by step explanation via a set of bullet points that justify the ranking you gave to each candidate. The overall explanation should be substantial and detailed - you should aim for 10 or more bullet points, each with 100 or more words. You should really make it clear why the candidates you ranked higher stand out and are more well aligned with the voter relative to the lower ranked candidates.

  Your answer perfectly and compliantly submits to the following requirements:
  * Your answer is a JSON that is syntactically valid according to RFC 8259, "The JavaScript Object Notation (JSON) Data Interchange Format," published by the Internet Engineering Task Force (IETF)
  * You list only the top five highest ranked candidates
  * You provide at least five justificatory bullet points for each candidate (with each point being at least 100 words long and making a clear and specific point about why the candidate is well aligned with the voter)

  If it is useful, here is a list of some of the key issues in the 2022 Oakland Mayoral Election:

Key issues:
```
{OAKLAND_MAYOR_ISSUES}
```

And here is the information about the voter:
```
{voter_info_json}
```

And here are the scoring summaries for each candidate:
```
{overall_candidate_scores}
```

Give your response in this format:
```JSON
{{
"summary_of_voter": {{A two-paragraph summary of the voter's overall values and interests.}},
"recommendation": {{top recommended candidate}},
"ranking": [
{{candidate 1}},
{{candidate 2}},
{{candidate 3}},
{{candidate 4}},
],
"justification": {{
"{{candidate 1}}": \"""
                                       * {{first long, clear bullet point of justification for ranking of candidate 1}}
                                       * {{second long, clear bullet point of justification for ranking of candidate 1}}
                                       * {{third long, clear bullet point of justification for ranking of candidate 1}}
                                       * {{fourth long, clear bullet point of justification for ranking of candidate 1}}
\"""
"{{candidate 2}}": \"""
                                       * {{first long, clear bullet point of justification for ranking of candidate 2}}
                                       * {{second long, clear bullet point of justification for ranking of candidate 2}}
                                       * {{third long, clear bullet point of justification for ranking of candidate 2}}
                                       * {{fourth long, clear bullet point of justification for ranking of candidate 2}}
\""",
"{{candidate 3}}": \"""
                                       * {{first long, clear bullet point of justification for ranking of candidate 3}}
                                       * {{second long, clear bullet point of justification for ranking of candidate 3}}
                                       * {{third long, clear bullet point of justification for ranking of candidate 3}}
                                       * {{fourth long, clear bullet point of justification for ranking of candidate 3}}
\""",
"{{candidate 4}}": \"""
                                       * {{first long, clear bullet point of justification for ranking of candidate 4}}
                                       * {{second long, clear bullet point of justification for ranking of candidate 4}}
                                       * {{third long, clear bullet point of justification for ranking of candidate 4}}
                                       * {{fourth long, clear bullet point of justification for ranking of candidate 4}}
\""",
}}
}}
```

The output is going to be directly parsed and loaded into python via a `json.loads` call, so make sure it is exactly adheres to the json syntactic validity requirements laid out in RFC 8259, "The JavaScript Object Notation (JSON) Data Interchange Format," published by the Internet Engineering Task Force (IETF)
"""