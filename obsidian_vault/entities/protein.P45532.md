---
entity_id: "protein.P45532"
entity_type: "protein"
name: "tusD"
source_database: "UniProt"
source_id: "P45532"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tusD yheN b3345 JW3307"
---

# tusD

`protein.P45532`

## Static

- Type: `protein`
- Source: `UniProt:P45532`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of a sulfur-relay system required for 2-thiolation of 5-methylaminomethyl-2-thiouridine (mnm(5)s(2)U) at tRNA wobble positions. Accepts sulfur from TusA and transfers it in turn to TusE. {ECO:0000269|PubMed:16387657}. TusD is labeled by 35S sulfur during 2-thiouridine formation in vitro. The cysteine residue C78 appears to be responsible for accepting the activated sulfur . A tusD deletion mutant lacks the 2-thio modification of mnm5s2U in tRNA and has a severe growth defect . TusD: "tRNA 2-thiouridine synthesizing protein"

## Biological Role

Component of sulfurtransferase complex TusBCD (complex.ecocyc.CPLX-3942).

## Enriched Pathways

- `eco04122` Sulfur relay system (KEGG)

## Annotation

FUNCTION: Part of a sulfur-relay system required for 2-thiolation of 5-methylaminomethyl-2-thiouridine (mnm(5)s(2)U) at tRNA wobble positions. Accepts sulfur from TusA and transfers it in turn to TusE. {ECO:0000269|PubMed:16387657}.

## Pathways

- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-3942|complex.ecocyc.CPLX-3942]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3345|gene.b3345]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45532`
- `KEGG:ecj:JW3307;eco:b3345;ecoc:C3026_18165;`
- `GeneID:947852;`
- `GO:GO:0002143; GO:0005829; GO:0016783; GO:0097163; GO:1990228`
- `EC:2.8.1.-`

## Notes

Sulfurtransferase TusD (EC 2.8.1.-) (tRNA 2-thiouridine synthesizing protein D)
