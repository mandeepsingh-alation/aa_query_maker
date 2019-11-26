from string import Template
from pyperclip import copy

# A data packet example is given below
# format: "{field: [field_id, field datatype]}" 
###################################################
# THESE ARE THE ONLY SETTINGS YOU NEED TO CHANGE
data_dict = {'ds_id':[3147,'integer_value'],
             'ds_private':[3255,'boolean_value'],
             'ds_title':[3,'text_value']}
object_name = 'datasource'
object_type_id = 7
###################################################
# setup the data packets and parameters
attrs_dict = dict(zip(data_dict.keys(),list(map(lambda x: x[0],data_dict.values()))))
type_dict = dict(zip(data_dict.keys(),list(map(lambda x: x[1],data_dict.values()))))

# placeholders for data
full_join_block = ''
full_where_block = ''
full_select_block = ''

# Base query skeleton
base_template = Template("""SELECT
    AO.*,
$select_block
FROM
    public.alation_object AS AO
$join_block
WHERE
    AO.object_type_id = $object_type_id
$where_block;
""")

# Select block template
select_template = Template("""    FV_$name.$a_type AS $name,""")

# Join block template
join_template = Template("""
-- Get $field_name for the $object_name
JOIN
    public.object_field_value AS OFV_$field_name
    ON
        AO.object_uuid = OFV_$field_name.object_uuid
    AND
        AO.object_type_id = OFV_$field_name.object_type_id
-- Get field value
JOIN
    public.field_value AS FV_$field_name
    ON
        OFV_$field_name.value_fp = FV_$field_name.value_fp
""")

# Where block template
where_template = Template("""
AND
    -- get only field_id = $field_id, $field_name
    OFV_$field_name.field_id = $field_id""")

# build join statements
for each in attrs_dict.keys():
    full_join_block = full_join_block + join_template.substitute(field_name=each,object_name=object_name)

# build where statements
for field_name, field_id in attrs_dict.items():
    full_where_block = full_where_block + where_template.substitute(field_name=field_name,field_id=field_id)

# build select statements
for attr,attr_type in type_dict.items():
    full_select_block = full_select_block + select_template.substitute(name=attr,a_type=attr_type) + '\n'

full_select_block = full_select_block[:-2] + '\n'

full_query = base_template.substitute(select_block = full_select_block,
                                      join_block = full_join_block,
                                      object_type_id = object_type_id,
                                      where_block = full_where_block)

copy(full_query)
# now paste the query into compose or text editor