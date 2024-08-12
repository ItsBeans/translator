To run the web application from the file.

Ensure you have python already downloaded, python 3.9.0 was used for this project.

Open the command prompt on your computer.

Open the directory in which you have downloaded the files in.  For example by doing:

cd downloads
cd projectFinal


Run the following commands in order:

pip install -r requirements.txt 
python manage.py migrate 
python manage.py runserver

Then it will tell you the link for the local host of the website, copy this into a browser of your choice. 

The link should be http://127.0.0.1:8000/

Now you have access to the web application

______________________________

The 'notebooks'  folder is not needed for the web application but holds the jupyter notebooks used when evaluating the 
accuracy of the models with the 2 test data sets, aswell as also evaluating their inference time. It also
includes the notebook for fine-tuning the existing models, using the trainer API from hugging face to do so. 
The same notebook was used for the different models and also adapted for different datasets as data processing had to be done 
differently with each one.
