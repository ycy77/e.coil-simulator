---
entity_id: "gene.b3525"
entity_type: "gene"
name: "pdeH"
source_database: "NCBI RefSeq"
source_id: "gene-b3525"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3525"
  - "pdeH"
---

# pdeH

`gene.b3525`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3525`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pdeH (gene.b3525) is a gene entity. It encodes pdeH (protein.P37646). Encoded protein function: FUNCTION: Involved in the control of the switch from cell motility to adhesion via regulation of cellular levels of cyclic-di-GMP (c-di-GMP) (PubMed:18765794). Part of a signaling cascade that regulates curli biosynthesis. The cascade is composed of two c-di-GMP control modules, in which c-di-GMP controlled by the DgcE/PdeH pair (module I) regulates the activity of the DgcM/PdeR pair (module II), which in turn regulates activity of the transcription factor MlrA and expression of the master biofilm regulator csgD (PubMed:23708798). Effect on flagella is controlled via the c-di-GMP-binding flagellar brake protein YcgR (PubMed:18765794). {ECO:0000269|PubMed:18765794, ECO:0000269|PubMed:23708798}. EcoCyc product frame: EG12252-MONOMER. EcoCyc synonyms: yhjH. Genomic coordinates: 3678420-3679187. EcoCyc protein note: Curli amyloid fibers are thin, coiled surface structures composed of a polymer of a single type of subunit, EG11489-MONOMER, encoded by the EG11489 gene . Curli are the key component of the extracellular matrix produced during biofilm formation by Escherichia coli and related Enterobacteriaceae and are involved in inert surface colonization, biofilm formation, and bacterial binding to a variety of extracellular matrix and serum proteins...

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37646|protein.P37646]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011515,ECOCYC:EG12252,GeneID:948042`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3678420-3679187:-; feature_type=gene
