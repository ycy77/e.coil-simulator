---
entity_id: "protein.P76142"
entity_type: "protein"
name: "lsrB"
source_database: "UniProt"
source_id: "P76142"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lsrB yneA b1516 JW1509"
---

# lsrB

`protein.P76142`

## Static

- Type: `protein`
- Source: `UniProt:P76142`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex LsrABCD involved in autoinducer 2 (AI-2) import. Binds AI-2 and delivers it to the LsrC and LsrD permeases (Probable). {ECO:0000305|PubMed:15601708}. Based on sequence similarity lsrB is predicted to encode the periplasmic binding protein of an AI-2 ABC transporter . lsrB is overexpressed in E. coli biofilms compared to planktonic growth in exponential phase . LsrB binds the chemically synthesized probe D-desthiobiotin-AI-2 . A ΔlsrB::aphA strain is impaired in biofilm formation .

## Biological Role

Component of Autoinducer-2 ABC transporter (complex.ecocyc.ABC-58-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex LsrABCD involved in autoinducer 2 (AI-2) import. Binds AI-2 and delivers it to the LsrC and LsrD permeases (Probable). {ECO:0000305|PubMed:15601708}.

## Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-58-CPLX|complex.ecocyc.ABC-58-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1516|gene.b1516]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76142`
- `KEGG:ecj:JW1509;eco:b1516;ecoc:C3026_08765;`
- `GeneID:945418;`
- `GO:GO:0009372; GO:0016020; GO:0042597; GO:0055052; GO:0055085; GO:1905887`

## Notes

Autoinducer 2-binding protein LsrB (AI-2-binding protein LsrB)
