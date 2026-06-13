---
entity_id: "gene.b3536"
entity_type: "gene"
name: "bcsE"
source_database: "NCBI RefSeq"
source_id: "gene-b3536"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3536"
  - "bcsE"
---

# bcsE

`gene.b3536`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3536`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bcsE (gene.b3536) is a gene entity. It encodes bcsE (protein.P37657). Encoded protein function: FUNCTION: Binds bis-(3'-5') cyclic diguanylic acid (c-di-GMP), the ability to bind c-di-GMP is important for its function (PubMed:24942809). {ECO:0000269|PubMed:24942809}. EcoCyc product frame: EG12263-MONOMER. EcoCyc synonyms: yhjS. Genomic coordinates: 3696458-3698029. EcoCyc protein note: BcsE has been identified as a c-di-GMP-binding protein. The central DUF2819 domain, renamed GIL for GGDEF I-site-like domain, is sufficient for c-di-GMP binding . Products of the bcs gene cluster are involved in cellulose biosynthesis, a characteristic of the rdar (red, dry and rough) morphotype; the K-12 laboratory strain of E. coli does not show a rdar morphotype and does not produce cellulose . In the cellulose producing K-12 strain AR3110, BcsE interacts with the cellulose phosphoethanolamine (pEtN) transferase EG12265-MONOMER "BcsG" suggesting that pEtN cellulose modification is controlled by the biofilm-promoting second messenger c-di-GMP ; pEtN cellulose modification is strongly reduced in an E. coli K-12 AR3110 ΔbcsE mutant . BcsE also contributes to cellulose production - deleting bcsE in E. coli strain AR3110 ΔcsgBA (which produces cellulose but no curli) results in decreased cellulose production . In E...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37657|protein.P37657]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=bcsE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011554,ECOCYC:EG12263,GeneID:948050`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3696458-3698029:+; feature_type=gene
