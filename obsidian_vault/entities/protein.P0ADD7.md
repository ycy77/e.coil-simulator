---
entity_id: "protein.P0ADD7"
entity_type: "protein"
name: "yjjQ"
source_database: "UniProt"
source_id: "P0ADD7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yjjQ b4365 JW4329"
---

# yjjQ

`protein.P0ADD7`

## Static

- Type: `protein`
- Source: `UniProt:P0ADD7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Putative transcription factor YjjQ YjjQ is a transcriptional repressor of genes required for flagellar synthesis, capsule formation, and other genes related to virulence . Repression is mediated by binding to a palindromic DNA motif. Episomal expression of yjjQ inhibits motility and biofilm formation . YjjQ harbors a FixJ/NarL-type C-terminal helix-turn-helix DNA-binding domain . YjjQ may play a role in detoxification of methylglyoxal (MG) and dihydroxyacetone (DHA) . YjjQ belongs to the LuxR family of transcriptional regulators. The orthologous protein in avian pathogenic E. coli and in Salmonella enterica serovar Typhimurium may play a role in virulence. A yjjQ insertion mutant increases the sensitivity of a gloA mutant to MG and DHA. A strain containing only the yjjQ insertion mutation does not show increased sensitivity to MG or DHA . yjjQ is expressed in an operon together with bglJ ; it is located upstream of bglJ, and thus the mutant phenotype of the yjjQ insertion mutant could be due to a polar effect on bglJ. Transcription of the yjjQ gene is upregulated in cells cultivated in LB broth in the presence of the antibiotics kanamycin, mitomycin C or ciprofloxacin . The YjjQ binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data...

## Annotation

Putative transcription factor YjjQ

## Outgoing Edges (2)

- `represses` --> [[gene.b1891|gene.b1891]] `RegulonDB` `S` - regulator=YjjQ; target=flhC; function=-
- `represses` --> [[gene.b1892|gene.b1892]] `RegulonDB` `S` - regulator=YjjQ; target=flhD; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b4365|gene.b4365]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADD7`
- `KEGG:ecj:JW4329;eco:b4365;ecoc:C3026_23580;`
- `GeneID:948896;`
- `GO:GO:0000976; GO:0003700; GO:0006355; GO:0051595`

## Notes

Putative transcription factor YjjQ
