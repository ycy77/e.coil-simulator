---
entity_id: "gene.b2067"
entity_type: "gene"
name: "dgcE"
source_database: "NCBI RefSeq"
source_id: "gene-b2067"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2067"
  - "dgcE"
---

# dgcE

`gene.b2067`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2067`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dgcE (gene.b2067) is a gene entity. It encodes dgcE (protein.P38097). Encoded protein function: FUNCTION: Catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP molecules (By similarity). Involved in the control of the switch from cell motility to adhesion via regulation of cellular levels of c-di-GMP (PubMed:20303158). Part of a signaling cascade that regulates curli biosynthesis (PubMed:23708798). The cascade is composed of two c-di-GMP control modules, in which c-di-GMP controlled by the DgcE/PdeH pair (module I) regulates the activity of the DgcM/PdeR pair (module II), which in turn regulates activity of the transcription factor MlrA and expression of the master biofilm regulator csgD (PubMed:23708798). {ECO:0000250|UniProtKB:P31129, ECO:0000269|PubMed:20303158, ECO:0000269|PubMed:23708798}. EcoCyc product frame: EG12396-MONOMER. EcoCyc synonyms: yegE. Genomic coordinates: 2143266-2146583.

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P38097|protein.P38097]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006845,ECOCYC:EG12396,GeneID:946600`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2143266-2146583:+; feature_type=gene
