---
entity_id: "protein.P63228"
entity_type: "protein"
name: "gmhB"
source_database: "UniProt"
source_id: "P63228"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gmhB yaeD b0200 JW0196"
---

# gmhB

`protein.P63228`

## Static

- Type: `protein`
- Source: `UniProt:P63228`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Converts the D-glycero-beta-D-manno-heptose 1,7-bisphosphate (beta-HBP) intermediate into D-glycero-beta-D-manno-heptose 1-phosphate by removing the phosphate group at the C-7 position. {ECO:0000269|PubMed:11751812, ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:20050615, ECO:0000269|PubMed:31449400}. gmhB encodes the D,D-heptose 1,7-bisphosphate phosphatase of the ADP-heptose biosynthesis pathway. GmhB belongs to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. A gmhB deletion strain has a partial defect in LPS core synthesis, but is not completely heptoseless . GmhB has a narrow substrate range, with activity that is specific for ketohexose and ketoheptose bisphosphates, and shows high catalytic efficiency towards its physiological substrate . Crystal structures of apo-GmhB and several liganded forms have been solved, guiding construction of site-directed mutants that provide insight into substrate recognition elements in the catalytic site and suggest a reaction intermediate . Protein-Protein Interaction (PPI) networks have been examined with algebraic topology analysis showing that most interacting proteins with GmhB are related to the critical cellular processes such as protein translation...

## Biological Role

Catalyzes D-glycero-alpha-D-manno-heptose 1,7-bisphosphate 7-phosphohydrolase (reaction.R09771), RXN0-4361 (reaction.ecocyc.RXN0-4361). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Converts the D-glycero-beta-D-manno-heptose 1,7-bisphosphate (beta-HBP) intermediate into D-glycero-beta-D-manno-heptose 1-phosphate by removing the phosphate group at the C-7 position. {ECO:0000269|PubMed:11751812, ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:20050615, ECO:0000269|PubMed:31449400}.

## Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R09771|reaction.R09771]] `KEGG` `database` - via EC:3.1.3.83
- `catalyzes` --> [[reaction.ecocyc.RXN0-4361|reaction.ecocyc.RXN0-4361]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0200|gene.b0200]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P63228`
- `KEGG:ecj:JW0196;eco:b0200;ecoc:C3026_00930;`
- `GeneID:93777223;944879;`
- `GO:GO:0000287; GO:0005829; GO:0008270; GO:0009103; GO:0009244; GO:0034200; GO:0097171`
- `EC:3.1.3.82`

## Notes

D-glycero-beta-D-manno-heptose-1,7-bisphosphate 7-phosphatase (EC 3.1.3.82) (D,D-heptose 1,7-bisphosphate phosphatase) (HBP phosphatase)
