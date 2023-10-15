# VoteWise

## Overview:

In the nexus of AI innovation and democratic participation, we introduce:

**VoteWise**: A dynamic tool tailoring the voting process to individual values and interests.

## Empowering Voters with VoteWise:

**The Challenge**: 
Complex ballots in regions like California often deter active participation, making democratic representation a challenge for many.

**Our Remedy**: 
VoteWise utilizes cutting-edge AI and LLMs to parse each ballot measure and candidate. By proactively engaging with users, it identifies and aligns with their core values, offering precise voting recommendations. This ensures that voting is not only more intuitive but also truly representative.

## Hackathon Judging Criteria

Criterion: How will VoteWise align with the criterion? 

### Relevance to Societal Challenges: 

This problem directly addresses the global issue of the voting process being unreflective of individuals’ values or completely inaccessible to large segments of society given its level of complexity. As a result political, social and economic institutions around the world are unrepresentative of people’s diverse backgrounds. VoteWise directly aligns with UN SDG 16 of building inclusive institutions and societies and UN SDG 10 of reducing inequalities and increasing the representation of the underrepresented. It also aligns with UN SDG 11 &4. 



### Real-World Impact: 

This solution will ensure people around the world have the opportunity to have a direct impact on their communities and their countries by participating in a truly representative democratic process. We believe that for peace and justice to be sustainable all institutions must be representative of and held accountable to all of their citizens, not just the most educated, wealthy, or older populations who are much more likely to vote. 

### Scalability and Sustainability: 
 
This project is designed to scale throughout the world as it’s multi-channel and supports any language. We plan to make this project Open Source and so it can be scaled and easily maintain in any country around the world. 

### Usability and Accessibility:

This project is designed to be accessible to people of all backgrounds in a number of ways: Mutli-lingual, Voice enabled for hearing disabilities, Mobile and web app, Adaptive to different education levels  
Innovative Use of AI:


### Innovative Use of AI: 

We use cutting edge AI models such as GPT4 and Claude that provide effective and high-accuracy abstractive summarization as well as complex reasoning capabilities and long context windows that allow integrating complex real world information about candidates’ positions and background.

### Technical Execution: 

An open source Flask-based web application. We minimize technical complexity to maximize maintainability and scalability. We use langchain to make calls as necessary to Anthropic and OpenAI APIs, and use Python web-scraping technologies to aggregate information about ballots and elections.

### Presentation and Documentation: 
See this document!

### Responsible AI: 

There is a risk of introducing misinformation. But the political media environment is already intensely polluted by candidates and campaigns deliberately flooding the public with misinformation. VoteWise can triangulate information from multiple sources (particularly sources we have curated for high credibility) in order to best estimate what’s likely to be true, and can admit when its knowledge is limited and can present opposing sides of an issue as necessary. We also aim to provide clear justification for all recommendations and to cite sources as much as possible.

### Data Consent  & Privacy:

We show a clear privacy and data use policy from users’ first point of contact with the app. We also emphasize data minimization and collect as little as we need to in order to make effective recommendations. We do not retain user information once they’ve finished using the service for a given location, minimizing the risk of data breach or loss.

--- 
## Impact & Broader Vision:

VoteWise is more than just technology; it's a movement towards a more inclusive society. By enhancing the voting experience, we champion:

- Robust democratic structures.
- Universal access to pivotal services.
- Gender inclusivity.
- Curtailing prevailing disparities.
- Cultivating sustainable urban and rural habitats.

By synchronizing genuine public sentiment with broader societal goals, we're creating a brighter, more sustainable tomorrow.

---

**Join the Evolution**:
With VoteWise's democratic insights and the advanced conversational capabilities of our Open-Source Python project, we're redefining the future of participatory democracy and AI-powered interactions. Join us in this transformative journey, making democracy more accessible and conversations richer.



## Prerequisites

- Python 3.9 or higher
- Flask
- Langchain
- OpenAI API
- OpenAI Python library

## Getting Started

### Clone the repository:

```bash
git clone https://github.com/gjlondon/VoteWise
```

###  Navigate to the project directory:
    
```
cd VoteWise
```

### Install the required dependencies using pip:
    
```
pip install -r requirements.txt
````

### Set up OpenAI API:

- Create an OpenAI account and obtain an API key.
- Set the `OPENAI_API_KEY`` environment variable with your API key 
- Set the `ANTHROPIC_API_KEY`` environment variable with your API key 

    On Windows:
    - Use the search bar in the Start menu to find “Edit the system environment variables”.
    - Click “Environment variables”
    - Use the upper “New…” button to add a User variable
    - Create a new variable called OPENAI_API_KEY and set the value to the secret key you got from your account settings on openai.com

    For Mac or Linux:
    - Find the .bashrc, .bash_profile, or .zshrc in your home directory
    - Open the file in a text editor
    - Add a new line to the file:
    ``export OPENAI_API_KEY= [your secret key]``

### Run the application:

Start the app like this

```
flask run
```

### View site
 Open your web browser and visit http://127.0.0.1:{port}/ to access the chat bot.



## Usage
Once the application is running, you can interact with the chat bot through the web interface. Type your messages in the input box, and the bot will respond accordingly.

## Deployment
To deploy the chat bot to a production environment, follow the deployment instructions provided by the Flask documentation. It's recommended to use a production-ready WSGI server, such as Gunicorn or uWSGI.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please create a GitHub issue or submit a pull request.

    Feel free to modify and expand upon this template according to your specific project needs.


