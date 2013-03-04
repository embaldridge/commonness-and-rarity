#retriever
from retriever.lib.templates import BasicTextTemplate
from retriever.lib.models import Table, Cleanup, correct_invalid_value

SCRIPT = BasicTextTemplate(tables={},
                           name="Mammal Community DataBase (Ecological Archives 2011)",
                           tags=['Taxon > Mammals', 'Spatial Scale > Global', 'Data Type > Observational'],
                           ref="http://esapubs.org/archive/ecol/E092/201/",
                           urls={'communities': 'http://esapubs.org/archive/ecol/E092/201/data/MCDB_communities.csv', 'trapping': 'http://esapubs.org/archive/ecol/E092/201/data/MCDB_trapping.csv', 'references': 'http://esapubs.org/archive/ecol/E092/201/data/MCDB_references.csv', 'sites': 'http://esapubs.org/archive/ecol/E092/201/data/MCDB_sites.csv', 'species': 'http://esapubs.org/archive/ecol/E092/201/data/MCDB_species.csv'},
                           shortname="MCDB",
                           description="Katherine M. Thibault, Sarah R. Supp, Mikaelle Giffin, Ethan P. White, and S. K. Morgan Ernest. 2011. Species composition and abundance of mammalian communities. Ecology 92:2316.")