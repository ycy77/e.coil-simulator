---
entity_id: "gene.b3289"
entity_type: "gene"
name: "rsmB"
source_database: "NCBI RefSeq"
source_id: "gene-b3289"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3289"
  - "rsmB"
---

# rsmB

`gene.b3289`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3289`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rsmB (gene.b3289) is a gene entity. It encodes rsmB (protein.P36929). Encoded protein function: FUNCTION: Specifically methylates the cytosine at position 967 (m5C967) of 16S rRNA (PubMed:10026269, PubMed:10194318). It recognizes protein-free synthetic 16S RNA as a substrate (PubMed:10026269). {ECO:0000269|PubMed:10026269, ECO:0000269|PubMed:10194318}. EcoCyc product frame: EG12163-MONOMER. EcoCyc synonyms: yhdB, rrmB, fmu, fmv, sun. Genomic coordinates: 3435207-3436496. EcoCyc protein note: RsmB is the methyltransferase responsible for methylation of 16S rRNA at the C967 nucleotide . In vitro, the enzyme is active on free 16S rRNA, but not 30S ribosomal subunits . Methylation of G966 and C967 in 16S rRNA appears to stabilize the binding of initiator tRNA to the 30S pre-initiation complex prior to recognition of the start codon, thus modulating the early stages of translation initiation . The crystal structure of the apoenzyme has been solved at 1.65 Å resolution, and that of the enzyme complexed with AdoMet at 2.1 Å resolution . A null mutation in rsmB has no significant effect on the growth rate in rich or minimal media , although competitive growth experiments reveal a fitness defect . Deletion of rsmB alters the initiation frequency from certain translation initiation codons . A C375A mutant is catalytically inactive, while a C325A mutant retains activity...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36929|protein.P36929]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010785,ECOCYC:EG12163,GeneID:947789`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3435207-3436496:+; feature_type=gene
