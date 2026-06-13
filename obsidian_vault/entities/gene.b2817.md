---
entity_id: "gene.b2817"
entity_type: "gene"
name: "amiC"
source_database: "NCBI RefSeq"
source_id: "gene-b2817"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2817"
  - "amiC"
---

# amiC

`gene.b2817`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2817`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

amiC (gene.b2817) is a gene entity. It encodes amiC (protein.P63883). Encoded protein function: FUNCTION: Cell-wall hydrolase involved in septum cleavage during cell division. Can also act as powerful autolysin in the presence of murein synthesis inhibitors. {ECO:0000269|PubMed:11454209, ECO:0000269|PubMed:18390656}. EcoCyc product frame: G7458-MONOMER. EcoCyc synonyms: ygdN. Genomic coordinates: 2947757-2949010. EcoCyc protein note: AmiC is an N-acetylmuramyl-L-alanine amidase, which cleaves the peptide moiety from N-acetylmuramic acid, removing murein crosslinks. AmiC is active toward the murein located at the septum and is therefore important for cell separation upon cell division . NACMURLALAAMI1-MONOMER "AmiA", NACMURLALAAMI2-MONOMER "AmiB" and AmiC appear to have overlapping functions . Murein amidase activity produces stemless or a-denuded-peptidoglycan denuded glycans. AmiC is translocated from the cytoplasm to the periplasm by the twin-arginine transport (Tat) system . During cell division, AmiC specifically localizes to the septal ring; localization is mediated by an N-terminal targeting domain and is dependent on FtsN. In small cells that have not begun dividing, AmiC is located throughout the periplasm . AmiC contains an N-terminal peptidoglycan binding domain and a C-terminal, zinc dependent, catalytic domain. The two domains are linked by a flexible segment...

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P63883|protein.P63883]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009238,ECOCYC:G7458,GeneID:947293`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2947757-2949010:-; feature_type=gene
