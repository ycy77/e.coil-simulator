---
entity_id: "protein.P0A7H0"
entity_type: "protein"
name: "recF"
source_database: "UniProt"
source_id: "P0A7H0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "recF uvrF b3700 JW3677"
---

# recF

`protein.P0A7H0`

## Static

- Type: `protein`
- Source: `UniProt:P0A7H0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: The RecF protein is involved in DNA metabolism; it is required for DNA replication and normal SOS inducibility. RecF binds preferentially to single-stranded, linear DNA. It also seems to bind ATP.

## Biological Role

Component of recombination mediator protein RecF (complex.ecocyc.CPLX0-8596).

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

FUNCTION: The RecF protein is involved in DNA metabolism; it is required for DNA replication and normal SOS inducibility. RecF binds preferentially to single-stranded, linear DNA. It also seems to bind ATP.

## Pathways

- `eco03440` Homologous recombination (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8596|complex.ecocyc.CPLX0-8596]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3700|gene.b3700]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7H0`
- `KEGG:ecj:JW3677;eco:b3700;ecoc:C3026_20060;`
- `GeneID:93778441;948209;`
- `GO:GO:0000725; GO:0000731; GO:0003697; GO:0005524; GO:0005737; GO:0006260; GO:0006302; GO:0009411; GO:0009432`

## Notes

DNA replication and repair protein RecF
