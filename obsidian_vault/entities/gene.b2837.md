---
entity_id: "gene.b2837"
entity_type: "gene"
name: "galR"
source_database: "NCBI RefSeq"
source_id: "gene-b2837"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2837"
  - "galR"
---

# galR

`gene.b2837`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2837`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

galR (gene.b2837) is a gene entity. It encodes galR (protein.P03024). Encoded protein function: FUNCTION: Repressor of the galactose operon. Binds galactose as an inducer. EcoCyc product frame: PD03028. EcoCyc synonyms: Rgal. Genomic coordinates: 2976599-2977630. EcoCyc protein note: The "Galactose repressor," GalR, is a DNA-binding transcription factor that represses transcription of the operons involved in transport and catabolism of D-galactose . Synthesis of these operons is induced when E. coli is grown in the presence of inducer (D-galactose) and the absence glucose . The expression of galR is increased only in the presence of inducer . In particular, in the absence of D-galactose, GalR represses the galETKM operon . In this repression system, GalR binds to two operators in the presence of HU, resulting in the formation of a repressor loop . This repressor binds in tandem to inverted repeat sequences that are 16 nucleotides long and possess conserved motifs; each dimer binds to one of these conserved sequences . On the other hand, GalR is highly homologous in its amino acid sequence to GalS (55% identical and 88% similar); apparently both act together and are capable of cross-talk to regulate expression of the gal regulon . For this reason these regulators bind the same operators, in the cis regulatory regions, with different affinities...

## Biological Role

Repressed by galR (protein.P03024).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P03024|protein.P03024]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P03024|protein.P03024]] `RegulonDB` `S` - regulator=GalR; target=galR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009307,ECOCYC:EG10364,GeneID:947314`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2976599-2977630:+; feature_type=gene
