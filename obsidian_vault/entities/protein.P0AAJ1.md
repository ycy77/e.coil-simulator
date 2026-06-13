---
entity_id: "protein.P0AAJ1"
entity_type: "protein"
name: "ynfG"
source_database: "UniProt"
source_id: "P0AAJ1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ynfG b1589 JW1581"
---

# ynfG

`protein.P0AAJ1`

## Static

- Type: `protein`
- Source: `UniProt:P0AAJ1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Electron transfer subunit of the terminal reductase during anaerobic growth on various sulfoxide and N-oxide compounds. YnfG is highly similar to DmsB, the iron-sulfur cluster-containing subunit of the dimethyl sulfoxide reductase heterotrimer, and cross-reacts with an anti-DmsB antibody. It contains iron-sulfur clusters which are indistinguishable from DmsB by EPR spectroscopy. When expressed together with DmsA and YnfH in a plasmid expression system, YnfG can form a complex with DmsA and YnfH and support growth on DMSO .

## Biological Role

Component of selenate reductase (complex.ecocyc.CPLX0-1601).

## Annotation

FUNCTION: Electron transfer subunit of the terminal reductase during anaerobic growth on various sulfoxide and N-oxide compounds.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1601|complex.ecocyc.CPLX0-1601]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1589|gene.b1589]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAJ1`
- `KEGG:ecj:JW1581;eco:b1589;ecoc:C3026_09155;`
- `GeneID:75171647;75204432;945638;`
- `GO:GO:0009061; GO:0009389; GO:0018907; GO:0019645; GO:0046872; GO:0051539; GO:1990204`

## Notes

Probable anaerobic dimethyl sulfoxide reductase chain YnfG (DMSO reductase iron-sulfur subunit YnfG)
