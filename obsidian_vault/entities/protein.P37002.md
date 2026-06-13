---
entity_id: "protein.P37002"
entity_type: "protein"
name: "fluC"
source_database: "UniProt"
source_id: "P37002"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00454, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16429150}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00454, ECO:0000269|PubMed:16429150}. Note=Could be a dual-topology protein, which inserts into the membrane in two opposite orientations (PubMed:16429150). May form an antiparallel homodimer in the inner membrane (PubMed:16429150). {ECO:0000269|PubMed:16429150}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fluC crcB ybeI b0624 JW0619"
---

# fluC

`protein.P37002`

## Static

- Type: `protein`
- Source: `UniProt:P37002`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00454, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16429150}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00454, ECO:0000269|PubMed:16429150}. Note=Could be a dual-topology protein, which inserts into the membrane in two opposite orientations (PubMed:16429150). May form an antiparallel homodimer in the inner membrane (PubMed:16429150). {ECO:0000269|PubMed:16429150}.

## Enriched Summary

FUNCTION: Fluoride-specific ion channel (PubMed:25156118). Important for reducing fluoride concentration in the cell, thus reducing its toxicity (PubMed:22194412, PubMed:25156118). Required to counteract cytoplasmic fluoride accumulation driven by pH gradients across the bacterial inner membrane set up by mild acidification of the growth medium (PubMed:25156118). {ECO:0000269|PubMed:22194412, ECO:0000269|PubMed:25156118}.

## Biological Role

Component of F- channel (complex.ecocyc.CPLX0-8271).

## Annotation

FUNCTION: Fluoride-specific ion channel (PubMed:25156118). Important for reducing fluoride concentration in the cell, thus reducing its toxicity (PubMed:22194412, PubMed:25156118). Required to counteract cytoplasmic fluoride accumulation driven by pH gradients across the bacterial inner membrane set up by mild acidification of the growth medium (PubMed:25156118). {ECO:0000269|PubMed:22194412, ECO:0000269|PubMed:25156118}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8271|complex.ecocyc.CPLX0-8271]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0624|gene.b0624]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37002`
- `KEGG:ecj:JW0619;eco:b0624;ecoc:C3026_03120;`
- `GeneID:945798;`
- `GO:GO:0005886; GO:0046872; GO:0062054; GO:0140114; GO:1903424; GO:1903425`

## Notes

Fluoride-specific ion channel FluC (Fluoride exporter)
