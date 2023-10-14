# VoteWise & OpenAI ChatGPT Integration: Democratizing Decision-Making with Advanced AI Conversations

---

## Overview:

In the nexus of AI innovation and democratic participation, we introduce:

**VoteWise**: A dynamic tool tailoring the voting process to individual values and interests.

## Empowering Voters with VoteWise:

**The Challenge**: 
Complex ballots in regions like California often deter active participation, making democratic representation a challenge for many.

**Our Remedy**: 
VoteWise utilizes cutting-edge AI and LLMs to parse each ballot measure and candidate. By proactively engaging with users, it identifies and aligns with their core values, offering precise voting recommendations. This ensures that voting is not only more intuitive but also truly representative.

---

## Enriched Conversations with OpenAI ChatGPT:

Revolutionizing user interactions, our Open-Source Python-Based project harnesses the strength of OpenAI ChatGPT. This versatile integration offers users profound and engaging dialogues, suitable for diverse needs – from customer support, knowledge retrieval to casual banter. Experience a heightened conversational ecosystem like never before.

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


View the live site at http://votewise.radiantmachines.com/

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


