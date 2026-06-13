---
entity_id: "protein.P18200"
entity_type: "protein"
name: "pgpA"
source_database: "UniProt"
source_id: "P18200"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:21148555}; Multi-pass membrane protein {ECO:0000269|PubMed:21148555}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pgpA yajN b0418 JW0408"
---

# pgpA

`protein.P18200`

## Static

- Type: `protein`
- Source: `UniProt:P18200`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:21148555}; Multi-pass membrane protein {ECO:0000269|PubMed:21148555}.

## Enriched Summary

FUNCTION: Lipid phosphatase which dephosphorylates phosphatidylglycerophosphate (PGP) to phosphatidylglycerol (PG). {ECO:0000269|PubMed:20485265, ECO:0000269|PubMed:21148555, ECO:0000269|PubMed:2846510, ECO:0000269|PubMed:6296050}. E.coli contains three phosphatidylglycerophosphatases - PgpA, PGPPHOSPHAB-MONOMER "PgpB" and EG11371 "PgpC" - which catalyse the dephosphorylation of phosphatidylglycerol phosphate (PGP) to phosphatidylglycerol (PG), an essential phospholipid of the inner and outer membrane in E. coli. PgpA and PgpC appear to be specific for PGP whereas PgpB is a multifunctional enzyme that is also active on undecaprenyl diphosphate, phosphatidicic acid and lysophosphatidic acid . A pgpApgpBpgpC triple mutant is not viable but can be generated with a complementing plasmid containing any one of the three phosphatidylglycerophosphatases. A triple mutant complemented with any one of pgpA, pgpB or pgpC expressed on a temperature sensitive plasmid is viable at 30°C but not at 42°C . Lipid profiling of these strains showed accumulation of PGP and disappearance of PG when shifted from 30°C to 42°C . Overexpression of pgpA from a plasmid results in increased phosphatidylglycerophosphatase activity compared to the wild type . PgpA contains a single transmembrane segment and an active site that faces the cytoplasm .

## Biological Role

Catalyzes PGPPHOSPHA-RXN (reaction.ecocyc.PGPPHOSPHA-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Lipid phosphatase which dephosphorylates phosphatidylglycerophosphate (PGP) to phosphatidylglycerol (PG). {ECO:0000269|PubMed:20485265, ECO:0000269|PubMed:21148555, ECO:0000269|PubMed:2846510, ECO:0000269|PubMed:6296050}.

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PGPPHOSPHA-RXN|reaction.ecocyc.PGPPHOSPHA-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0418|gene.b0418]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P18200`
- `KEGG:ecj:JW0408;eco:b0418;ecoc:C3026_02040;`
- `GeneID:93777042;947542;`
- `GO:GO:0005886; GO:0006655; GO:0008962; GO:0009395; GO:0032026; GO:0042577; GO:0046474; GO:0046839; GO:0046872`
- `EC:3.1.3.27`

## Notes

Phosphatidylglycerophosphatase A (EC 3.1.3.27) (Phosphatidylglycerolphosphate phosphatase A) (PGP phosphatase A)
