---
entity_id: "protein.P0ABD5"
entity_type: "protein"
name: "accA"
source_database: "UniProt"
source_id: "P0ABD5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "accA b0185 JW0180"
---

# accA

`protein.P0ABD5`

## Static

- Type: `protein`
- Source: `UniProt:P0ABD5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Component of the acetyl coenzyme A carboxylase (ACC) complex. First, biotin carboxylase catalyzes the carboxylation of biotin on its carrier protein (BCCP) and then the CO(2) group is transferred by the carboxyltransferase to acetyl-CoA to form malonyl-CoA. {ECO:0000255|HAMAP-Rule:MF_00823, ECO:0000269|PubMed:15066985}. accA is an essential gene . Transcription of accA is growth rate-regulated . AccA: "acetyl-CoA carboxylase A"

## Biological Role

Catalyzes acetyl-CoA:carbon-dioxide ligase (ADP-forming) (reaction.R00742). Component of acetyl-CoA carboxylase complex (complex.ecocyc.ACETYL-COA-CARBOXYLMULTI-CPLX), acetyl-CoA carboxyltransferase (complex.ecocyc.ACETYL-COA-CARBOXYLTRANSFER-CPLX).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

FUNCTION: Component of the acetyl coenzyme A carboxylase (ACC) complex. First, biotin carboxylase catalyzes the carboxylation of biotin on its carrier protein (BCCP) and then the CO(2) group is transferred by the carboxyltransferase to acetyl-CoA to form malonyl-CoA. {ECO:0000255|HAMAP-Rule:MF_00823, ECO:0000269|PubMed:15066985}.

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00742|reaction.R00742]] `KEGG` `database` - via EC:6.4.1.2
- `is_component_of` --> [[complex.ecocyc.ACETYL-COA-CARBOXYLMULTI-CPLX|complex.ecocyc.ACETYL-COA-CARBOXYLMULTI-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.ACETYL-COA-CARBOXYLTRANSFER-CPLX|complex.ecocyc.ACETYL-COA-CARBOXYLTRANSFER-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0185|gene.b0185]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABD5`
- `KEGG:ecj:JW0180;eco:b0185;ecoc:C3026_00850;`
- `GeneID:86945115;944895;`
- `GO:GO:0003989; GO:0005524; GO:0005737; GO:0005829; GO:0006633; GO:0009317; GO:0009329; GO:0016743; GO:0042759; GO:0042802; GO:2001295`
- `EC:2.1.3.15`

## Notes

Acetyl-coenzyme A carboxylase carboxyl transferase subunit alpha (ACCase subunit alpha) (Acetyl-CoA carboxylase carboxyltransferase subunit alpha) (EC 2.1.3.15)
