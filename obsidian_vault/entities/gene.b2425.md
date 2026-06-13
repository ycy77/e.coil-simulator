---
entity_id: "gene.b2425"
entity_type: "gene"
name: "cysP"
source_database: "NCBI RefSeq"
source_id: "gene-b2425"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2425"
  - "cysP"
---

# cysP

`gene.b2425`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2425`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cysP (gene.b2425) is a gene entity. It encodes cysP (protein.P16700). Encoded protein function: FUNCTION: Part of the ABC transporter complex CysAWTP (TC 3.A.1.6.1) involved in sulfate/thiosulfate import. This protein specifically binds thiosulfate and is involved in its transmembrane transport. EcoCyc product frame: CYSP-MONOMER. Genomic coordinates: 2542512-2543528. EcoCyc protein note: CysP (also known as thiosulfate binding protein or TSBP) is the periplasmic binding protein of an ATP dependent thiosulfate/sulfate uptake system. cysP is the first gene of a five gene operon (cysPUWAM); cysP is expressed from a PC00040 "CysB" dependent promoter . Assays of sulfate and thiosulfate binding and uptake suggest that CysP is primarily a thiosulfate binding protein . cysP insertional mutants are not cysteine auxotrophs but they do have reduced growth with either sulfate or thiosulfate as the sulfur source . Double cysP sbp mutants (cysP::Cat sbp::Kan) are cysteine auxotrophs; growth on sulfate (and thiosulfate) as sole sulfur source can be restored in the double mutant by multicopy expression of either cysP or sbp however growth is impaired compared to the wild type strain; CysP and Sbp have overlapping specificity and both are required for wild-type levels of sulfate/thiosulfate transport

## Biological Role

Activated by rpoD (protein.P00579), cysB (protein.P0A9F3).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16700|protein.P16700]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cysP; function=+
- `activates` <-- [[protein.P0A9F3|protein.P0A9F3]] `RegulonDB` `S` - regulator=CysB; target=cysP; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007992,ECOCYC:EG10195,GeneID:946883`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2542512-2543528:-; feature_type=gene
