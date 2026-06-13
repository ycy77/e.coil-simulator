---
entity_id: "protein.P51025"
entity_type: "protein"
name: "frmB"
source_database: "UniProt"
source_id: "P51025"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "frmB yaiM b0355 JW0346"
---

# frmB

`protein.P51025`

## Static

- Type: `protein`
- Source: `UniProt:P51025`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Serine hydrolase involved in the detoxification of formaldehyde. Hydrolyzes S-formylglutathione to glutathione and formate. Also shows esterase activity against two pNP-esters (pNP-acetate and pNP-propionate), alpha-naphthyl acetate and lactoylglutathione. {ECO:0000269|PubMed:16567800}. FrmB is a promiscuous serine hydrolase; its highest specific activity is with the substrate S-formylglutathione. Sulfhydryl inhibitors affect enzymatic activity . FrmB is encoded in an operon with FrmR and FrmA, which are proteins involved in the oxidation of formaldehyde. FrmB has similarity to the S-formylglutathione hydrolase of Paracoccus denitrificans and a paralog, YeiG . Formaldehyde stimulates expression of frmB 45-fold in wild type and 70-fold in a yeiG deletion background. Under normal growth conditions, neither a frmB deletion mutant nor a frmB yeiG double mutant have a detectable growth defect. Addition of 0.4 mM formaldehyde to the growth medium caused only a small growth defect in the frmB single mutant, while the growth rate of the double mutant drops to 43% of wild type . Overexpression of frmB from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hypochlorous acid .

## Biological Role

Catalyzes S-formylglutathione hydrolase (reaction.R00527), S-FORMYLGLUTATHIONE-HYDROLASE-RXN (reaction.ecocyc.S-FORMYLGLUTATHIONE-HYDROLASE-RXN).

## Enriched Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Serine hydrolase involved in the detoxification of formaldehyde. Hydrolyzes S-formylglutathione to glutathione and formate. Also shows esterase activity against two pNP-esters (pNP-acetate and pNP-propionate), alpha-naphthyl acetate and lactoylglutathione. {ECO:0000269|PubMed:16567800}.

## Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00527|reaction.R00527]] `KEGG` `database` - via EC:3.1.2.12
- `catalyzes` --> [[reaction.ecocyc.S-FORMYLGLUTATHIONE-HYDROLASE-RXN|reaction.ecocyc.S-FORMYLGLUTATHIONE-HYDROLASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0355|gene.b0355]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P51025`
- `KEGG:ecj:JW0346;eco:b0355;`
- `GeneID:944991;`
- `GO:GO:0005829; GO:0018738; GO:0046292; GO:0046294; GO:0052689`
- `EC:3.1.2.12`

## Notes

S-formylglutathione hydrolase FrmB (FGH) (EC 3.1.2.12)
