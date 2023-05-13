# Kyiv weather

## The principle of the parser

The parser is organized in a separate Celery task scheduler. To offload synchronous Django and other tasks. The parser is launched every day at a certain time specified in the database, settings model (only one entry is created). When the parser is launched, the status of the task execution changes and a request is made to the site to collect information. Next comes data processing. It is checked by date whether there is already such a date, if yes, the record is updated, if not, a new record is created. After all this, the status changes back.

## Endpoints

```python
#Changing the start time of the parser for daily information (PUT)
/api/change-time-update
#Getting the weather for the last 5 days from the database (GET)
/api/get-weather-kiev
#Getting the execution status of the parser task (GET)
/api/get-status-parser
#Premature launch of the parser to collect information from the site (GET)
/api/run-parser
