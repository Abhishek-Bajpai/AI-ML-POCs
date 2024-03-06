#Image build -> 
docker build -t abhirajbajpai/ai_image_recognition .

docker push abhirajbajpai/ai_image_recognition

#Run container ->  Here my data folder is mapped as volume while spinning container.. thats where my training and test data is located..outside container env
docker run -p 5000:5000 -v C:\CloudEngineeringPOCs\AI-ML-Edureka\AIML_POCs\CNN_ImageIDed\data:/app/data abhirajbajpai/ai_image_recognition:v1

# AIML_POCs\ImageIdentification-CNN_POC\data
#My app.py is fetching the labels from mapped directory like so... mapped volumn is accessible from WORKDIR
class_labels = sorted(os.listdir("/app/data/training/people"))        

==========================================================================================
- Apply K8s resources
    - kubectl apply -f .\deployment.yaml
    - kubectl apply -f .\service.yaml

- To check pod level events 
    - Get POD ID - kubectl get pods -o wide
    - Check POD events - kubectl describe pod pod/ai-image-recognition-deployment-78fb66bbbb-8t626<<PID ID>>

- Verify Container Logs 
    - kubectl logs <<POD ID>> -c ai-image-recognition

- Remove deployment and service from cluster
    - kubectl delete deploy ai-image-recognition-deployment
    - kubectl delete svc ai-image-recognition-service
