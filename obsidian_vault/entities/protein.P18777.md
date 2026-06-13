---
entity_id: "protein.P18777"
entity_type: "protein"
name: "dmsC"
source_database: "UniProt"
source_id: "P18777"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dmsC b0896 JW0879"
---

# dmsC

`protein.P18777`

## Static

- Type: `protein`
- Source: `UniProt:P18777`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Terminal reductase during anaerobic growth on various sulfoxide and N-oxide compounds. DmsC anchors the DmsAB dimer to the membrane and stabilizes it. DmsC is the integral membrane subunit of the DMSO reductase complex. It is predicted to have 8 transmembrane helices with the N and C termini located in the periplasm . This subunit anchors and stabilizes the catalytic subunits DmsA and DmsB . A glutamate residue, E87, is important for menaquinol binding and oxidation .

## Biological Role

Component of dimethyl sulfoxide reductase (complex.ecocyc.DIMESULFREDUCT-CPLX).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Terminal reductase during anaerobic growth on various sulfoxide and N-oxide compounds. DmsC anchors the DmsAB dimer to the membrane and stabilizes it.

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.DIMESULFREDUCT-CPLX|complex.ecocyc.DIMESULFREDUCT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0896|gene.b0896]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P18777`
- `KEGG:ecj:JW0879;eco:b0896;ecoc:C3026_05540;`
- `GeneID:945502;`
- `GO:GO:0005886; GO:0009061; GO:0009389; GO:0009390; GO:0018907; GO:0019645`

## Notes

Anaerobic dimethyl sulfoxide reductase chain C (DMSO reductase anchor subunit)
