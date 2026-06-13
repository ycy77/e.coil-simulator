---
entity_id: "protein.P20083"
entity_type: "protein"
name: "parE"
source_database: "UniProt"
source_id: "P20083"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "parE nfxD b3030 JW2998"
---

# parE

`protein.P20083`

## Static

- Type: `protein`
- Source: `UniProt:P20083`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Topoisomerase IV is essential for chromosome segregation; it is the principal protein responsible for decatenating newly replicated chromosomes (PubMed:9334322). It relaxes supercoiled DNA (PubMed:15105144, PubMed:21300644, PubMed:23294697, PubMed:23352267). MukB stimulates the relaxation activity of topoisomerase IV and also has a modest effect on decatenation (PubMed:20921377). {ECO:0000269|PubMed:15105144, ECO:0000269|PubMed:20921377, ECO:0000269|PubMed:21300644, ECO:0000269|PubMed:23294697, ECO:0000269|PubMed:23352267, ECO:0000269|PubMed:9334322}. The crystal structures of two N-terminal fragments of ParE have been solved .

## Biological Role

Component of DNA topoisomerase IV (complex.ecocyc.CPLX0-2424).

## Annotation

FUNCTION: Topoisomerase IV is essential for chromosome segregation; it is the principal protein responsible for decatenating newly replicated chromosomes (PubMed:9334322). It relaxes supercoiled DNA (PubMed:15105144, PubMed:21300644, PubMed:23294697, PubMed:23352267). MukB stimulates the relaxation activity of topoisomerase IV and also has a modest effect on decatenation (PubMed:20921377). {ECO:0000269|PubMed:15105144, ECO:0000269|PubMed:20921377, ECO:0000269|PubMed:21300644, ECO:0000269|PubMed:23294697, ECO:0000269|PubMed:23352267, ECO:0000269|PubMed:9334322}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2424|complex.ecocyc.CPLX0-2424]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3030|gene.b3030]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P20083`
- `KEGG:ecj:JW2998;eco:b3030;ecoc:C3026_16550;`
- `GeneID:93778963;947501;`
- `GO:GO:0003677; GO:0003918; GO:0005524; GO:0005694; GO:0005829; GO:0006265; GO:0007059; GO:0007062; GO:0009330; GO:0030541; GO:0046677; GO:0046872; GO:0051276`
- `EC:5.6.2.2`

## Notes

DNA topoisomerase 4 subunit B (EC 5.6.2.2) (Topoisomerase IV subunit B)
