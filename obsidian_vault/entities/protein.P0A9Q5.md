---
entity_id: "protein.P0A9Q5"
entity_type: "protein"
name: "accD"
source_database: "UniProt"
source_id: "P0A9Q5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "accD dedB usg b2316 JW2313"
---

# accD

`protein.P0A9Q5`

## Static

- Type: `protein`
- Source: `UniProt:P0A9Q5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Component of the acetyl coenzyme A carboxylase (ACC) complex. Biotin carboxylase (BC) catalyzes the carboxylation of biotin on its carrier protein (BCCP) and then the CO(2) group is transferred by the transcarboxylase to acetyl-CoA to form malonyl-CoA.; FUNCTION: Controls translation of mRNA for both itself and the alpha-subunit (accA) by binding to a probable hairpin in the 5' of the mRNA. Binding to mRNA inhibits translation; this is partially relieved by acetyl-CoA. Increasing amounts of mRNA also inhibit enzyme activity. The Zn2+-binding domain of AccD is required both for catalytic activity and for binding to mRNA . Transcription of accD is growth rate-regulated . A temperature-sensitive mutation in this gene was identified that showed potential as a growth-switch for genetic engineering . A lesson in gene naming:DedB: "downstream E. coli DNA (from hisT)" Usg: "upstream gene" AccD: "acetyl-CoA carboxylase D"

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

FUNCTION: Component of the acetyl coenzyme A carboxylase (ACC) complex. Biotin carboxylase (BC) catalyzes the carboxylation of biotin on its carrier protein (BCCP) and then the CO(2) group is transferred by the transcarboxylase to acetyl-CoA to form malonyl-CoA.; FUNCTION: Controls translation of mRNA for both itself and the alpha-subunit (accA) by binding to a probable hairpin in the 5' of the mRNA. Binding to mRNA inhibits translation; this is partially relieved by acetyl-CoA. Increasing amounts of mRNA also inhibit enzyme activity.

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

- `encodes` <-- [[gene.b2316|gene.b2316]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9Q5`
- `KEGG:ecj:JW2313;eco:b2316;ecoc:C3026_12910;`
- `GeneID:75172444;75202601;946796;`
- `GO:GO:0003677; GO:0003729; GO:0003989; GO:0005524; GO:0005829; GO:0006633; GO:0008270; GO:0009317; GO:0009329; GO:0016743; GO:0017148; GO:0042759; GO:2001295`
- `EC:2.1.3.15`

## Notes

Acetyl-coenzyme A carboxylase carboxyl transferase subunit beta (ACCase subunit beta) (Acetyl-CoA carboxylase carboxyltransferase subunit beta) (EC 2.1.3.15)
