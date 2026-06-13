---
entity_id: "protein.P0AC23"
entity_type: "protein"
name: "focA"
source_database: "UniProt"
source_id: "P0AC23"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:20041954, ECO:0000269|PubMed:24659605, ECO:0000269|PubMed:33169422}; Multi-pass membrane protein {ECO:0000250|UniProtKB:P0AC25}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "focA ycaE b0904 JW0887"
---

# focA

`protein.P0AC23`

## Static

- Type: `protein`
- Source: `UniProt:P0AC23`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:20041954, ECO:0000269|PubMed:24659605, ECO:0000269|PubMed:33169422}; Multi-pass membrane protein {ECO:0000250|UniProtKB:P0AC25}.

## Enriched Summary

FUNCTION: Involved in the bidirectional transport of formate during mixed-acid fermentation (PubMed:23335413, PubMed:24659605, PubMed:30247527, PubMed:33169422, PubMed:35084298, PubMed:35377837, PubMed:35390794, PubMed:8022272). Functions to maintain relatively constant intracellular formate levels during growth, using different mechanisms for efflux and uptake of the anion (PubMed:35377837). Has a strong preference for formate as a substrate in vivo and not other acidic fermentation products (PubMed:23335413). {ECO:0000269|PubMed:23335413, ECO:0000269|PubMed:24659605, ECO:0000269|PubMed:30247527, ECO:0000269|PubMed:33169422, ECO:0000269|PubMed:35084298, ECO:0000269|PubMed:35377837, ECO:0000269|PubMed:35390794, ECO:0000269|PubMed:8022272}.

## Biological Role

Component of formate channel FocA (complex.ecocyc.CPLX0-7843).

## Annotation

FUNCTION: Involved in the bidirectional transport of formate during mixed-acid fermentation (PubMed:23335413, PubMed:24659605, PubMed:30247527, PubMed:33169422, PubMed:35084298, PubMed:35377837, PubMed:35390794, PubMed:8022272). Functions to maintain relatively constant intracellular formate levels during growth, using different mechanisms for efflux and uptake of the anion (PubMed:35377837). Has a strong preference for formate as a substrate in vivo and not other acidic fermentation products (PubMed:23335413). {ECO:0000269|PubMed:23335413, ECO:0000269|PubMed:24659605, ECO:0000269|PubMed:30247527, ECO:0000269|PubMed:33169422, ECO:0000269|PubMed:35084298, ECO:0000269|PubMed:35377837, ECO:0000269|PubMed:35390794, ECO:0000269|PubMed:8022272}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7843|complex.ecocyc.CPLX0-7843]] `EcoCyc` `database` - EcoCyc component coefficient=5 | EcoCyc protcplxs.col coefficient=5 | EcoCyc transporter component coefficient=5

## Incoming Edges (1)

- `encodes` <-- [[gene.b0904|gene.b0904]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC23`
- `KEGG:ecj:JW0887;eco:b0904;ecoc:C3026_05580;`
- `GeneID:93776514;945513;`
- `GO:GO:0005886; GO:0010447; GO:0015499; GO:0015724; GO:0019664; GO:0042802`

## Notes

Formate channel FocA (Formate transporter FocA)
