<p align="center"><img src ="logo.png" /></p>

# Alation Analytics: Object Query Maker

## Purpose

This utility takes in the field_id and field_datatype value for each property of an Alation object stored in Alation Analytics (V R6 and below) and produces a complete query. Once you run the code, the query will automatically be added to your clipboard. All you need to do is paste it into compose.

## Input Data

The query is produced based on a data packet which looks like:

```python
object_name = 'datasource'
object_type_id = 7
```
In the parameters above, it does not matter what you enter for ```object_name```, but getting the correct ```object_type_id``` is important.

```python
data_dict = {'ds_id':[3147,'integer_value'],
             'ds_private':[3255,'boolean_value'],
             'ds_title':[3,'text_value']}
```
The name/key for the dictionary doesn't matter. We simply need the ```field_id``` and ```field_datatype``` values for the object we are creating the query for.


## How to find the field_id and field_datatype

### Run the following in compose to get a mapping for your object

```sql
SELECT DISTINCT
    OFV.field_id,
    OBF.field_name,
    OBF.field_datatype
FROM
    public.object_field_value AS OFV
JOIN
    public.object_field AS OBF
    ON
        OFV.field_id = OBF.field_id
WHERE
    OFV.object_type_id = ${Object Type ID | E.g. Article = 0};
```

Please refer to Alation's [Help Center](https://alationhelp.zendesk.com/hc/en-us/sections/360003193413-Alation-Analytics) for complete documention for Alation Analytics.