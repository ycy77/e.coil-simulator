---
entity_id: "gene.b2018"
entity_type: "gene"
name: "hisL"
source_database: "NCBI RefSeq"
source_id: "gene-b2018"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2018"
  - "hisL"
---

# hisL

`gene.b2018`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2018`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hisL (gene.b2018) is a gene entity. It encodes hisL (protein.P60995). Encoded protein function: FUNCTION: This protein is involved in the attenuation mechanism for the control of the expression of the his operon structural genes. EcoCyc product frame: EG11269-MONOMER. Genomic coordinates: 2089996-2090046. EcoCyc protein note: The HisL leader peptide controls by attenuation the transcription of the hisLGDCBHAFI operon (which encodes the enzymes of the histidine biosynthesis pathway). HisL contains seven histidine residues as its attenuation regulatory points within a 16 amino acid long peptide . Moreover, the hisL and the tRNAHis sequences have been detected to be homologs, implying that both can interact with or be the target of the same regulatory effects , which may have important effects in the operon expression. Reviews:

## Biological Role

Repressed by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), argR (protein.P0A6D0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60995|protein.P60995]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=hisL; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006710,ECOCYC:EG11269,GeneID:946547`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2089996-2090046:+; feature_type=gene
