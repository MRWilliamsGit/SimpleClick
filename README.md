# SimpleClick

This is a simple project that demonstrates how to interact with a maching learning model from the command line using the Click python package.

The model used is the pretrained GPT-2 model pulled from Hugging Face

## How To Use:

#### Step 1: Clone this repo to the development environment of your choice.
#### Setp 2: Install all dependancies from requirements.txt.

It is best practice to establish a virtual environment first. Use the command line to navigate to the folder containing these files, and then, if your environment supports Makefile:

```
make all
```

You can also install directly using pip:

```
pip install -r requirements.txt
```

#### Step 3: Run the program 

```
python clickmodel.py
```

The program will print a welcome message and prompt you to type in any text you wish. To exit the loop, type "hush"

## Example Command Line Results


## References

Click: https://click.palletsprojects.com/en/8.1.x/
GPT-2: https://huggingface.co/gpt2
