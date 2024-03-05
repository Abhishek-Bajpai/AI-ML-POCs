#Image build -> 
docker build -t abhirajbajpai/ai-imagerecognition-app .

#Run container ->  Here my data folder is mapped as volume while spinning container.. thats where my training and test data is located..outside container env
docker run -p 5000:5000 -v ImageIdentification-CNN_POC\data:/app/data abhirajbajpai/ai-imagerecognition-app

#My app.py is fetching the labels from mapped directory like so... mapped volumn is accessible from WORKDIR
class_labels = sorted(os.listdir("/app/data/training/people"))        
