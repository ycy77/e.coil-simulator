---
entity_id: "protein.P18776"
entity_type: "protein"
name: "dmsB"
source_database: "UniProt"
source_id: "P18776"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dmsB b0895 JW0878"
---

# dmsB

`protein.P18776`

## Static

- Type: `protein`
- Source: `UniProt:P18776`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Electron transfer subunit of the terminal reductase during anaerobic growth on various sulfoxide and N-oxide compounds. The DmsB subunit of DMSO reductase subunit contains four 4 (4Fe-4S) clusters - FS1, FS2, FS3 and FS4 .

## Biological Role

Component of dimethyl sulfoxide reductase (complex.ecocyc.DIMESULFREDUCT-CPLX).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Electron transfer subunit of the terminal reductase during anaerobic growth on various sulfoxide and N-oxide compounds.

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.DIMESULFREDUCT-CPLX|complex.ecocyc.DIMESULFREDUCT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0895|gene.b0895]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P18776`
- `KEGG:ecj:JW0878;eco:b0895;ecoc:C3026_05535;`
- `GeneID:86863417;93776525;945507;`
- `GO:GO:0005886; GO:0009061; GO:0009389; GO:0009390; GO:0018907; GO:0019645; GO:0046872; GO:0051539`

## Notes

Anaerobic dimethyl sulfoxide reductase chain B (DMSO reductase iron-sulfur subunit)
