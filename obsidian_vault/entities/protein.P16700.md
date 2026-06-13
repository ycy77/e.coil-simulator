---
entity_id: "protein.P16700"
entity_type: "protein"
name: "cysP"
source_database: "UniProt"
source_id: "P16700"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cysP b2425 JW2418"
---

# cysP

`protein.P16700`

## Static

- Type: `protein`
- Source: `UniProt:P16700`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex CysAWTP (TC 3.A.1.6.1) involved in sulfate/thiosulfate import. This protein specifically binds thiosulfate and is involved in its transmembrane transport. CysP (also known as thiosulfate binding protein or TSBP) is the periplasmic binding protein of an ATP dependent thiosulfate/sulfate uptake system. cysP is the first gene of a five gene operon (cysPUWAM); cysP is expressed from a PC00040 "CysB" dependent promoter . Assays of sulfate and thiosulfate binding and uptake suggest that CysP is primarily a thiosulfate binding protein . cysP insertional mutants are not cysteine auxotrophs but they do have reduced growth with either sulfate or thiosulfate as the sulfur source . Double cysP sbp mutants (cysP::Cat sbp::Kan) are cysteine auxotrophs; growth on sulfate (and thiosulfate) as sole sulfur source can be restored in the double mutant by multicopy expression of either cysP or sbp however growth is impaired compared to the wild type strain; CysP and Sbp have overlapping specificity and both are required for wild-type levels of sulfate/thiosulfate transport

## Biological Role

Component of thiosulfate/sulfate ABC transporter (complex.ecocyc.ABC-7-CPLX).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex CysAWTP (TC 3.A.1.6.1) involved in sulfate/thiosulfate import. This protein specifically binds thiosulfate and is involved in its transmembrane transport.

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-7-CPLX|complex.ecocyc.ABC-7-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2425|gene.b2425]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16700`
- `KEGG:ecj:JW2418;eco:b2425;ecoc:C3026_13475;`
- `GeneID:946883;`
- `GO:GO:0005615; GO:0006790; GO:0015709; GO:0016020; GO:0030288; GO:0035796; GO:0036173; GO:0043199; GO:0140104; GO:1902358`

## Notes

Thiosulfate-binding protein
