---
entity_id: "gene.b2709"
entity_type: "gene"
name: "norR"
source_database: "NCBI RefSeq"
source_id: "gene-b2709"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2709"
  - "norR"
---

# norR

`gene.b2709`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2709`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

norR (gene.b2709) is a gene entity. It encodes norR (protein.P37013). Encoded protein function: FUNCTION: Required for the expression of anaerobic nitric oxide (NO) reductase, acts as a transcriptional activator for at least the norVW operon. Activation also requires sigma-54. Not required for induction of the aerobic NO-detoxifying enzyme NO dioxygenase. Binds to the promoter region of norVW, to a consensus target sequence, GT-(N7)-AC, which is highly conserved among proteobacteria. {ECO:0000269|PubMed:11751865, ECO:0000269|PubMed:12586421}. EcoCyc product frame: EG12108-MONOMER. EcoCyc synonyms: ygaA. Genomic coordinates: 2830775-2832289. EcoCyc protein note: NorR, "NO reduction and detoxification Regulator," is one of several regulatory proteins, such as Fur, SoxR, and OxyR, that are involved in the response to reactive nitrogen species. Under anaerobic and microaerobic conditions it activates transcription of the norVW operon, encoding a nitric oxide (NO)-reducing flavorubredoxin that detoxifies NO . It was determined by Genomic SELEX screening that NorR binds strongly only between norR and norVW, and it binds with minor strength between genes such as sad/yneJ and glpF/zapB . It has been classified as a single-target transcription factor...

## Biological Role

Repressed by norR (protein.P37013).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37013|protein.P37013]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37013|protein.P37013]] `RegulonDB` `C` - regulator=NorR; target=norR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008904,ECOCYC:EG12108,GeneID:947186`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2830775-2832289:-; feature_type=gene
