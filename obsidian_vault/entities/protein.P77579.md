---
entity_id: "protein.P77579"
entity_type: "protein"
name: "fryC"
source_database: "UniProt"
source_id: "P77579"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fryC ypdG b2386 JW2383"
---

# fryC

`protein.P77579`

## Static

- Type: `protein`
- Source: `UniProt:P77579`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitant with their translocation across the cell membrane. {ECO:0000250}. fryC encodes a predicted Enzyme IIC component of a PTS permease of unknown specificity. FryC shows similarity to the IIC domain of the PTS Enzyme II specific for fructose

## Biological Role

Component of putative PTS enzyme II FryBCA (complex.ecocyc.CPLX0-8119).

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitant with their translocation across the cell membrane. {ECO:0000250}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8119|complex.ecocyc.CPLX0-8119]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2386|gene.b2386]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77579`
- `KEGG:ecj:JW2383;eco:b2386;ecoc:C3026_13265;`
- `GeneID:949111;`
- `GO:GO:0005886; GO:0008982; GO:0009401; GO:0090563`

## Notes

Fructose-like permease IIC component 1 (PTS system fructose-like EIIC component 1)
