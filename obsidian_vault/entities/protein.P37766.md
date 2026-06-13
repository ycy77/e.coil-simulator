---
entity_id: "protein.P37766"
entity_type: "protein"
name: "ydiF"
source_database: "UniProt"
source_id: "P37766"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ydiF b1694 JW1684"
---

# ydiF

`protein.P37766`

## Static

- Type: `protein`
- Source: `UniProt:P37766`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: CoA transferase having broad substrate specificity for short-chain acyl-CoA thioesters with the activity decreasing when the length of the carboxylic acid chain exceeds four carbons. May play a role in short-chain fatty acid metabolism in E.coli. {ECO:0000250|UniProtKB:Q8X5X6}. Based on sequence similarity, particularly with conserved motifs EXGXXG and GXGGF, YdiF is predicted to be an acetate CoA-transferase . YdiF not only catalyzes the formation of acetyl-CoA from acetate, it also catalyzes the conversion of lactyl-CoA from L-lactate both in vitro with purified YdiF and in vivo when overexpressed from a plasmid; the lactyl-CoA product is then used by EG12270-MONOMER . The enzyme from E. coli O157:H7 has broad substrate specificity for short-chain acyl-CoA thioesters. Crystal structures of the enzyme from E. coli O157:H7 have been solved; the enzyme is a homotetramer in a dimer of dimers configuration . The protein sequence of the O157:H7 enzyme (Q8X5X6) is 99% identical to that of the K-12 enzyme.

## Biological Role

Catalyzes acyl-CoA:acetate CoA-transferase (reaction.R00393), ACETOACETYL-COA-TRANSFER-RXN (reaction.ecocyc.ACETOACETYL-COA-TRANSFER-RXN), lactate-CoA transferase (reaction.ecocyc.RXN-25375).

## Enriched Pathways

- `eco00627` Aminobenzoate degradation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: CoA transferase having broad substrate specificity for short-chain acyl-CoA thioesters with the activity decreasing when the length of the carboxylic acid chain exceeds four carbons. May play a role in short-chain fatty acid metabolism in E.coli. {ECO:0000250|UniProtKB:Q8X5X6}.

## Pathways

- `eco00627` Aminobenzoate degradation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00393|reaction.R00393]] `KEGG` `database` - via EC:2.8.3.8
- `catalyzes` --> [[reaction.ecocyc.ACETOACETYL-COA-TRANSFER-RXN|reaction.ecocyc.ACETOACETYL-COA-TRANSFER-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-25375|reaction.ecocyc.RXN-25375]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1694|gene.b1694]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37766`
- `KEGG:ecj:JW1684;eco:b1694;`
- `GeneID:946211;`
- `GO:GO:0008775; GO:0046459; GO:0046952; GO:0051289`
- `EC:2.8.3.8`

## Notes

Acetate CoA-transferase YdiF (EC 2.8.3.8) (Short-chain acyl-CoA:acetate CoA-transferase)
