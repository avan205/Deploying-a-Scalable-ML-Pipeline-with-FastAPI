Working in a command line environment is recommended for ease of use with git and dvc. If on Windows, WSL1 or 2 is recommended.

# Environment Set up (pip or conda)
* Option 1: use the supplied file `environment.yml` to create a new environment with conda
* Option 2: use the supplied file `requirements.txt` to create a new environment with pip
    
## Repositories
* Create a directory for the project and initialize git.
    * As you work on the code, continually commit changes. Trained models you want to use in production must be committed to GitHub.
* Connect your local git repo to GitHub.
* Setup GitHub Actions on your repo. You can use one of the pre-made GitHub Actions if at a minimum it runs pytest and flake8 on push and requires both to pass without error.
    * Make sure you set up the GitHub Action to have the same version of Python as you used in development.

# Data
* Download census.csv and commit it to dvc.
* This data is messy, try to open it in pandas and see what you get.
* To clean it, use your favorite text editor to remove all spaces.

# Model
* Using the starter code, write a machine learning model that trains on the clean data and saves the model. Complete any function that has been started.
* Write unit tests for at least 3 functions in the model code.
* Write a function that outputs the performance of the model on slices of the data.
    * Suggestion: for simplicity, the function can just output the performance on slices of just the categorical features.
* Write a model card using the provided template.

# API Creation
*  Create a RESTful API using FastAPI this must implement:
    * GET on the root giving a welcome message.
    * POST that does model inference.

# GitHub Link 

# Sources
Actions. (n.d.). GitHub - actions/starter-workflows: Accelerating new GitHub Actions workflows. GitHub. https://github.com/actions/starter-workflows
Archana, D. (2022, January 19). Training set and test set size. Data Science. Retrieved August 21, 2026, from https://datascience.stackexchange.com/questions/97613/training-set-and-test-set-size
Benjumea, Y. D. M. (2023, November 24). Simplifying unit testing in machine learning with Python. medium.com. Retrieved August 22, 2026, from https://medium.com/@ydmarinb/simplifying-unit-testing-in-machine-learning-with-python-df9b9c1a3300
Building and testing Python - GitHub Docs. (n.d.-a). GitHub Docs. https://docs.github.com/en/actions/tutorials/build-and-test-code/python?utm
Building and testing Python - GitHub Docs. (n.d.-b). GitHub Docs. https://docs.github.com/en/actions/tutorials/build-and-test-code/python?utm_source
Classification: Accuracy, recall, precision, and related metrics. (n.d.). Google for Developers. https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall
Client Script - an Overview | Online Help - Zoho CRM. (n.d.). Zoho. https://www.zoho.com/crm/developer/docs/client-script/overview.html
Docs | ServiceNow. (n.d.). https://www.servicenow.com/docs/r/xanadu/application-development/scripts/client-scripts.html
Fox, S. (2018, December 3). Scikit-Learn’s LabelBinarizer vs. OneHotEncoder. StackOverflow. Retrieved August 21, 2026, from https://stackoverflow.com/questions/50473381/scikit-learns-labelbinarizer-vs-onehotencoder
GeeksforGeeks. (2025, July 15). Python unittest assertIsInstance() function. GeeksforGeeks. https://geeksforgeeks.org/python/python-unittest-assertisinstance-function/
Get Started with DVC. (n.d.). Data Version Control · DVC. https://doc.dvc.org/start
Hyperparameter tuning. (2026, June 26). Geeksforgeeks. Retrieved August 22, 2026, from https://www.geeksforgeeks.org/machine-learning/hyperparameter-tuning/
Index - Uvicorn. (n.d.). https://uvicorn.dev/
in-n-out.cloud. (2017, January 30). What is Flake8, and why should we use it? www.medium.com. Retrieved August 21, 2026, from https://medium.com/python-pandemonium/what-is-flake8-and-why-we-should-use-it-b89bd78073f2
LabelBinarizer. (n.d.). Scikit-learn. https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html
Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., & Gebru, T. (2019). Model cards for model reporting. Proceedings of the Conference on Fairness, Accountability, and Transparency, 220–229. https://doi.org/10.1145/3287560.3287596
Nepali, S. (2024, August 26). Understanding the ISinstance() function in Python. medium.com. Retrieved August 22, 2026, from 
https://medium.com/@sunilnepali844/understanding-the-isinstance-function-in-python-9f254be49e0a
OpenAI. (202). ChatGPT (Aug 22 version) [Large language model]. https://chat.openai.com [1, 2, 3] 
pickle. (n.d.). Real Python. Retrieved August 22, 2026, from https://realpython.com/ref/stdlib/pickle/
pickle — Python object serialization. (n.d.). Python Documentation. https://docs.python.org/3/library/pickle.html
Pieters, M. (2013, April 22). I am confused with PROJECT_PATH = os.path.abspath(os.path.dirname(__file__)). StackOverflow. Retrieved August 21, 2026, from https://stackoverflow.com/questions/16157359/i-am-confused-with-project-path-os-path-abspathos-path-dirname-file
pytest documentation. (n.d.). https://docs.pytest.org/en/stable/
pytest vs Unittest, Which is Better? (2023, February 17). JetBrains Guide. https://www.jetbrains.com/guide/pytest/links/pytest-v-unittest/
Salerno, A. (2020, May 25). Pickling in Python. medium.com. Retrieved August 21, 2026, from https://medium.com/swlh/pickling-in-python-ac3c7a045ae5
Soni, H. (2022, March 29). OneHotEncoding vs LabelEncoder vs Pandas GetDummies — how and why? medium.com. Retrieved August 21, 2026, from https://harshal-soni.medium.com/onehotencoding-vs-labelencoder-vs-pandas-get-dummies-how-and-why-b190dff7a86f
Team, T. (2024, October 22). Pytest vs Unittest: A Comparison. https://trunk.io/learn/pytest-vs-unittest-a-comparison
Tech With Tim. (2025, February 25). Please learn how to write tests in Python. . . • Pytest tutorial [Video]. YouTube. https://www.youtube.com/watch?v=EgpLj86ZHFQ
UCI Machine Learning Repository. (n.d.). https://archive.ics.uci.edu/dataset/20/census+income
Udacity. (2026). Marvin AI [Large language model]. Udacity.
Workflow syntax for GitHub Actions A workflow is a configurable automated process made up of one or more jobs. You must create a YAML file to define your workflow configuration. (n.d.). github.com. Retrieved August 21, 2026, from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax

