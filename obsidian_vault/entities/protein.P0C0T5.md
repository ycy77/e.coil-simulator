---
entity_id: "protein.P0C0T5"
entity_type: "protein"
name: "mepA"
source_database: "UniProt"
source_id: "P0C0T5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305|PubMed:15292190}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mepA b2328 JW2325"
---

# mepA

`protein.P0C0T5`

## Static

- Type: `protein`
- Source: `UniProt:P0C0T5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305|PubMed:15292190}.

## Enriched Summary

FUNCTION: Murein endopeptidase that cleaves the D-alanyl-meso-2,6-diamino-pimelyl amide bond that connects peptidoglycan strands. Likely plays a role in the removal of murein from the sacculus and could also play a role in the integration of nascent murein strands into the sacculus. {ECO:0000269|PubMed:15292190}.

## Biological Role

Component of peptidoglycan DD-endopeptidase/peptidoglycan LD-endopeptidase (complex.ecocyc.CPLX0-3201).

## Annotation

FUNCTION: Murein endopeptidase that cleaves the D-alanyl-meso-2,6-diamino-pimelyl amide bond that connects peptidoglycan strands. Likely plays a role in the removal of murein from the sacculus and could also play a role in the integration of nascent murein strands into the sacculus. {ECO:0000269|PubMed:15292190}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3201|complex.ecocyc.CPLX0-3201]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2328|gene.b2328]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0C0T5`
- `KEGG:ecj:JW2325;eco:b2328;ecoc:C3026_12970;`
- `GeneID:946812;`
- `GO:GO:0000270; GO:0004175; GO:0004222; GO:0004252; GO:0006508; GO:0008233; GO:0009252; GO:0009410; GO:0030288; GO:0046872`
- `EC:3.4.24.-`

## Notes

Penicillin-insensitive murein endopeptidase (EC 3.4.24.-) (D-alanyl-D-alanine-endopeptidase) (DD-endopeptidase)
