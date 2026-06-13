---
entity_id: "protein.P52613"
entity_type: "protein"
name: "fliJ"
source_database: "UniProt"
source_id: "P52613"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein; Cytoplasmic side."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fliJ flaO flaS b1942 JW1926"
---

# fliJ

`protein.P52613`

## Static

- Type: `protein`
- Source: `UniProt:P52613`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein; Cytoplasmic side.

## Enriched Summary

FUNCTION: The FliJ protein is a flagellar protein that affects chemotactic events. Mutations in FliJ results in failure to respond to chemotactic stimuli. FliJ is one of three soluble components of the flagellar export system, along with FliH and FliI . FliJ has several feature similarities with the type III cytoplasmic chaperone family .

## Biological Role

Component of flagellar export assembly apparatus (complex.ecocyc.CPLX0-7451).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: The FliJ protein is a flagellar protein that affects chemotactic events. Mutations in FliJ results in failure to respond to chemotactic stimuli.

## Pathways

- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7451|complex.ecocyc.CPLX0-7451]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1942|gene.b1942]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52613`
- `KEGG:ecj:JW1926;eco:b1942;ecoc:C3026_11000;`
- `GeneID:946454;`
- `GO:GO:0003774; GO:0005886; GO:0006935; GO:0009288; GO:0030254; GO:0030257; GO:0044781; GO:0071973; GO:0120102`

## Notes

Flagellar FliJ protein
