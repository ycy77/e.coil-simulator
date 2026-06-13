---
entity_id: "protein.P62601"
entity_type: "protein"
name: "treF"
source_database: "UniProt"
source_id: "P62601"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01059, ECO:0000269|PubMed:10816581}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "treF b3519 JW3487"
---

# treF

`protein.P62601`

## Static

- Type: `protein`
- Source: `UniProt:P62601`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01059, ECO:0000269|PubMed:10816581}.

## Enriched Summary

FUNCTION: Hydrolyzes trehalose to glucose. Could be involved, in cells returning to low osmolarity conditions, in the utilization of the accumulated cytoplasmic trehalose, which was synthesized in response to high osmolarity. E. coli contains two trehalases: the cytoplasmic TreF (discussed here) and the periplasmic TREHALAPERI-MONOMER "TreA". Both enzymes catalyze the hydrolysis of trehalose into two molecules of D-glucose. Transcription of treF is only weakly induced by high osmolarity and partially dependent on the stationary-phase alternative sigma factor RpoS . Under aerobic conditions, TreF protein is induced more than 20-fold by high osmolarity .

## Biological Role

Catalyzes alpha,alpha-trehalose glucohydrolase (reaction.R00010), TREHALA-RXN (reaction.ecocyc.TREHALA-RXN).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Hydrolyzes trehalose to glucose. Could be involved, in cells returning to low osmolarity conditions, in the utilization of the accumulated cytoplasmic trehalose, which was synthesized in response to high osmolarity.

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00010|reaction.R00010]] `KEGG` `database` - via EC:3.2.1.28
- `catalyzes` --> [[reaction.ecocyc.TREHALA-RXN|reaction.ecocyc.TREHALA-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3519|gene.b3519]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P62601`
- `KEGG:ecj:JW3487;eco:b3519;ecoc:C3026_19065;`
- `GeneID:948037;`
- `GO:GO:0004555; GO:0005737; GO:0005993; GO:0071474`
- `EC:3.2.1.28`

## Notes

Cytoplasmic trehalase (EC 3.2.1.28) (Alpha,alpha-trehalase) (Alpha,alpha-trehalose glucohydrolase)
