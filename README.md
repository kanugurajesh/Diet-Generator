# Diet Generator 🥗

A Streamlit-based web application that generates personalized diet recommendations using LangChain and Ollama (llama3.2) 🚀

## Description 📝

Diet Generator is an AI-powered tool that creates customized dietary recommendations based on individual characteristics such as:
- Age 👶👨👴
- Gender ⚧
- Body Composition 💪
- Activity Level 🏃‍♂️

The application uses LangChain with a local Ollama setup running the llama3.2 model to generate personalized diet advice.

## Prerequisites ✅

- Python 3.8+ 🐍
- Ollama installed on your system 🖥️
- llama3.2 model downloaded via Ollama 🦙

## Installation 🛠️

1. Clone the repository:
```bash
git clone https://github.com/kanugurajesh/diet-generator.git
cd diet-generator
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install langchain langchain-community langchain-ollama streamlit
```

4. Install and setup Ollama:
- Visit [Ollama's official website](https://ollama.ai/) to download and install
- After installation, open the terminal and run the llama3.2 model:
```bash
ollama run llama3.2
```

## Usage 📱

1. Make sure Ollama is running in the background with llama3.2 model available

2. Start the Streamlit application:
```bash
streamlit run app.py
```

3. Access the web interface through your browser (typically http://localhost:8501)

4. Fill in your details:
   - Select your gender 👨👩
   - Enter your age 🔢
   - Choose your body composition 💪
   - Select your activity level 🏃‍♂️
   
5. Click "Generate" to receive your personalized diet recommendations

6. You can either view the recommendations directly on the page or download them as a text file 📄

## Project Structure 📂

- `app.py` - Main Streamlit application interface
- `generate_diet.py` - Core logic for diet generation using LangChain and Ollama
- `requirements.txt` - Project dependencies
- `.gitignore` - Git ignore rules

## Technical Details ⚙️

The application uses:
- Streamlit for the web interface 🌐
- LangChain for prompt engineering and LLM integration ⛓️
- Ollama for local LLM hosting 🦙
- llama3.2 as the base language model 🤖

## Error Handling ⚠️

The application includes basic error handling for:
- Invalid input validation
- LLM generation failures
- Connection issues with Ollama

## Creator 👨‍💻

**Kanugu Rajesh**
- GitHub: [https://github.com/kanugurajesh](https://github.com/kanugurajesh) 🌟
- LinkedIn: [https://linkedin.com/in/rajeshkanugu](https://linkedin.com/in/rajeshkanugu) 💼

## Contributing 🤝

Feel free to fork the repository and submit pull requests for any improvements.

## License 📄