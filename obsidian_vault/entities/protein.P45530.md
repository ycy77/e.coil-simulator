---
entity_id: "protein.P45530"
entity_type: "protein"
name: "tusB"
source_database: "UniProt"
source_id: "P45530"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tusB yheL b3343 JW3305"
---

# tusB

`protein.P45530`

## Static

- Type: `protein`
- Source: `UniProt:P45530`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of a sulfur-relay system required for 2-thiolation of 5-methylaminomethyl-2-thiouridine (mnm(5)s(2)U) at tRNA wobble positions. {ECO:0000269|PubMed:16387657}. A tusB deletion mutant lacks the 2-thio modification of mnm5s2U in tRNA and has a severe growth defect . TusB: "tRNA 2-thiouridine synthesizing protein"

## Biological Role

Component of sulfurtransferase complex TusBCD (complex.ecocyc.CPLX-3942).

## Enriched Pathways

- `eco04122` Sulfur relay system (KEGG)

## Annotation

FUNCTION: Part of a sulfur-relay system required for 2-thiolation of 5-methylaminomethyl-2-thiouridine (mnm(5)s(2)U) at tRNA wobble positions. {ECO:0000269|PubMed:16387657}.

## Pathways

- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-3942|complex.ecocyc.CPLX-3942]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3343|gene.b3343]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45530`
- `KEGG:ecj:JW3305;eco:b3343;ecoc:C3026_18155;`
- `GeneID:947844;`
- `GO:GO:0002143; GO:1990228`

## Notes

Protein TusB (tRNA 2-thiouridine synthesizing protein B)
