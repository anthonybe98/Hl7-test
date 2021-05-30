
# Mini Project 3 HL7v2 TO FHIR

## HL7v2 to JSON to FHIR

Small clinics that haven’t switched to FHIR have a lot HL7 v2 data that needs to be converted. 

## How to use it

First, download **Python 3** and **pip** on your machine.

In **Terminal.** run the following:

```shell
pip install hl7apy
pip install py-fhir 
```
Then run:

```shell
python main.py
python fhir1.py
```
If you want to use another HL7 message copy and paste it inside the main.py
## Result

After executing **main.py** file, you will see get a  "**data1.json**" that has the converted message. Then we will use a json file to convert it to FHIR which will then output another json file

## Future work needed

This is just a beginning for the HL7v2 to FHIR. The next step would be to parse the whole JSON document and form the whole FHIR message from it
