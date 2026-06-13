---
entity_id: "protein.P29745"
entity_type: "protein"
name: "pepT"
source_database: "UniProt"
source_id: "P29745"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pepT b1127 JW1113"
---

# pepT

`protein.P29745`

## Static

- Type: `protein`
- Source: `UniProt:P29745`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Cleaves the N-terminal amino acid of tripeptides. {ECO:0000250}.

## Biological Role

Component of peptidase T (complex.ecocyc.CPLX0-3041).

## Annotation

FUNCTION: Cleaves the N-terminal amino acid of tripeptides. {ECO:0000250}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3041|complex.ecocyc.CPLX0-3041]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1127|gene.b1127]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P29745`
- `KEGG:ecj:JW1113;eco:b1127;ecoc:C3026_06785;`
- `GeneID:946333;`
- `GO:GO:0005829; GO:0006508; GO:0006518; GO:0008237; GO:0008270; GO:0042803; GO:0043171; GO:0045148`
- `EC:3.4.11.4`

## Notes

Peptidase T (EC 3.4.11.4) (Aminotripeptidase) (Tripeptidase) (Tripeptide aminopeptidase)
