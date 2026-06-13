---
entity_id: "protein.P23538"
entity_type: "protein"
name: "ppsA"
source_database: "UniProt"
source_id: "P23538"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ppsA pps b1702 JW1692"
---

# ppsA

`protein.P23538`

## Static

- Type: `protein`
- Source: `UniProt:P23538`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of pyruvate to phosphoenolpyruvate. {ECO:0000269|PubMed:4319237}.

## Biological Role

Catalyzes ATP:pyruvate,water phosphotransferase (reaction.R00199). Component of phosphoenolpyruvate synthetase (complex.ecocyc.PEPSYNTH-CPLX).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorylation of pyruvate to phosphoenolpyruvate. {ECO:0000269|PubMed:4319237}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00199|reaction.R00199]] `KEGG` `database` - via EC:2.7.9.2
- `is_component_of` --> [[complex.ecocyc.PEPSYNTH-CPLX|complex.ecocyc.PEPSYNTH-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1702|gene.b1702]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23538`
- `KEGG:ecj:JW1692;eco:b1702;ecoc:C3026_09745;`
- `GeneID:75171769;75203549;946209;`
- `GO:GO:0000287; GO:0005524; GO:0006094; GO:0008986; GO:0042803`
- `EC:2.7.9.2`

## Notes

Phosphoenolpyruvate synthase (PEP synthase) (EC 2.7.9.2) (Pyruvate, water dikinase)
