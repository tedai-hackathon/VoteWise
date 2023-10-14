# VoterGuideAI & OpenAI ChatGPT Integration: Bridging Democratic Decision-Making with Advanced AI Conversations

---

## Overview:

We stand at the confluence of AI innovation and democratic responsibility. Our platform brings to you two pioneering solutions:

1. **VoterGuideAI**: A tool that dynamically aligns the complexities of voting with individual values.
2. An **Open-Source Python-Based Project** harnessing the capabilities of OpenAI ChatGPT, fostering intelligent and dynamic interactions.

---

## The New Age of Voting with VoterGuideAI:

**The Challenge**: 
Regions like California present intricate ballots that often deter the average citizen from participating in the democratic process due to their complexity.

**Our Remedy**: 
VoterGuideAI employs advanced AI and LLMs to dissect every ballot measure and candidate. By actively interacting with users, it discerns their unique values, offering tailored voting recommendations, ensuring that the act of voting becomes more intuitive and resonant.

---

## Intelligent Conversations with OpenAI ChatGPT:

Redefining user interactions, our Open-Source Python-Based project taps into the power of OpenAI ChatGPT. Designed for versatility, this integration delivers insightful and engaging dialogues, catering to a myriad of needs – be it customer support, information extraction, or casual interactions. Dive into an enhanced conversational experience like never before.

---

## Impact & Broader Vision:

Beyond the technology, VoterGuideAI aims to drive meaningful societal change. By optimizing the voting experience, we are championing:

- Strengthened democratic institutions.
- Expanded access to essential services.
- Promotion of gender equality.
- Reduction in prevailing inequalities.
- Creation of sustainable communities.

In aligning genuine public sentiment with broader objectives, we're not merely aiming; we're actualizing a sustainable future.

---

**Join the Movement**:
With VoterGuideAI's democratic insights and the Open-Source Python-Based project's conversational prowess, we're carving out the future of informed decision-making. Be a part of this transformative journey, where democracy becomes more accessible, and interactions smarter.


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


