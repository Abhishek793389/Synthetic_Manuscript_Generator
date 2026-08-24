SYNTHETIC INDIC MANUSCRIPT GENERATOR
INSTALLATION AND RUN INSTRUCTIONS
==================================

1. REQUIREMENTS
---------------

Required:

- Python 3.10 or newer
- Git
- Windows PowerShell or Command Prompt


2. CLONE THE REPOSITORY
-----------------------

Open PowerShell and run:

git clone https://github.com/Abhishek793389/Synthetic_Manuscript_Generator.git

Move into the project directory:

cd Synthetic_Manuscript_Generator


3. CREATE VIRTUAL ENVIRONMENT
-----------------------------

Create a Python virtual environment:

python -m venv venv

Activate the virtual environment:

.\venv\Scripts\Activate.ps1

After activation, the terminal should show:

(venv)


If PowerShell prevents activation, run:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Then activate again:

.\venv\Scripts\Activate.ps1


4. INSTALL DEPENDENCIES
-----------------------

Install all required Python packages:

pip install -r requirements.txt


5. VERIFY THE PROJECT FILES
---------------------------

Make sure the following files/directories exist:

generate.py

requirements.txt

input/
    devanagari.md
    modi.md
    sharada.md

fonts/
    devanagari/
        NotoSansDevanagari-Regular.ttf
    modi/
        NotoSansModi-Regular.ttf
    sharada/
        NotoSansSharada-Regular.ttf

src/
    annotation.py
    background.py
    effects.py
    renderer.py
    text_loader.py


6. RUN THE GENERATOR
--------------------

Make sure the virtual environment is activated.

Run:

python generate.py


7. DATASET GENERATION
---------------------

The generator automatically creates manuscript images for:

- Sharada
- Devanagari
- Modi

Each script generates 100 images.

Total:

300 images


8. OUTPUT
---------

Generated files are saved inside:

output/dataset/


The directory structure is:

output/
    dataset/
        sharada/
            train/
            validation/
            test/

        devanagari/
            train/
            validation/
            test/

        modi/
            train/
            validation/
            test/


9. IMAGE AND ANNOTATION FILES
-----------------------------

Every generated image has a corresponding Markdown annotation file.

Example:

sharada_0001.png
sharada_0001.md

The image and annotation use the same filename so that they remain synchronized.


10. DATASET SPLIT
-----------------

For each script:

Train      : 85 images
Validation : 10 images
Test       : 5 images
Total      : 100 images

For all three scripts:

Total      : 300 images


11. RUN AGAIN
-------------

To generate another dataset, simply run:

python generate.py

The generator uses random seeds to create variations in:

- Paper texture
- Paper aging
- Stains
- Folds
- Ink color
- Text position
- Highlights
- Marginal annotations
- Manuscript imperfections


12. TROUBLESHOOTING
-------------------

If Python is not recognized:

Check:

python --version

If dependencies are missing:

pip install -r requirements.txt

If a font error occurs:

Check that the required .ttf files exist inside the fonts/ directory.

If an input file error occurs:

Check that the required .md files exist inside the input/ directory.


13. QUICK START
---------------

For a fresh installation:

git clone https://github.com/Abhishek793389/Synthetic_Manuscript_Generator.git

cd Synthetic_Manuscript_Generator

python -m venv venv

.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

python generate.py


The generated dataset will be available at:

output/dataset/
