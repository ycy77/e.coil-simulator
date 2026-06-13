---
entity_id: "gene.b3465"
entity_type: "gene"
name: "rsmD"
source_database: "NCBI RefSeq"
source_id: "gene-b3465"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3465"
  - "rsmD"
---

# rsmD

`gene.b3465`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3465`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rsmD (gene.b3465) is a gene entity. It encodes rsmD (protein.P0ADX9). Encoded protein function: FUNCTION: Specifically methylates the guanine in position 966 of 16S rRNA in the assembled 30S particle. {ECO:0000269|PubMed:17189261}. EcoCyc product frame: EG10343-MONOMER. EcoCyc synonyms: yhhF. Genomic coordinates: 3604393-3604989. EcoCyc protein note: RsmD is the methyltransferase responsible for methylation of 16S rRNA at the N2 postion of the G966 nucleotide . Its substrate is the 16S ribosomal subunit, but not free unmethylated 16S rRNA . RsmD binds 30S ribosomal subunits with rRNA unmodified at G996 tightly . Binding of S7 and S19 together to 16S rRNA allows methylation by RsmD . Methylation of G966 and C967 in 16S rRNA appears to stabilize the binding of initiator tRNA to the 30S pre-initiation complex prior to recognition of the start codon, thus modulating the early stages of translation initiation . A crystal structure of RsmD has been solved at 2.05 Å resolution; the structure shows strong similarity to that of the RsmC methyltransferase . rsmD mutants appear to have no growth defect when grown alone, but have a modest effect on cell fitness in a growth competition assay . Deletion of rsmD alters the initiation frequency from certain translation initiation codons . Review:

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADX9|protein.P0ADX9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011321,ECOCYC:EG10343,GeneID:947977`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3604393-3604989:+; feature_type=gene
