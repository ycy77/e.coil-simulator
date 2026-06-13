---
entity_id: "protein.P0AFI2"
entity_type: "protein"
name: "parC"
source_database: "UniProt"
source_id: "P0AFI2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "parC b3019 JW2987"
---

# parC

`protein.P0AFI2`

## Static

- Type: `protein`
- Source: `UniProt:P0AFI2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein.

## Enriched Summary

FUNCTION: Topoisomerase IV is essential for chromosome segregation; it is the principal protein responsible for decatenating newly replicated chromosomes (PubMed:9334322). It relaxes supercoiled DNA (PubMed:12269820, PubMed:16023670, PubMed:21300644). MukB stimulates the relaxation activity of topoisomerase IV and also has a modest effect on decatenation (PubMed:20921377). {ECO:0000269|PubMed:12269820, ECO:0000269|PubMed:16023670, ECO:0000269|PubMed:20921377, ECO:0000269|PubMed:21300644, ECO:0000269|PubMed:9334322}. The purified ParC protein is a dimer in solution .

## Biological Role

Component of DNA topoisomerase IV (complex.ecocyc.CPLX0-2424).

## Annotation

FUNCTION: Topoisomerase IV is essential for chromosome segregation; it is the principal protein responsible for decatenating newly replicated chromosomes (PubMed:9334322). It relaxes supercoiled DNA (PubMed:12269820, PubMed:16023670, PubMed:21300644). MukB stimulates the relaxation activity of topoisomerase IV and also has a modest effect on decatenation (PubMed:20921377). {ECO:0000269|PubMed:12269820, ECO:0000269|PubMed:16023670, ECO:0000269|PubMed:20921377, ECO:0000269|PubMed:21300644, ECO:0000269|PubMed:9334322}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2424|complex.ecocyc.CPLX0-2424]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3019|gene.b3019]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFI2`
- `KEGG:ecj:JW2987;eco:b3019;ecoc:C3026_16495;`
- `GeneID:75173148;75203584;947499;`
- `GO:GO:0003677; GO:0003918; GO:0005524; GO:0005694; GO:0005737; GO:0005829; GO:0006265; GO:0007059; GO:0007062; GO:0009330; GO:0019897; GO:0030541`
- `EC:5.6.2.2`

## Notes

DNA topoisomerase 4 subunit A (EC 5.6.2.2) (Topoisomerase IV subunit A)
