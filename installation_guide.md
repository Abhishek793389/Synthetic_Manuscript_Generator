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

Create a Python virtual environment


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
