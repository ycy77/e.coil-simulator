---
entity_id: "gene.b4473"
entity_type: "gene"
name: "smf"
source_database: "NCBI RefSeq"
source_id: "gene-b4473"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4473"
  - "smf"
---

# smf

`gene.b4473`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4473`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

smf (gene.b4473) is a gene entity. It encodes smf (protein.P30852). Encoded protein function: FUNCTION: Partially complements natural chromosomal DNA transformation defect of an H.influenzae dprA disruption mutant (PubMed:16978360). May help load RecA onto ssDNA (By similarity). {ECO:0000250|UniProtKB:Q8DPI7, ECO:0000269|PubMed:16978360}. EcoCyc product frame: EG11604-MONOMER. EcoCyc synonyms: b3286, b3285, smf1, smf2. Genomic coordinates: 3432436-3433560. EcoCyc protein note: The smf gene can partially complement the transformation defect of a Haemophilus influenzae dprA mutant. However, in E. coli, smf does not appear to have a role in transformation, conjugation, DNA repair, or recombination . smf is not required for spontaneous plasmid transformation on nutrient plates with high agar concentration . smf: inverse of fms

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30852|protein.P30852]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0174103,ECOCYC:EG11604,GeneID:2847708`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3432436-3433560:-; feature_type=gene
