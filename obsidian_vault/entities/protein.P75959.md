---
entity_id: "protein.P75959"
entity_type: "protein"
name: "nagK"
source_database: "UniProt"
source_id: "P75959"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nagK ycfX b1119 JW1105"
---

# nagK

`protein.P75959`

## Static

- Type: `protein`
- Source: `UniProt:P75959`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of N-acetyl-D-glucosamine (GlcNAc) derived from cell-wall degradation, yielding GlcNAc-6-P. Has also low level glucokinase activity in vitro. {ECO:0000269|PubMed:15489439}. N-acetyl-D-glucosamine (GlcNAc) is released in the cytoplasm during murein recycling. NagK is the only known cytoplasmic GlcNAc kinase in E. coli . The enzyme was originally purified and studied by Asensio and Ruiz-Amil who reported a high affinity and specificity for GlcNAc, marginal activity on D-glucose and no detectable activity on D-glucosamine, N-methyl D-glucosamine, N-acetyl-D-mannosamine nor N-acetyl-D-galactosamine . Overexpression of nagK rescues the glucose auxotrophy of a glucokinase mutant, and the NagK protein functions as a rudimentary glucokinase in vitro . The Km of NagK for glucose is 100-fold higher than its Km for GlcNAc . Contrary to expectations, a nagK mutant does not accumulate GlcNAc in the cytoplasm, suggesting the presence of an additional pathway for GlcNAc utilization . The PTS transporter NagE was found to contribute to this pathway . nagK is expressed constitutively . NagK: "N-acetylglucosamine kinase" Review:

## Biological Role

Catalyzes N-ACETYLGLUCOSAMINE-KINASE-RXN (reaction.ecocyc.N-ACETYLGLUCOSAMINE-KINASE-RXN).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorylation of N-acetyl-D-glucosamine (GlcNAc) derived from cell-wall degradation, yielding GlcNAc-6-P. Has also low level glucokinase activity in vitro. {ECO:0000269|PubMed:15489439}.

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.N-ACETYLGLUCOSAMINE-KINASE-RXN|reaction.ecocyc.N-ACETYLGLUCOSAMINE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1119|gene.b1119]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75959`
- `KEGG:ecj:JW1105;eco:b1119;ecoc:C3026_06740;`
- `GeneID:75171243;945664;`
- `GO:GO:0005524; GO:0006044; GO:0008270; GO:0009254; GO:0045127`
- `EC:2.7.1.59`

## Notes

N-acetyl-D-glucosamine kinase (EC 2.7.1.59) (GlcNAc kinase)
