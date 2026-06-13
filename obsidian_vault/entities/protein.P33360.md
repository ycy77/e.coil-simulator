---
entity_id: "protein.P33360"
entity_type: "protein"
name: "yehX"
source_database: "UniProt"
source_id: "P33360"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yehX b2129 JW2117"
---

# yehX

`protein.P33360`

## Static

- Type: `protein`
- Source: `UniProt:P33360`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Part of an ABC transporter complex involved in low-affinity glycine betaine uptake. Probably responsible for energy coupling to the transport system. {ECO:0000269|PubMed:26325238}. YehX is the predicted, ATP binding component of a low affinity glycine betaine ABC transporter .

## Biological Role

Component of glycine betaine ABC transporter, non-osmoregulatory (complex.ecocyc.ABC-40-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of an ABC transporter complex involved in low-affinity glycine betaine uptake. Probably responsible for energy coupling to the transport system. {ECO:0000269|PubMed:26325238}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-40-CPLX|complex.ecocyc.ABC-40-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2129|gene.b2129]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33360`
- `KEGG:ecj:JW2117;eco:b2129;ecoc:C3026_11940;`
- `GeneID:946659;`
- `GO:GO:0005524; GO:0005886; GO:0006865; GO:0015838; GO:0016020; GO:0016887; GO:0031459; GO:0031460; GO:0055052`
- `EC:7.4.2.-`

## Notes

Glycine betaine uptake system ATP-binding protein YehX (EC 7.4.2.-)
