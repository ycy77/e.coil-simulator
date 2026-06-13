---
entity_id: "gene.b2605"
entity_type: "gene"
name: "yfiB"
source_database: "NCBI RefSeq"
source_id: "gene-b2605"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2605"
  - "yfiB"
---

# yfiB

`gene.b2605`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2605`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfiB (gene.b2605) is a gene entity. It encodes yfiB (protein.P07021). Encoded protein function: Putative lipoprotein YfiB EcoCyc product frame: EG11152-MONOMER. Genomic coordinates: 2743625-2744107. EcoCyc protein note: YfiB is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). Under the conditions examined, yfiB is not essential for viability of E. coli . A yfiB deletion mutant shows increased early biofilm formation . Under conditions when the C. elegans gut microbiota consists of a single E. coli ΔyfiB mutant strain, the life span of the nematode increases by 20% compared to colonization with wild-type E. coli . yfiR, yfiN and yfiB may form an operon in E. coli K-12. In Pseudomonas aeruginosa this operon is involved in exopolysaccharide synthesis ; in uropathogenic E. coli YfiR and YfiN were shown to have a role in cellulose production, but no evidence implicating YfiB in this process was obtained . E. coli K-12 does not produce cellulose due to a mutation in the bcs operon (see EG12261).

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07021|protein.P07021]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yfiB; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008572,ECOCYC:EG11152,GeneID:947094`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2743625-2744107:+; feature_type=gene
