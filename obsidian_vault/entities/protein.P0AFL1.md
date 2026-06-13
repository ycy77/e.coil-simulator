---
entity_id: "protein.P0AFL1"
entity_type: "protein"
name: "potI"
source_database: "UniProt"
source_id: "P0AFL1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "potI b0857 JW0841"
---

# potI

`protein.P0AFL1`

## Static

- Type: `protein`
- Source: `UniProt:P0AFL1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex PotFGHI involved in putrescine uptake (PubMed:23719730, PubMed:8416922). Responsible for the translocation of the substrate across the membrane (Probable). Imports putrescine for maintenance of the optimal concentration of polyamines necessary for cell growth in the presence of glucose (PubMed:23719730). {ECO:0000269|PubMed:23719730, ECO:0000269|PubMed:8416922, ECO:0000305}. potI encodes one of two integral membrane subunits of an ATP-dependent putrescine uptake system; PotI is predicted to contain 6 transmembrane regions; PotI has 37% sequence similarity with PotC - the integral membrane subunit of the spermidine ABC transporter PotABCD

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

- `encodes` <-- [[gene.b0857|gene.b0857]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFL1`
- `KEGG:ecj:JW0841;eco:b0857;ecoc:C3026_05345;`
- `GeneID:89520233;945485;`
- `GO:GO:0005886; GO:0015417; GO:0015847; GO:0016020; GO:0043190; GO:0055052`

## Notes

Putrescine transport system permease protein PotI
