---
entity_id: "protein.P76173"
entity_type: "protein"
name: "ynfH"
source_database: "UniProt"
source_id: "P76173"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250}; Multi-pass membrane protein {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ynfH b1590 JW5261"
---

# ynfH

`protein.P76173`

## Static

- Type: `protein`
- Source: `UniProt:P76173`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250}; Multi-pass membrane protein {ECO:0000250}.

## Enriched Summary

FUNCTION: Terminal reductase during anaerobic growth on various sulfoxide and N-oxide compounds. The C subunit anchors the other two subunits to the membrane and stabilize the catalytic subunits (By similarity). {ECO:0000250}. YnfH contains eight potential transmembrane helices and is similar to DmsC, the membrane anchor subunit of the dimethyl sulfoxide reductase heterotrimer. When expressed together with DmsA and either DmsB or YnfG in a plasmid expression system, YnfH can form a complex with DmsA and DmsB/YnfG and support growth on DMSO . A ynfH mutant reaches slightly higher cell density in stationary phase than wild type when growing in media with sublethal levels of streptomycin, an aminoglycoside antibiotic .

## Biological Role

Component of selenate reductase (complex.ecocyc.CPLX0-1601).

## Annotation

FUNCTION: Terminal reductase during anaerobic growth on various sulfoxide and N-oxide compounds. The C subunit anchors the other two subunits to the membrane and stabilize the catalytic subunits (By similarity). {ECO:0000250}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1601|complex.ecocyc.CPLX0-1601]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1590|gene.b1590]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76173`
- `KEGG:ecj:JW5261;eco:b1590;ecoc:C3026_09160;`
- `GeneID:945822;`
- `GO:GO:0005886; GO:0009061; GO:0009389; GO:0009390; GO:0019645; GO:1990204`

## Notes

Anaerobic dimethyl sulfoxide reductase chain YnfH (DMSO reductase anchor subunit YnfH)
