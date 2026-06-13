---
entity_id: "gene.b3680"
entity_type: "gene"
name: "yidL"
source_database: "NCBI RefSeq"
source_id: "gene-b3680"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3680"
  - "yidL"
---

# yidL

`gene.b3680`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3680`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yidL (gene.b3680) is a gene entity. It encodes yidL (protein.P31449). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YidL EcoCyc product frame: EG11707-MONOMER. Genomic coordinates: 3860283-3861176. EcoCyc protein note: YidL was predicted to be an AraC-type transcription factor and it was predicted that this protein regulates genes related to metabolism and transport . Genome-wide YidL binding sites were determined in vivo by the chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium . Expression of yidL is positively regulated by BglJ-RcsB and negatively regulated by HNS . This gene is affected by conditions that lead to biofilm formation . Insertion mutants showed reduced growth in M9 glucose minimal medium compared to growth in rich medium . Mutations in yidL were identified in copper-resistant strains evolved experimentally .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31449|protein.P31449]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012034,ECOCYC:EG11707,GeneID:948186`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3860283-3861176:+; feature_type=gene
