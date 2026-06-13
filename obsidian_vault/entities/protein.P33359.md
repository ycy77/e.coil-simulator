---
entity_id: "protein.P33359"
entity_type: "protein"
name: "yehW"
source_database: "UniProt"
source_id: "P33359"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yehW b2128 JW2116"
---

# yehW

`protein.P33359`

## Static

- Type: `protein`
- Source: `UniProt:P33359`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of an ABC transporter complex involved in low-affinity glycine betaine uptake. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:26325238}. YehW is the predicted, integral inner membrane component of a low affinity glycine betaine ABC transporter .

## Biological Role

Component of glycine betaine ABC transporter, non-osmoregulatory (complex.ecocyc.ABC-40-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of an ABC transporter complex involved in low-affinity glycine betaine uptake. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:26325238}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-40-CPLX|complex.ecocyc.ABC-40-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2128|gene.b2128]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33359`
- `KEGG:ecj:JW2116;eco:b2128;ecoc:C3026_11935;`
- `GeneID:949028;`
- `GO:GO:0005886; GO:0006865; GO:0015838; GO:0016020; GO:0031460; GO:0055052; GO:0055085`

## Notes

Glycine betaine uptake system permease protein YehW
