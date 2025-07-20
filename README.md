## How to Run the Broadway Gross Prediction App

This application predicts the weekly gross revenue of a Broadway show based on key inputs like attendance and show capacity.

### Requirements
- Python 3.10+
- Internet connection (for package install)
- No database setup required (data is run from an already embedded .csv file)

---

### Step-by-Step Instructions

Below each step are the commands to run in your local machine's terminal.

1. **Download or clone this repository**  
        git clone https://github.com/YOUR_USERNAME/broadway-insights.git #(replace YOUR_USERNAME with your GitHub username)  
        cd broadway-insights
2. **Create a virtual environment**  
        python -m venv .venv  
        source .venv/bin/activate (or on Windows: .venv\Scripts\activate)
3. **Install dependencies**  
        pip install -r requirements.txt
4. **Train the model**  
        PYTHONPATH=. python models/train_linear_model.py
5. **Start the prediction server**  
        python backend/app.py
6. **Open the dashboard in your browser**  
        Open your browser and navigate to http://127.0.0.1:5000  
        Use the online form to enter your data you'd like to test. 

### ADVANCED
To run everything the entire project on Unix/macOS: Double-click on "bash run_app.sh"  
To run everything the entire project on Windows: Double-click on "run_app.bat"  
After running the appropriate scripts, navigate to http://127.0.0.1:5000  
> This will set up the environment, install requirements, train the model, and launch the app.
