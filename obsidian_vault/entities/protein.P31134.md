---
entity_id: "protein.P31134"
entity_type: "protein"
name: "potG"
source_database: "UniProt"
source_id: "P31134"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "potG b0855 JW5818"
---

# potG

`protein.P31134`

## Static

- Type: `protein`
- Source: `UniProt:P31134`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex PotFGHI involved in putrescine uptake (PubMed:23719730, PubMed:8416922). Responsible for energy coupling to the transport system (PubMed:23719730). Imports putrescine for maintenance of the optimal concentration of polyamines necessary for cell growth in the presence of glucose (PubMed:23719730). {ECO:0000269|PubMed:23719730, ECO:0000269|PubMed:8416922}. potG encodes the predicted ATP-binding subunit of a putrescine uptake system; PotG contains signature motifs coserved in ATP-binding cassette (ABC) proteins . PotG has 42% sequence similarity with PotA - the ATP-binding subunit of the spermidine ABC transporter .

## Biological Role

Component of putrescine ABC transporter (complex.ecocyc.ABC-25-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex PotFGHI involved in putrescine uptake (PubMed:23719730, PubMed:8416922). Responsible for energy coupling to the transport system (PubMed:23719730). Imports putrescine for maintenance of the optimal concentration of polyamines necessary for cell growth in the presence of glucose (PubMed:23719730). {ECO:0000269|PubMed:23719730, ECO:0000269|PubMed:8416922}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-25-CPLX|complex.ecocyc.ABC-25-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0855|gene.b0855]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31134`
- `KEGG:ecj:JW5818;eco:b0855;ecoc:C3026_05335;`
- `GeneID:945476;`
- `GO:GO:0005524; GO:0005886; GO:0015594; GO:0015847; GO:0016020; GO:0016887; GO:0043190; GO:0055052; GO:0140359`
- `EC:7.6.2.16`

## Notes

Putrescine transport ATP-binding protein PotG (EC 7.6.2.16)
