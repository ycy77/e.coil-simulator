---
entity_id: "protein.P0AGL2"
entity_type: "protein"
name: "tdcF"
source_database: "UniProt"
source_id: "P0AGL2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tdcF yhaR b3113 JW5521"
---

# tdcF

`protein.P0AGL2`

## Static

- Type: `protein`
- Source: `UniProt:P0AGL2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: May be a post-translational regulator that controls the metabolic fate of L-threonine or the potentially toxic intermediate 2-ketobutyrate.

## Biological Role

Component of predicted enamine/imine deaminase (complex.ecocyc.CPLX0-7987).

## Annotation

FUNCTION: May be a post-translational regulator that controls the metabolic fate of L-threonine or the potentially toxic intermediate 2-ketobutyrate.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7987|complex.ecocyc.CPLX0-7987]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b3113|gene.b3113]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGL2`
- `KEGG:ecj:JW5521;eco:b3113;ecoc:C3026_16980;`
- `GeneID:93778872;947624;`
- `GO:GO:0005829; GO:0006566; GO:0019239; GO:0042802; GO:0070689`
- `EC:3.5.4.-`

## Notes

Putative reactive intermediate deaminase TdcF (EC 3.5.4.-)
