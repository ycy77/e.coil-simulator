---
entity_id: "protein.P52599"
entity_type: "protein"
name: "emrK"
source_database: "UniProt"
source_id: "P52599"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}; Periplasmic side {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "emrK b2368 JW2365"
---

# emrK

`protein.P52599`

## Static

- Type: `protein`
- Source: `UniProt:P52599`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}; Periplasmic side {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of the tripartite efflux system EmrYK-TolC, which confers resistance to various drugs. {ECO:0000250}. EmrK is the membrane fusion protein of a putative tripartite efflux pump complex EmrK has 50.45% sequence identity with the EG11354-MONOMER "EmrA" membrane fusion protein . An emrK-lacZ' protein fusion shows increased expression upon prolonged (24hr) incubation with sub-inhibitory concentrations of tetracycline, chloramphenicol or salicylate; EmrAB is implicated in tetracycline efflux . Expression of emrK increases when cells are exposed to 2mM indole emrK was identified in a screen for genes that reduce the lethal effects of stress. An emrK insertion mutant is more sensitive than wild type to mitomycin C and other stresses such as UV irradiation .

## Biological Role

Component of tripartite efflux pump EmrKY-TolC (complex.ecocyc.CPLX0-2161).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of the tripartite efflux system EmrYK-TolC, which confers resistance to various drugs. {ECO:0000250}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2161|complex.ecocyc.CPLX0-2161]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2368|gene.b2368]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52599`
- `KEGG:ecj:JW2365;eco:b2368;ecoc:C3026_13170;`
- `GeneID:946840;`
- `GO:GO:0005886; GO:0006974; GO:0015125; GO:0015721; GO:0042910; GO:0046677; GO:0098567; GO:0140330; GO:1990281; GO:1990961`

## Notes

Probable multidrug resistance protein EmrK
