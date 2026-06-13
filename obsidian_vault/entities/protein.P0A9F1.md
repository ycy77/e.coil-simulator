---
entity_id: "protein.P0A9F1"
entity_type: "protein"
name: "mntR"
source_database: "UniProt"
source_id: "P0A9F1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mntR ybiQ b0817 JW0801"
---

# mntR

`protein.P0A9F1`

## Static

- Type: `protein`
- Source: `UniProt:P0A9F1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: In the presence of manganese, represses expression of mntH and mntS. Up-regulates expression of mntP. {ECO:0000269|PubMed:11466284, ECO:0000269|PubMed:21908668}.

## Biological Role

Component of MntR-Mn2+ DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7672), MntR-Mn2+ (complex.ecocyc.CPLX0-7701).

## Annotation

FUNCTION: In the presence of manganese, represses expression of mntH and mntS. Up-regulates expression of mntP. {ECO:0000269|PubMed:11466284, ECO:0000269|PubMed:21908668}.

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7672|complex.ecocyc.CPLX0-7672]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7701|complex.ecocyc.CPLX0-7701]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b2392|gene.b2392]] `RegulonDB` `S` - regulator=MntR; target=mntH; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0817|gene.b0817]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9F1`
- `KEGG:ecj:JW0801;eco:b0817;ecoc:C3026_05140;`
- `GeneID:93776610;945437;`
- `GO:GO:0003677; GO:0003700; GO:0005737; GO:0030145; GO:0045892; GO:0046983; GO:2000144`

## Notes

Transcriptional regulator MntR (Manganese transport regulator)
