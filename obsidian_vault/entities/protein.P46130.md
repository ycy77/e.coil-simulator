---
entity_id: "protein.P46130"
entity_type: "protein"
name: "ybhC"
source_database: "UniProt"
source_id: "P46130"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000305}; Lipid-anchor {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybhC b0772 JW0755"
---

# ybhC

`protein.P46130`

## Static

- Type: `protein`
- Source: `UniProt:P46130`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000305}; Lipid-anchor {ECO:0000305}.

## Enriched Summary

FUNCTION: Putative thioesterase. Does not bind pectin, and has no pectinesterase activity. {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:19452549}. YbhC is an outer membrane lipoprotein . Sequence similarity suggests that it is a member of the Outer Membrane Porin (OPR) Family . Phylogenetic analysis places YbhC into a distinct subclade of the carbohydrate esterase 8 (CE8) family . Esterase/thioesterase activity of YbhC was discovered in a high-throughput screen of purified proteins . This activity could not be reproduced by . YbhC is enriched in the membrane fraction of minicells (versus rod cells) purifed from an E. coli minicell mutant and is a polar protein candidate . A crystal structure of a truncated form of YbhC lacking the membrane anchor has been solved at 1.7 Å resolution . Overexpression of yhbC from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hydrogen peroxide .

## Biological Role

Catalyzes pectin pectylhydrolase (reaction.R02362).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Putative thioesterase. Does not bind pectin, and has no pectinesterase activity. {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:19452549}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.R02362|reaction.R02362]] `KEGG` `database` - via EC:3.1.1.11

## Incoming Edges (1)

- `encodes` <-- [[gene.b0772|gene.b0772]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P46130`
- `KEGG:ecj:JW0755;eco:b0772;ecoc:C3026_03915;`
- `GeneID:75204887;945381;`
- `GO:GO:0009279; GO:0030599; GO:0042545; GO:0052689`
- `EC:3.1.2.-`

## Notes

Putative acyl-CoA thioester hydrolase YbhC (EC 3.1.2.-)
