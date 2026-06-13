---
entity_id: "gene.b3538"
entity_type: "gene"
name: "bcsG"
source_database: "NCBI RefSeq"
source_id: "gene-b3538"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3538"
  - "bcsG"
---

# bcsG

`gene.b3538`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3538`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bcsG (gene.b3538) is a gene entity. It encodes bcsG (protein.P37659). Encoded protein function: Cellulose biosynthesis protein BcsG EcoCyc product frame: EG12265-MONOMER. EcoCyc synonyms: yhjU. Genomic coordinates: 3698214-3699893. EcoCyc protein note: bcsE, bcsF and bcsG are part of the bacterial cellulose synthesis gene cluster; in other organisms these genes are involved in cellulose biosynthesis, a characteristic of the rdar (red, dry and rough) morphotype. However, the K-12 laboratory strain of E. coli does not show a rdar morphotype and does not produce cellulose . In the cellulose producing K-12 strain AR3110, BcsG is a membrane anchored, Zn2+-dependent phosphoethanolamine (pEtN) transferase which, as part of a multisubunit cellulose synthase complex, modifies cellulose with an additional pEtN group on every other glucosyl residue; BcsG interacts with EG12264-MONOMER "BcsF" and the cellulose synthase catalytic subunit EG12260-MONOMER "BcsA" (and see ). In E. coli K-12 strains such as W3110 and MG1655, a "domesticating SNP" consists of a point mutation that introduces a stop codon after the first 5 amino acids of the wild-type bcsQ ORF. This domesticating SNP lowers expression of both bcsQ and the downstream bcsA gene. After repairing the SNP, the resulting "de-domesticated" W3110 derivative strain produces cellulose and has dramatically altered biofilm morphology...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37659|protein.P37659]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=bcsG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011558,ECOCYC:EG12265,GeneID:948058`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3698214-3699893:+; feature_type=gene
