---
entity_id: "gene.b0081"
entity_type: "gene"
name: "mraZ"
source_database: "NCBI RefSeq"
source_id: "gene-b0081"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0081"
  - "mraZ"
---

# mraZ

`gene.b0081`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0081`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mraZ (gene.b0081) is a gene entity. It encodes mraZ (protein.P22186). Encoded protein function: FUNCTION: Negatively regulates its own expression and that of the subsequent genes in the proximal part of the division and cell wall (dcw) gene cluster. Acts by binding directly to DNA. May also regulate the expression of genes outside the dcw cluster. {ECO:0000255|HAMAP-Rule:MF_01008, ECO:0000269|PubMed:24659771}. EcoCyc product frame: EG11084-MONOMER. EcoCyc synonyms: yabB. Genomic coordinates: 89634-90092. EcoCyc protein note: MraZ is a transcriptional repressor involved in the control of cell division and cell wall genes . Based on differential gene expression analysis comparing the WT to a mraZ mutant, 100 genes under the control of MraZ were identified . The analysis showed that three successive TGGGN direct repeats are separated by two consecutive 5-nt spacers . By using synthetic gene circuits, it was demonstrated that MraZ acts as an activator under the tested conditions, with stronger activation when its binding site is located at positions +1 and -57 relative to the promoter compared to the distal upstream position -103 . The MraZ protein is highly conserved in bacteria , and MraW is more universal . MraZ is similar in both structure and sequence to the DNA-binding transition-state regulator AbrB from Bacillus subtilis...

## Biological Role

Repressed by pdhR (protein.P0ACL9), mraZ (protein.P22186).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P22186|protein.P22186]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=mraZ; function=-
- `represses` <-- [[protein.P22186|protein.P22186]] `RegulonDB` `C` - regulator=MraZ; target=mraZ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000302,ECOCYC:EG11084,GeneID:944810`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:89634-90092:+; feature_type=gene
