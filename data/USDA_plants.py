#retriever
from retriever.lib.templates import BasicTextTemplate
from retriever.lib.models import Table, Cleanup, correct_invalid_value

SCRIPT = BasicTextTemplate(tables={'PlantTaxonomy': Table('PlantTaxonomy', do_not_bulk_insert=True,columns=[('record_id', ('pk-auto',)), ('symbol', ('char', '7')), ('synonym_symbol', ('char', '7')), ('scientific_name', ('char',)), ('common_name', ('char', '50')), ('family', ('char', '30'))])},
                           name="USDA plants",
                           tags=['Taxon > Plants', 'Data Type > Taxonomy'],
                           ref="http://plants.usda.gov",
                           urls={'PlantTaxonomy': 'http://plants.usda.gov/java/downloadData?fileName=plantlst.txt&static=true'},
                           shortname="PlantTaxonomy",
                           description="Plant taxonomy system available on the USDA plants site.")