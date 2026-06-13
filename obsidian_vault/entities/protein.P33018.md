---
entity_id: "protein.P33018"
entity_type: "protein"
name: "yeiG"
source_database: "UniProt"
source_id: "P33018"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yeiG b2154 JW2141"
---

# yeiG

`protein.P33018`

## Static

- Type: `protein`
- Source: `UniProt:P33018`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Serine hydrolase involved in the detoxification of formaldehyde. Hydrolyzes S-formylglutathione to glutathione and formate. Also shows esterase activity against alpha-naphthyl acetate, lactoylglutathione, palmitoyl-CoA and several pNP-esters of short chain fatty acids. {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16567800}. YeiG is a promiscuous serine hydrolase; its highest specific activity is with the substrate S-formylglutathione. Sulfhydryl inhibitors affect enzymatic activity . A general esterase activity of YeiG was first discovered in a high-throughput screen of purified proteins . YeiG also has significant activity with the substrate lactoylglutathione, an intermediate of the detoxification of methylglyoxal. It may thus represent a cytoplasmic equivalent of glyoxalase II, which may be involved in the detoxification of endogenous methylglyoxal . YeiG has similarity to S-formylglutathione hydrolases of Arabidopsis, S. cerevisiae, human, and a paralog, FrmB . yeiG is expressed constitutively in both the wild type and frmB deletion background. Under normal growth conditions, neither a yeiG deletion mutant nor a frmB yeiG double mutant have a detectable growth defect. Addition of 0.4 mM formaldehyde to the growth medium had no effect on the yeiG single mutant, while the growth rate of the double mutant drops to 43% of wild type...

## Biological Role

Catalyzes S-formylglutathione hydrolase (reaction.R00527). Component of S-formylglutathione hydrolase / S-lactoylglutathione hydrolase (complex.ecocyc.CPLX0-3954).

## Enriched Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Serine hydrolase involved in the detoxification of formaldehyde. Hydrolyzes S-formylglutathione to glutathione and formate. Also shows esterase activity against alpha-naphthyl acetate, lactoylglutathione, palmitoyl-CoA and several pNP-esters of short chain fatty acids. {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16567800}.

## Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00527|reaction.R00527]] `KEGG` `database` - via EC:3.1.2.12
- `is_component_of` --> [[complex.ecocyc.CPLX0-3954|complex.ecocyc.CPLX0-3954]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2154|gene.b2154]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33018`
- `KEGG:ecj:JW2141;eco:b2154;ecoc:C3026_12075;`
- `GeneID:949045;`
- `GO:GO:0004416; GO:0005829; GO:0018738; GO:0032991; GO:0042802; GO:0046294; GO:0051289; GO:0052689`
- `EC:3.1.2.12`

## Notes

S-formylglutathione hydrolase YeiG (FGH) (EC 3.1.2.12)
