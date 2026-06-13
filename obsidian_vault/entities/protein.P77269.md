---
entity_id: "protein.P77269"
entity_type: "protein"
name: "yphF"
source_database: "UniProt"
source_id: "P77269"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yphF b2548 JW2532"
---

# yphF

`protein.P77269`

## Static

- Type: `protein`
- Source: `UniProt:P77269`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Probably part of the binding-protein-dependent transport system YphDEF. YphF is predicted to be the substrate binding protein of a putative ATP-dependent transport system .

## Biological Role

Component of putative transport complex, ABC superfamily (complex.ecocyc.ABC-60-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Probably part of the binding-protein-dependent transport system YphDEF.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-60-CPLX|complex.ecocyc.ABC-60-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2548|gene.b2548]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77269`
- `KEGG:ecj:JW2532;eco:b2548;ecoc:C3026_14110;`
- `GeneID:947020;`
- `GO:GO:0016020; GO:0030246; GO:0030288; GO:0055052; GO:0055085`

## Notes

ABC transporter periplasmic-binding protein YphF
