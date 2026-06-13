---
entity_id: "protein.P31135"
entity_type: "protein"
name: "potH"
source_database: "UniProt"
source_id: "P31135"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "potH b0856 JW0840"
---

# potH

`protein.P31135`

## Static

- Type: `protein`
- Source: `UniProt:P31135`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex PotFGHI involved in putrescine uptake (PubMed:23719730, PubMed:8416922). Responsible for the translocation of the substrate across the membrane (Probable). Imports putrescine for maintenance of the optimal concentration of polyamines necessary for cell growth in the presence of glucose (PubMed:23719730). {ECO:0000269|PubMed:23719730, ECO:0000269|PubMed:8416922, ECO:0000305}. potH encodes one of two integral membrane subunits of an ATP-dependent putrescine uptake system; PotH is predicted to contain 6 transmembrane regions; PotH has 37% sequence similarity with PotB - the integral membrane subunit of the spermidine ABC transporter PotABCD .

## Biological Role

Component of putrescine ABC transporter (complex.ecocyc.ABC-25-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex PotFGHI involved in putrescine uptake (PubMed:23719730, PubMed:8416922). Responsible for the translocation of the substrate across the membrane (Probable). Imports putrescine for maintenance of the optimal concentration of polyamines necessary for cell growth in the presence of glucose (PubMed:23719730). {ECO:0000269|PubMed:23719730, ECO:0000269|PubMed:8416922, ECO:0000305}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-25-CPLX|complex.ecocyc.ABC-25-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0856|gene.b0856]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31135`
- `KEGG:ecj:JW0840;eco:b0856;ecoc:C3026_05340;`
- `GeneID:945475;`
- `GO:GO:0005886; GO:0015417; GO:0015847; GO:0016020; GO:0043190; GO:0055052; GO:1903711`

## Notes

Putrescine transport system permease protein PotH
