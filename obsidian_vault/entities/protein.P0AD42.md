---
entity_id: "protein.P0AD42"
entity_type: "protein"
name: "pgpC"
source_database: "UniProt"
source_id: "P0AD42"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:21148555}; Single-pass membrane protein {ECO:0000269|PubMed:21148555}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pgpC yfhB b2560 JW5408"
---

# pgpC

`protein.P0AD42`

## Static

- Type: `protein`
- Source: `UniProt:P0AD42`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:21148555}; Single-pass membrane protein {ECO:0000269|PubMed:21148555}.

## Enriched Summary

FUNCTION: Lipid phosphatase which dephosphorylates phosphatidylglycerophosphate (PGP) to phosphatidylglycerol (PG). {ECO:0000269|PubMed:21148555}. E.coli contains three phosphatidylglycerophosphatases - EG10704 "PgpA", PGPPHOSPHAB-MONOMER "PgpB" and PgpC - which catalyse the dephosphorylation of phosphatidylglycerol phosphate (PGP) to phosphatidylglycerol (PG), an essential phospholipid of the inner and outer membrane in E. coli. PgpA and PgpC appear to be specific for PGP whereas PgpB is a multifunctional enzyme that is also active on undecaprenyl diphosphate, phosphatidicic acid and lysophosphatidic acid . pgpC is essential for growth in a pgpApgpB mutant but not in wild type cells . A pgpApgpBpgpC triple mutant is not viable but can be generated with a complementing plasmid containing any one of the three phosphatidylglycerophosphatases. A triple mutant complemented with any one of pgpA, pgpB or pgpC expressed on a temperature sensitive plasmid is viable at 30°C but not at 42°C . Lipid profiling of these strains showed accumulation of PGP and disappearance of PG when shifted from 30°C to 42°C . Overexpression of pgpC from a plasmid results in increased phosphatidylglycerophosphatase activity compared to the wild type . The activity of PgpC is temperature sensitive with significant reduction observed at 42°C compared to 30°C...

## Biological Role

Catalyzes PGPPHOSPHA-RXN (reaction.ecocyc.PGPPHOSPHA-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

FUNCTION: Lipid phosphatase which dephosphorylates phosphatidylglycerophosphate (PGP) to phosphatidylglycerol (PG). {ECO:0000269|PubMed:21148555}.

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PGPPHOSPHA-RXN|reaction.ecocyc.PGPPHOSPHA-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2560|gene.b2560]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AD42`
- `KEGG:ecj:JW5408;eco:b2560;ecoc:C3026_14170;`
- `GeneID:93774575;947026;`
- `GO:GO:0005886; GO:0006655; GO:0008962; GO:0009395; GO:0046474; GO:0046872`
- `EC:3.1.3.27`

## Notes

Phosphatidylglycerophosphatase C (EC 3.1.3.27) (Phosphatidylglycerolphosphate phosphatase C) (PGP phosphatase C)
