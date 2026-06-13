---
entity_id: "protein.P45531"
entity_type: "protein"
name: "tusC"
source_database: "UniProt"
source_id: "P45531"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tusC yheM b3344 JW3306"
---

# tusC

`protein.P45531`

## Static

- Type: `protein`
- Source: `UniProt:P45531`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of a sulfur-relay system required for 2-thiolation of 5-methylaminomethyl-2-thiouridine (mnm(5)s(2)U) at tRNA wobble positions. {ECO:0000269|PubMed:16387657}. A tusC deletion mutant lacks the 2-thio modification of mnm5s2U in tRNA and has a severe growth defect . TusC: "tRNA 2-thiouridine synthesizing protein"

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

- `encodes` <-- [[gene.b3344|gene.b3344]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45531`
- `KEGG:ecj:JW3306;eco:b3344;ecoc:C3026_18160;`
- `GeneID:93778654;947853;`
- `GO:GO:0002143; GO:1990228`

## Notes

Protein TusC (tRNA 2-thiouridine synthesizing protein C)
