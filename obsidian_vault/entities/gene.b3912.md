---
entity_id: "gene.b3912"
entity_type: "gene"
name: "cpxR"
source_database: "NCBI RefSeq"
source_id: "gene-b3912"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3912"
  - "cpxR"
---

# cpxR

`gene.b3912`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3912`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cpxR (gene.b3912) is a gene entity. It encodes cpxR (protein.P0AE88). Encoded protein function: FUNCTION: Response regulator member of the two-component regulatory system CpxA/CpxR which responds to envelope stress response by activating expression of downstream genes including cpxP, degP, dsbA and ppiA (PubMed:7883164, PubMed:9401031). Required for efficient binding of stationary phase cells to hydrophobic surfaces, part of the process of biofilm formation (PubMed:11830644). Induced upon cell surface binding, subsequently induces genes it controls (cpxP, dsbA and spy, degP is only partially induced) (PubMed:11830644). Binds and activates transcription from the degP promoter (PubMed:7883164); binding is enhanced by phosphorylation (PubMed:9401031). This system combats a variety of extracytoplasmic protein-mediated toxicities by increasing the transcription of the periplasmic protease, DegP in concert with sigma factor E (PubMed:7883164), as well as that of CpxP protein. Other downstream effectors may include SrkA (PubMed:23416055). {ECO:0000269|PubMed:11830644, ECO:0000269|PubMed:23416055, ECO:0000269|PubMed:7883164, ECO:0000269|PubMed:9401031}. EcoCyc product frame: PHOSPHO-CPXR. EcoCyc synonyms: yiiA. Genomic coordinates: 4104972-4105670.

## Biological Role

Activated by cpxR (protein.P0AE88).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE88|protein.P0AE88]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `C` - regulator=CpxR; target=cpxR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012774,ECOCYC:EG10020,GeneID:948404`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4104972-4105670:-; feature_type=gene
