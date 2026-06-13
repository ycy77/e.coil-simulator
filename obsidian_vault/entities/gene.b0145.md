---
entity_id: "gene.b0145"
entity_type: "gene"
name: "dksA"
source_database: "NCBI RefSeq"
source_id: "gene-b0145"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0145"
  - "dksA"
---

# dksA

`gene.b0145`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0145`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dksA (gene.b0145) is a gene entity. It encodes dksA (protein.P0ABS1). Encoded protein function: FUNCTION: Transcription factor that acts by binding directly to the RNA polymerase (RNAP). Required for negative regulation of rRNA expression and positive regulation of several amino acid biosynthesis promoters. Also required for regulation of fis expression. Binding to RNAP disrupts interaction of RNAP with DNA, inhibits formation of initiation complexes, and amplifies effects of ppGpp and the initiating NTP on rRNA transcription. Inhibits transcript elongation, exonucleolytic RNA cleavage and pyrophosphorolysis, and increases intrinsic termination. Also involved, with RecN, in repair of DNA double-strand breaks. Required, probably upstream of the two-component system BarA-UvrY, for expression of CsrA-antagonistic small RNAs CsrB and CsrC (PubMed:21488981). {ECO:0000255|HAMAP-Rule:MF_00926, ECO:0000269|PubMed:15294156, ECO:0000269|PubMed:15294157, ECO:0000269|PubMed:15948952, ECO:0000269|PubMed:16885445, ECO:0000269|PubMed:21488981, ECO:0000269|PubMed:22210857}. EcoCyc product frame: EG10230-MONOMER. EcoCyc synonyms: msmA. Genomic coordinates: 160149-160604. EcoCyc protein note: The DksA protein binds directly to RNA polymerase, affecting transcript elongation and potentiating allosterically the effect of the alarmone ppGpp on transcription initiation...

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABS1|protein.P0ABS1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000499,ECOCYC:EG10230,GeneID:944850`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:160149-160604:-; feature_type=gene
