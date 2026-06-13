---
entity_id: "gene.b3985"
entity_type: "gene"
name: "rplJ"
source_database: "NCBI RefSeq"
source_id: "gene-b3985"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3985"
  - "rplJ"
---

# rplJ

`gene.b3985`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3985`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplJ (gene.b3985) is a gene entity. It encodes rplJ (protein.P0A7J3). Encoded protein function: FUNCTION: Forms part of the ribosomal stalk, playing a central role in the interaction of the ribosome with GTP-bound translation factors. {ECO:0000269|PubMed:15923259}.; FUNCTION: Protein L10 is also a translational repressor protein. It controls the translation of the rplJL-rpoBC operon by binding to its mRNA. {ECO:0000269|PubMed:2448482}. EcoCyc product frame: EG10871-MONOMER. Genomic coordinates: 4179996-4180493. EcoCyc protein note: The L10 protein is a component of the 50S subunit of the ribosome and also regulates the expression of the L10 (β) operon at the posttranscriptional level. L10 forms a complex with L7/L12; this complex was originally identified as the L8 subunit . L10 and L7/L12 bind to the 23S rRNA early during assembly of the 50S subunit . Binding of L10 to 23S rRNA can be separated from binding to L7/L12 ; two binding sites in the C terminus of L10 are required for the binding of two L7/L12 dimers, but not for assembly of L10 into the ribosome . Synthesis of L10 and L7/L12 is regulated at the level of translation initiation . Expression of L12 is closely linked to expression of L10 , and a region within the leader sequence of the L10 operon mRNA regulates the translation efficiency of L10 and L7/L12 . The L10 protein acts at a single site in the leader mRNA...

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7J3|protein.P0A7J3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013035,ECOCYC:EG10871,GeneID:948490`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4179996-4180493:+; feature_type=gene
