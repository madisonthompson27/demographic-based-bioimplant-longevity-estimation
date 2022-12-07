# demographic-based-bioimplant-longevity-estimation (DBBLE)
Code that uses equations from two years of research to predict the BMD, bone volume, and bone mass of a patient's bone dependent on their age, race, gender, exercise, and nutrition.

Research (complete): https://drive.google.com/drive/folders/1AUdU2NJc5TyBJ38FE-GmBR4poLSCYKqR?usp=sharing

Research (in progress): https://drive.google.com/drive/folders/1GasxbkWZZKTjtb5i69ugg3woIakA3C4d?usp=sharing

Folders contain the following: 

Databases: values from meta-analyses and user inputs that are within two standard devaitions of the meta-analysis provided value at a ninety-nine percent confidence interval. 
    Contain values for elastic modulus, cross-sectional area, height, weight, BMI, BMD decay rate, and BMD starting value dependent on age, race, and gender. 

Devnotes: development notes, labeled by project and sorted by date. 

Equations: contain the equations used to calculate expected bone change by volume, mass, and density. 

GUI: contains the files that allow backend code to be implemented in a user-friendly fashion. 

Modeling: contains the files that alter a 3D render of a patient's bone based on their expected bone change by volume, mass, and density. 

Persistance: allows medical practitioners to login, access patient records, update patient records. 

For all folders above, files will be added as they are written. 