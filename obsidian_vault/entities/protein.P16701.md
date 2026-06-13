---
entity_id: "protein.P16701"
entity_type: "protein"
name: "cysU"
source_database: "UniProt"
source_id: "P16701"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00441, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cysU cysT b2424 JW2417"
---

# cysU

`protein.P16701`

## Static

- Type: `protein`
- Source: `UniProt:P16701`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00441, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex CysAWTP (TC 3.A.1.6.1) involved in sulfate/thiosulfate import. Probably responsible for the translocation of the substrate across the membrane. CysU is one of two predicted inner membrane subunits of an ATP-dependent sulfate/thiosulfate uptake system; CysU contains 50% hydrophobic residues

## Biological Role

Component of thiosulfate/sulfate ABC transporter (complex.ecocyc.ABC-7-CPLX), sulfate/thiosulfate ABC transporter (complex.ecocyc.ABC-70-CPLX).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex CysAWTP (TC 3.A.1.6.1) involved in sulfate/thiosulfate import. Probably responsible for the translocation of the substrate across the membrane.

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ABC-7-CPLX|complex.ecocyc.ABC-7-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.ABC-70-CPLX|complex.ecocyc.ABC-70-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2424|gene.b2424]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16701`
- `KEGG:ecj:JW2417;eco:b2424;ecoc:C3026_13470;`
- `GeneID:93774707;946882;`
- `GO:GO:0005886; GO:0015419; GO:0015709; GO:0016020; GO:0035796; GO:1902358`

## Notes

Sulfate transport system permease protein CysT
