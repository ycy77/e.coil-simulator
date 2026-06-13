---
entity_id: "gene.b3537"
entity_type: "gene"
name: "bcsF"
source_database: "NCBI RefSeq"
source_id: "gene-b3537"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3537"
  - "bcsF"
---

# bcsF

`gene.b3537`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3537`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bcsF (gene.b3537) is a gene entity. It encodes bcsF (protein.P0ADJ5). Encoded protein function: Cellulose biosynthesis protein BcsF EcoCyc product frame: EG12264-MONOMER. EcoCyc synonyms: yhjT. Genomic coordinates: 3698026-3698217. EcoCyc protein note: Products of the bcs gene cluster are involved in cellulose biosynthesis, a characteristic of the rdar (red, dry and rough) morphotype; the K-12 laboratory strain of E. coli does not show a rdar morphotype and does not produce cellulose (see ). In E. coli K-12 strains such as W3110 and MG1655, a "domesticating SNP" consists of a point mutation that introduces a stop codon after the first 5 amino acids of the wild-type bcsQ ORF. This domesticating SNP lowers expression of both bcsQ and the downstream bcsA gene. After repairing the SNP, the resulting "de-domesticated" W3110 derivative strain produces cellulose and has dramatically altered biofilm morphology. A ΔbcsEFG mutation introduced into this strain leads to significantly reduced cellulose biosynthesis . In the cellulose producing K-12 strain AR3110, BcsF interacts with the cellulose phosphoethanolamine (pEtN) transferase BcsG and with the c-di-GMP binding protein BcsE and is implicated in a pathway that controls pEtN cellulose modification; pEtN cellulose modification is reduced in an E...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADJ5|protein.P0ADJ5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=bcsF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011556,ECOCYC:EG12264,GeneID:948059`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3698026-3698217:+; feature_type=gene
