---
entity_id: "gene.b1427"
entity_type: "gene"
name: "rimL"
source_database: "NCBI RefSeq"
source_id: "gene-b1427"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1427"
  - "rimL"
---

# rimL

`gene.b1427`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1427`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rimL (gene.b1427) is a gene entity. It encodes rimL (protein.P13857). Encoded protein function: FUNCTION: This enzyme acetylates the N-terminal serine of ribosomal protein bL12, converting it into the acetylated form of bL12 known as bL7. {ECO:0000269|PubMed:2671655}. EcoCyc product frame: EG10853-MONOMER. Genomic coordinates: 1498938-1499477. EcoCyc protein note: RimL is the acetyl transferase that acetylates the Nα-terminal serine residue of ribosomal protein L12, converting it into its modified form, L7 . Acetylation of L12 does not appear to be essential for its function . RimL can also acetylate a mutant ribosomal protein L12 which contains alanine instead of serine at the N-terminal position (after cleavage of the leading methionine); substitution of the adjacent amino acid with aspartate leads to lower catalytic efficiency . RimL is similar to the MccE acetyltransferase that acetylates and thereby provides resistance to processed microcin C (McC). RimL, but not RimI or RimJ, contributes to E. coli's basal level of resistance to McC and some of its analogs . A rimL mutant lacks ribosomal protein L7, the acetylated form of ribosomal protein L12 . RimL shows similarity to RimJ .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P13857|protein.P13857]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004763,ECOCYC:EG10853,GeneID:945998`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1498938-1499477:+; feature_type=gene
