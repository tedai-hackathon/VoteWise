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


