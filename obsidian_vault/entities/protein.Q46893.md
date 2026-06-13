---
entity_id: "protein.Q46893"
entity_type: "protein"
name: "ispD"
source_database: "UniProt"
source_id: "Q46893"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ispD ygbP b2747 JW2717"
---

# ispD

`protein.Q46893`

## Static

- Type: `protein`
- Source: `UniProt:Q46893`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the formation of 4-diphosphocytidyl-2-C-methyl-D-erythritol from CTP and 2-C-methyl-D-erythritol 4-phosphate (MEP).

## Biological Role

Component of 2-C-methyl-D-erythritol 4-phosphate cytidylyltransferase (complex.ecocyc.CPLX0-234).

## Enriched Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of 4-diphosphocytidyl-2-C-methyl-D-erythritol from CTP and 2-C-methyl-D-erythritol 4-phosphate (MEP).

## Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-234|complex.ecocyc.CPLX0-234]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2747|gene.b2747]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46893`
- `KEGG:ecj:JW2717;eco:b2747;ecoc:C3026_15105;`
- `GeneID:93779259;948269;`
- `GO:GO:0000287; GO:0005829; GO:0019288; GO:0042802; GO:0050518`
- `EC:2.7.7.60`

## Notes

2-C-methyl-D-erythritol 4-phosphate cytidylyltransferase (EC 2.7.7.60) (4-diphosphocytidyl-2C-methyl-D-erythritol synthase) (CDP-ME synthase) (MEP cytidylyltransferase) (MCT)
