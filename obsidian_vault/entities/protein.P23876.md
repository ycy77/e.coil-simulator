---
entity_id: "protein.P23876"
entity_type: "protein"
name: "fepD"
source_database: "UniProt"
source_id: "P23876"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:1479347, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fepD b0590 JW0582"
---

# fepD

`protein.P23876`

## Static

- Type: `protein`
- Source: `UniProt:P23876`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:1479347, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex FepBDGC involved in ferric enterobactin uptake (PubMed:1479347, PubMed:1838574). Responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:1479347, ECO:0000269|PubMed:1838574, ECO:0000305}. FepD is the predicted integral membrane subunit of a ferrric enterobactin ABC transporter complex; insertional inactivation of fepD results in the loss of ferric eneterobactin uptake .

## Biological Role

Component of ferric enterobactin ABC transporter (complex.ecocyc.ABC-10-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex FepBDGC involved in ferric enterobactin uptake (PubMed:1479347, PubMed:1838574). Responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:1479347, ECO:0000269|PubMed:1838574, ECO:0000305}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-10-CPLX|complex.ecocyc.ABC-10-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0590|gene.b0590]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23876`
- `KEGG:ecj:JW0582;eco:b0590;ecoc:C3026_02945;`
- `GeneID:945214;`
- `GO:GO:0005886; GO:0015620; GO:0015685; GO:0016020; GO:0022857; GO:0033212; GO:0033214; GO:0055052`

## Notes

Ferric enterobactin transport system permease protein FepD
