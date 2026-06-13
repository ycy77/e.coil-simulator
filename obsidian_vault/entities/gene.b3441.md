---
entity_id: "gene.b3441"
entity_type: "gene"
name: "yhhY"
source_database: "NCBI RefSeq"
source_id: "gene-b3441"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3441"
  - "yhhY"
---

# yhhY

`gene.b3441`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3441`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhhY (gene.b3441) is a gene entity. It encodes aaaT (protein.P46854). Encoded protein function: FUNCTION: Catalyzes the N-acetylation of L-phenylalanine and L-methionine using acetyl-CoA as acetyl donor in vitro. Cannot accept L-tyrosine as substrate and propionyl-CoA, succinyl-CoA or (S)-methylmalonyl-CoA as acyl donors (PubMed:27941785). Is also able to acetylate and thus detoxify several nonhydrolyzable aminoacyl adenylates, but not the processed form of the peptide-nucleotide antibiotic microcin C (McC). When overproduced, provides complete resistance to leucyl sulfamoyl adenylate (LSA) and partial resistance to alanyl sulfamoyl adenylate (ASA) and phenylalanyl sulfamoyl adenylate (FSA). Therefore, may protect bacteria from various toxic aminoacyl nucleotides, either exogenous or those generated inside the cell during normal metabolism (PubMed:25002546). {ECO:0000269|PubMed:25002546, ECO:0000269|PubMed:27941785}. EcoCyc product frame: G7758-MONOMER. Genomic coordinates: 3581138-3581626. EcoCyc protein note: YhhY is an acetyltransferase that is able to detoxify nonhydrolyzable aminoacyl adenylates. In vitro, YhhY is able to acetylate the synthetic aminoacyl sulfamoyl adenylates LSA and ISA, but not DSA and ESA . Transcription of yhhY is regulated by Fur .

## Biological Role

Activated by fur (protein.P0A9A9), zraR (protein.P14375).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46854|protein.P46854]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=yhhY; function=+
- `activates` <-- [[protein.P14375|protein.P14375]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=yhhY; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011240,ECOCYC:G7758,GeneID:947943`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3581138-3581626:+; feature_type=gene
