---
entity_id: "protein.P0A7A2"
entity_type: "protein"
name: "gpmB"
source_database: "UniProt"
source_id: "P0A7A2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gpmB ytjC b4395 JW4358"
---

# gpmB

`protein.P0A7A2`

## Static

- Type: `protein`
- Source: `UniProt:P0A7A2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Probable phosphoglycerate mutase GpmB (EC 5.4.2.-) (PGAM) (Phosphoglyceromutase) YtjC was identified as a member of the phosphoglycerate mutase B subfamily; however, no members of that family have been functionally characterized , and were unable to detect phosphoglycerate mutase activity in vitro. Members of this family may in fact be acid phosphatases . Unpurified YtjC has phosphatase activity against 6-phosphobenzisoxazole and p-nitrophenyl phosphate . YtjC is a multicopy suppressor of the conditional ΔEG10945 serB phenotype . The intrinsic phosphoserine phosphatase activity of YtjC is extremely low; mutants with increased activity have been selected . The 14 enzymes involved in glycolysis have hundreds of unique protein-protein interactions (PPIs) with at least 237 other protein interactors, most of which are not essential and about half of the interactors are other enzymes. Six of the glycolytic enzymes (Pgk, GpmA, GpmI, PykA, GapA and Eno) have at least 1 uncharacterized interactor, while Eno has 5 interactors. There were no uncharacterized interactors identified for GpmB .

## Biological Role

Catalyzes D-phosphoglycerate 2,3-phosphomutase (reaction.R01518).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

Probable phosphoglycerate mutase GpmB (EC 5.4.2.-) (PGAM) (Phosphoglyceromutase)

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.R01518|reaction.R01518]] `KEGG` `database` - via EC:5.4.2.11

## Incoming Edges (1)

- `encodes` <-- [[gene.b4395|gene.b4395]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7A2`
- `KEGG:ecj:JW4358;eco:b4395;ecoc:C3026_23750;`
- `GeneID:93777450;948918;`
- `GO:GO:0004619; GO:0005737; GO:0006096; GO:0016791`
- `EC:5.4.2.-`

## Notes

Probable phosphoglycerate mutase GpmB (EC 5.4.2.-) (PGAM) (Phosphoglyceromutase)
