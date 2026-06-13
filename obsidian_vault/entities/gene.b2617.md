---
entity_id: "gene.b2617"
entity_type: "gene"
name: "bamE"
source_database: "NCBI RefSeq"
source_id: "gene-b2617"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2617"
  - "bamE"
---

# bamE

`gene.b2617`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2617`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bamE (gene.b2617) is a gene entity. It encodes bamE (protein.P0A937). Encoded protein function: FUNCTION: Part of the outer membrane protein assembly complex (Bam), which is involved in assembly and insertion of beta-barrel proteins into the outer membrane. Nonessential member of the complex that stabilizes the interaction between the essential proteins BamA and BamD. May modulate the conformation of BamA, likely through interactions with BamD. Efficient substrate folding and insertion into the outer membrane requires all 5 subunits (PubMed:20378773, PubMed:21823654, PubMed:27686148). A lateral gate may open between the first and last strands of the BamA beta-barrel that allows substrate to insert into the outer membrane; comparison of the structures of complete and nearly complete Bam complexes show there is considerable movement of all 5 proteins (PubMed:26744406, PubMed:26900875, PubMed:26901871, PubMed:27686148). {ECO:0000269|PubMed:17404237, ECO:0000269|PubMed:20378773, ECO:0000269|PubMed:21207987, ECO:0000269|PubMed:21586578, ECO:0000269|PubMed:21823654, ECO:0000269|PubMed:22178970, ECO:0000269|PubMed:26744406, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871, ECO:0000269|PubMed:27686148}. EcoCyc product frame: EG10952-MONOMER. EcoCyc synonyms: smpA, smqA. Genomic coordinates: 2753605-2753946...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A937|protein.P0A937]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=bamE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008614,ECOCYC:EG10952,GeneID:945583`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2753605-2753946:+; feature_type=gene
