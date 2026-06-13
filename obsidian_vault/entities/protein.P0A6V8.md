---
entity_id: "protein.P0A6V8"
entity_type: "protein"
name: "glk"
source_database: "UniProt"
source_id: "P0A6V8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:9023215}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glk b2388 JW2385"
---

# glk

`protein.P0A6V8`

## Static

- Type: `protein`
- Source: `UniProt:P0A6V8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:9023215}.

## Enriched Summary

FUNCTION: An ATP-dependent kinase that phosphorylates glucose to make glucose-6-phosphate, not active on fructose, galactose or mannose. Not highly important in wild-type E.coli as glucose is transported into the cell by the PTS system as glucose 6-phosphate. {ECO:0000269|PubMed:9023215}. The cytoplasmic glucokinase is not required for growth on glucose as the carbon source, because glucose is phosphorylated during transport by the PTS system. Glucokinase phosphorylates glucose which is produced by amylomaltase. Growth on glucose reduces the expression of glk by 50%. Growth on other carbon sources does not appear to affect glk expression . Overexpression of foreign proteins appears to induce expression of glk as well . A crystal structure of the enzyme from E. coli O157:H7 has been reported . Evolutionary relationships between glucose kinases based on their tertiary structures have been discussed . A periplasmic glucokinase whose expression is induced during overexpression of foreign proteins has been reported, but it does not appear to be the product of the glk gene . A role for cytoplasmic glucose and Glk in the complex regulation of maltose and maltodextrin utilization by E. coli has been proposed. The maltose utilization system is controlled by MalT, the central transcriptional activator of mal genes. Glk was suggested to exert regulatory effects on MalT...

## Biological Role

Catalyzes ATP:D-glucose 6-phosphotransferase (reaction.R00299), GLUCOKIN-RXN (reaction.ecocyc.GLUCOKIN-RXN), GLUCOSAMINE-KINASE-RXN (reaction.ecocyc.GLUCOSAMINE-KINASE-RXN).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: An ATP-dependent kinase that phosphorylates glucose to make glucose-6-phosphate, not active on fructose, galactose or mannose. Not highly important in wild-type E.coli as glucose is transported into the cell by the PTS system as glucose 6-phosphate. {ECO:0000269|PubMed:9023215}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00299|reaction.R00299]] `KEGG` `database` - via EC:2.7.1.2
- `catalyzes` --> [[reaction.ecocyc.GLUCOKIN-RXN|reaction.ecocyc.GLUCOKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.GLUCOSAMINE-KINASE-RXN|reaction.ecocyc.GLUCOSAMINE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2388|gene.b2388]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6V8`
- `KEGG:ecj:JW2385;eco:b2388;ecoc:C3026_13275;`
- `GeneID:75172507;75202543;946858;`
- `GO:GO:0004340; GO:0005524; GO:0005536; GO:0005829; GO:0006096`
- `EC:2.7.1.2`

## Notes

Glucokinase (EC 2.7.1.2) (Glucose kinase)
