---
entity_id: "gene.b3264"
entity_type: "gene"
name: "envR"
source_database: "NCBI RefSeq"
source_id: "gene-b3264"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3264"
  - "envR"
---

# envR

`gene.b3264`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3264`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

envR (gene.b3264) is a gene entity. It encodes envR (protein.P0ACT2). Encoded protein function: FUNCTION: Potential regulator protein for the acrEF/envCD genes. EcoCyc product frame: EG11741-MONOMER. EcoCyc synonyms: acrS, yhdK. Genomic coordinates: 3412803-3413465. EcoCyc protein note: EnvR, also known as AcrS, represses the transcription of genes encoding a drug efflux pump that has a role in resistance to antibiotics . This protein is homologous to some other proteins, such as MtrR of Neisseria gonorrhoeae, TcmR of Streptomyces glaucescens, JadR2 from Streptomyces venezuelae, and AcrR from Escherichia coli . All of these proteins, including EnvR, have a helix-turn-helix motif close to the N terminus . EnvR recognizes and binds a 24-bp palindromic DNA sequence . The same sequence is also recognized by the transcriptional repressor AcrR . envR is adjacent and divergent in the genome to acrEF, an operon that encodes another drug efflux pump; however, it is not regulated or is only lightly affected by EnvR . Both of these transcription units appears to be repressed by HNS . Based on wide-scale analyses, the conservation of the TetR-family transcriptional regulators (TFTRs) across two genera, Escherichia and Salmonella, were analyzed and compared on three levels: genus, species, and strain...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACT2|protein.P0ACT2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010712,ECOCYC:EG11741,GeneID:947704`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3412803-3413465:-; feature_type=gene
