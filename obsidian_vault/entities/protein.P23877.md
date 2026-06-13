---
entity_id: "protein.P23877"
entity_type: "protein"
name: "fepG"
source_database: "UniProt"
source_id: "P23877"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:1479347, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fepG b0589 JW0581"
---

# fepG

`protein.P23877`

## Static

- Type: `protein`
- Source: `UniProt:P23877`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:1479347, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex FepBDGC involved in ferric enterobactin uptake (PubMed:1479347, PubMed:1838574). Responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:1479347, ECO:0000269|PubMed:1838574, ECO:0000305}. FepG is the predicted integral membrane subunit of a ferrric enterobactin ABC transporter complex; insertional inactivation of fepG results in the loss of ferric eneterobactin uptake .

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

- `encodes` <-- [[gene.b0589|gene.b0589]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23877`
- `KEGG:ecj:JW0581;eco:b0589;ecoc:C3026_02940;`
- `GeneID:945209;`
- `GO:GO:0005886; GO:0015620; GO:0015685; GO:0016020; GO:0022857; GO:0033212; GO:0033214; GO:0055052`

## Notes

Ferric enterobactin transport system permease protein FepG
