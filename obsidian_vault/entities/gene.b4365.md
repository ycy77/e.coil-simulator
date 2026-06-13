---
entity_id: "gene.b4365"
entity_type: "gene"
name: "yjjQ"
source_database: "NCBI RefSeq"
source_id: "gene-b4365"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4365"
  - "yjjQ"
---

# yjjQ

`gene.b4365`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4365`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjjQ (gene.b4365) is a gene entity. It encodes yjjQ (protein.P0ADD7). Encoded protein function: Putative transcription factor YjjQ EcoCyc product frame: G7947-MONOMER. Genomic coordinates: 4603477-4604202. EcoCyc protein note: YjjQ is a transcriptional repressor of genes required for flagellar synthesis, capsule formation, and other genes related to virulence . Repression is mediated by binding to a palindromic DNA motif. Episomal expression of yjjQ inhibits motility and biofilm formation . YjjQ harbors a FixJ/NarL-type C-terminal helix-turn-helix DNA-binding domain . YjjQ may play a role in detoxification of methylglyoxal (MG) and dihydroxyacetone (DHA) . YjjQ belongs to the LuxR family of transcriptional regulators. The orthologous protein in avian pathogenic E. coli and in Salmonella enterica serovar Typhimurium may play a role in virulence. A yjjQ insertion mutant increases the sensitivity of a gloA mutant to MG and DHA. A strain containing only the yjjQ insertion mutation does not show increased sensitivity to MG or DHA . yjjQ is expressed in an operon together with bglJ ; it is located upstream of bglJ, and thus the mutant phenotype of the yjjQ insertion mutant could be due to a polar effect on bglJ. Transcription of the yjjQ gene is upregulated in cells cultivated in LB broth in the presence of the antibiotics kanamycin, mitomycin C or ciprofloxacin...

## Biological Role

Repressed by hns (protein.P0ACF8), glaR (protein.P37338). Activated by leuO (protein.P10151).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADD7|protein.P0ADD7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P10151|protein.P10151]] `RegulonDB` `S` - regulator=LeuO; target=yjjQ; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=yjjQ; function=-
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yjjQ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0014322,ECOCYC:G7947,GeneID:948896`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4603477-4604202:+; feature_type=gene
