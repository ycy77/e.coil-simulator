---
entity_id: "gene.b0162"
entity_type: "gene"
name: "cdaR"
source_database: "NCBI RefSeq"
source_id: "gene-b0162"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0162"
  - "cdaR"
---

# cdaR

`gene.b0162`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0162`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cdaR (gene.b0162) is a gene entity. It encodes cdaR (protein.P37047). Encoded protein function: FUNCTION: Seems to regulate the expression of the operons for the enzymes involved in D-galactarate, D-glucarate and D-glycerate utilization. EcoCyc product frame: EG12335-MONOMER. EcoCyc synonyms: sdaR, yaeG. Genomic coordinates: 182463-183620. EcoCyc protein note: The "Carbohydrate diacid regulator," CdaR, or "sugar diacid regulator," SdaR, regulates genes involved in the uptake and metabolism of galactarate and glucarate, and it is also autoregulated . SdaR responds to d-galactarate and d-glucarate, and even better to d-glycerate to activate the genes it regulates . In addition, it was found that 2-O-α-mannosyl-d-glycerate (MG) can induce the SdaR regulon . MG has been recognized as a protective osmolyte in hyperthermophylic prokaryotes and as a carbon source for Escherichia coli . This protein has a helix-turn-helix motif for DNA binding in the C-terminal domain . CdaR was transcriptionally upregulated in iron excess over iron limitation at 63% dissolved oxygen as determined by RNA-seq . The exact position and sequence that SdaR binds to in DNA have not been yet determined. It has been observed that cdaR contains a single nucleotide mutation in cells induced for chlorhexidine (CHX) resistance, and its expression is repressed in these altered cells .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37047|protein.P37047]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=cdaR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000554,ECOCYC:EG12335,GeneID:944860`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:182463-183620:+; feature_type=gene
