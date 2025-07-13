# GCPFileDownload
How to connect and then download GCP file from local machine using python program
# Search Keyword
  I searched first with "how to read a google bucket file using python" and since I had to read the file line by line (that's the requirement) - I modified the search as "how to read a google bucket file using python line by line". And I got 2 different programs which I have combined into one and have attached that to this repository:
  However, most important thing for the program to run is Authentication. We can download \ read the file only if we could authenticate to the GCP Bucket, and following are the steps which are mentioned at CoPilot result.
  
  **Steps: 1**
  Install the library: Ensure you have the google-cloud-storage library installed. You can install it using: pip install google-cloud-storage

  **Copy the code: 2**  
  Set up authentication: Make sure you have authenticated your application with Google Cloud by setting the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of your service account key file:

  **Copy the code: 3**
  export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"
  Run the script: Replace your-bucket-name and path/to/your/file.txt with your actual bucket name and file path.

  This approach downloads the file content as text and processes it line by line. If the file is very large, consider using blob.download_to_file() to stream the content instead. Let me know if you'd like an example for that!

## Steps: 1 - 
  In order to install library - you just need to open VS Code (or any other editor) - and hit command "pip install google-clound-storage"

## Steps: 2 -
  As I was somewhat confused on Step2 - I again did the google search with keyword - "how to Download your Google Cloud service account key JSON file from the Google Cloud Console" - which gave me following results
  The UI is a little confusing, here is the step on how you can download the serviceAccount.json file:
  
    a) log in to your GCP account - https://console.cloud.google.com/iam-admin
    b) Go to the "IAM & Admin" -> Service Accounts section. As shown in below image - or else simple search service account in search bar
    (<img width="1098" height="445" alt="image" src="https://github.com/user-attachments/assets/ff839157-05b1-4c77-8711-0f4f2ba7112a" />)
    
    c) Create a new service account or Click on the existing service account. Click on 3 dots as shown in folloiwng image - and then click on Manage Keys.
    <img width="1857" height="216" alt="image" src="https://github.com/user-attachments/assets/5bbd3065-997f-43b7-98e6-b3154e3514a7" />

    d) Click on the "Keys" tab. Click on Add Key and Create New Key if key doesn't exists
    <img width="861" height="313" alt="image" src="https://github.com/user-attachments/assets/0c40cb31-c89b-4518-b4ae-3622ce3e36f8" />

    e) Click on "Add Key" -> Click on "Create new Key".
    f) Select "JSON" from the radio button
    <img width="551" height="356" alt="image" src="https://github.com/user-attachments/assets/02f3a2c3-7218-4773-b288-731525449511" />

    g) Click on the "Create" button
    h) It will create and download the service-account.json file in your system

  
  
