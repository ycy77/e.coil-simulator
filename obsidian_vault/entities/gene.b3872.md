---
entity_id: "gene.b3872"
entity_type: "gene"
name: "yihL"
source_database: "NCBI RefSeq"
source_id: "gene-b3872"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3872"
  - "yihL"
---

# yihL

`gene.b3872`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3872`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yihL (gene.b3872) is a gene entity. It encodes yihL (protein.P0ACM9). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YihL EcoCyc product frame: EG11838-MONOMER. Genomic coordinates: 4060447-4061157. EcoCyc protein note: The YihL putative transcriptional regulator belongs to the GntR family . This protein contains a helix-turn-helix motif to bind DNA in its N-terminal domain, and it was predicted to regulate genes related to metabolism . Genome-wide YihL binding sites were determined in vivo by the chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium . The transcription of the yihL gene is affected by temperature and oxidative stress . YihL was transcriptionally upregulated in iron excess over iron limitation at 63% dissolved oxygen as determined by RNA-seq .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACM9|protein.P0ACM9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yihL; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012651,ECOCYC:EG11838,GeneID:948368`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4060447-4061157:+; feature_type=gene
