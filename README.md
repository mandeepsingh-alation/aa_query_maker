<p align="center"><img src ="logo.png" /></p>

# Alation Analytics: Object Query Maker

## Purpose

This utility takes in the field_id and field_datatype value for each property of an Alation object stored in Alation Analytics (V R6 and below) and produces a complete query. Once you run the code, the query will automatically be added to your clipboard. All you need to do is paste it into compose.

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