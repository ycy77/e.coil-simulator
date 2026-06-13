---
entity_id: "protein.P0AAB8"
entity_type: "protein"
name: "uspD"
source_database: "UniProt"
source_id: "P0AAB8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uspD yiiT b3923 JW3894"
---

# uspD

`protein.P0AAB8`

## Static

- Type: `protein`
- Source: `UniProt:P0AAB8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Required for resistance to DNA-damaging agents. {ECO:0000269|PubMed:11849540}.

## Biological Role

Component of universal stress protein D (complex.ecocyc.CPLX0-8587).

## Annotation

FUNCTION: Required for resistance to DNA-damaging agents. {ECO:0000269|PubMed:11849540}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8587|complex.ecocyc.CPLX0-8587]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3923|gene.b3923]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAB8`
- `KEGG:ecj:JW3894;eco:b3923;ecoc:C3026_21205;`
- `GeneID:93777975;948415;`
- `GO:GO:0000303; GO:0005829; GO:0006950; GO:0009411; GO:0042594; GO:0042803`

## Notes

Universal stress protein D
