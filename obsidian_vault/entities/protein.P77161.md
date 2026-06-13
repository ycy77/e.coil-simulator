---
entity_id: "protein.P77161"
entity_type: "protein"
name: "glxR"
source_database: "UniProt"
source_id: "P77161"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glxR glxB1 ybbQ b0509 JW0497"
---

# glxR

`protein.P77161`

## Static

- Type: `protein`
- Source: `UniProt:P77161`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

2-hydroxy-3-oxopropionate reductase (EC 1.1.1.60) (Tartronate semialdehyde reductase) (TSAR) Tartronate semialdehyde reductase 2 (GlxR) catalyzes the reversible reactions of NAD+-dependent oxidation of D-glycerate and the NADH-dependent reduction of tartronate semialdehyde . Expression of tartronate semialdehyde reductase is induced by anaerobic growth with allantoin as the sole source of nitrogen and is induced more than 100-fold by growth on glyoxylate as the sole source of carbon . A glxR mutant lacks the ability to utilize glyoxylate . Review:

## Biological Role

Catalyzes (R)-glycerate:NAD+ oxidoreductase (reaction.R01745), (R)-glycerate:NADP+ oxidoreductase (reaction.R01747). Component of tartronate semialdehyde reductase 2 (complex.ecocyc.CPLX0-7616).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

2-hydroxy-3-oxopropionate reductase (EC 1.1.1.60) (Tartronate semialdehyde reductase) (TSAR)

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R01745|reaction.R01745]] `KEGG` `database` - via EC:1.1.1.60
- `catalyzes` --> [[reaction.R01747|reaction.R01747]] `KEGG` `database` - via EC:1.1.1.60
- `is_component_of` --> [[complex.ecocyc.CPLX0-7616|complex.ecocyc.CPLX0-7616]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0509|gene.b0509]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77161`
- `KEGG:ecj:JW0497;eco:b0509;ecoc:C3026_02500;`
- `GeneID:945146;`
- `GO:GO:0006974; GO:0008679; GO:0009436; GO:0009442; GO:0046296; GO:0050661; GO:0051287`
- `EC:1.1.1.60`

## Notes

2-hydroxy-3-oxopropionate reductase (EC 1.1.1.60) (Tartronate semialdehyde reductase) (TSAR)
