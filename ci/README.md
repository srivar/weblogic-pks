# WLS PKS CI

Here is some information on accepting the Oracle license so we can automate the product download
* https://stackoverflow.com/questions/10268583/downloading-java-jdk-on-linux-via-wget-is-shown-license-page-instead#

Below is a sample deployment of the pipeline where passwords are entered since they're not in the properties.yml file.
```
fly -t homelab set-pipeline -p wls-pks -c pipeline.yml -v "docker-hub-password=YOUR_PASSWORD" -v "git-private-key=$(cat id_rsa)" -l properties.yml
```
