---
entity_id: "gene.b0375"
entity_type: "gene"
name: "iprA"
source_database: "NCBI RefSeq"
source_id: "gene-b0375"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0375"
  - "iprA"
---

# iprA

`gene.b0375`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0375`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

iprA (gene.b0375) is a gene entity. It encodes iprA (protein.P0AAP5). Encoded protein function: FUNCTION: Involved in oxidative stress resistance. {ECO:0000255|HAMAP-Rule:MF_02072}. EcoCyc product frame: G6226-MONOMER. EcoCyc synonyms: yaiV. Genomic coordinates: 394506-395129. EcoCyc protein note: IprA, which is predicted to be a transcription factor, appears to belong to the CRP family, and it was predicted to regulate genes related to metabolism . Upstream of the iprA gene, a sequence was found that could work as a transcriptional promoter, and the transcription of the iprA gene is affected by conditions that lead to biofilm formation and general transcriptional termination . A ΔiprA mutant displays aggravating genetic interactions with several mismatch repair mutants and shows an 80,000-fold increase in resistance to oxidative stress . IprA: "inhibitor of hydrogen peroxide resistance A"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAP5|protein.P0AAP5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001290,ECOCYC:G6226,GeneID:946902`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:394506-395129:+; feature_type=gene
