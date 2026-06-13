---
entity_id: "protein.P62620"
entity_type: "protein"
name: "ispG"
source_database: "UniProt"
source_id: "P62620"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ispG gcpE b2515 JW2499"
---

# ispG

`protein.P62620`

## Static

- Type: `protein`
- Source: `UniProt:P62620`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Converts 2C-methyl-D-erythritol 2,4-cyclodiphosphate (ME-2,4cPP) into 1-hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate, using flavodoxin as the reducing agent. {ECO:0000255|HAMAP-Rule:MF_00159, ECO:0000269|PubMed:15978585, ECO:0000269|PubMed:16268586}. 1-hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate synthase (IspG) catalyzes the sixth step of the mevalonate-independent NONMEVIPP-PWY methylerythritol phosphate (MEP) pathway, the conversion of 2C-methyl-D-erythritol 2,4-cyclodiphosphate into 1-hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate . IspG activity depends on additional proteins, most likely involved in the oxidation portion of the reaction . IspG contains a [4Fe-4S] cluster that is required for its activity . Mutations in cysteine residues responsible for Fe-S cluster coordination abolish IspG's enzymatic activity . In vitro, CPLX0-7617 ErpA can transfer a [4Fe-4S] cluster to apo-IspG . Increased IspG activity was observed under new assay conditions . Flux through the entire MEP pathway was shown to depend on the presence of FLAVODOXIN1-MONOMER, which may supply reducing equivalents necessary to reduce the Fe-S cluster and yield an active enzyme . A new reaction mechanism was proposed . Further studies on the reaction mechanism and reaction intermediate have been published , and potential reaction mechanisms are reviewed in...

## Biological Role

Catalyzes (E)-4-hydroxy-3-methylbut-2-en-1-yl-diphosphate:oxidized flavodoxin oxidoreductase (reaction.R10859), RXN-15878 (reaction.ecocyc.RXN-15878). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7), Mn2+ (molecule.ecocyc.MN_2).

## Enriched Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Converts 2C-methyl-D-erythritol 2,4-cyclodiphosphate (ME-2,4cPP) into 1-hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate, using flavodoxin as the reducing agent. {ECO:0000255|HAMAP-Rule:MF_00159, ECO:0000269|PubMed:15978585, ECO:0000269|PubMed:16268586}.

## Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R10859|reaction.R10859]] `KEGG` `database` - via EC:1.17.7.3
- `catalyzes` --> [[reaction.ecocyc.RXN-15878|reaction.ecocyc.RXN-15878]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2515|gene.b2515]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P62620`
- `KEGG:ecj:JW2499;eco:b2515;ecoc:C3026_13945;`
- `GeneID:86860640;86947404;946991;`
- `GO:GO:0005506; GO:0005829; GO:0016114; GO:0019288; GO:0046429; GO:0046872; GO:0051539; GO:0141197`
- `EC:1.17.7.3`

## Notes

4-hydroxy-3-methylbut-2-en-1-yl diphosphate synthase (flavodoxin) (EC 1.17.7.3) (1-hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate synthase) (Protein GcpE) (Protein E)
