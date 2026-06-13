---
entity_id: "gene.b1448"
entity_type: "gene"
name: "mnaT"
source_database: "NCBI RefSeq"
source_id: "gene-b1448"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1448"
  - "mnaT"
---

# mnaT

`gene.b1448`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1448`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mnaT (gene.b1448) is a gene entity. It encodes mnaT (protein.P76112). Encoded protein function: FUNCTION: Acyltransferase that appears to be required for E.coli optimal growth rate and yield via the formation of N-acetylated amino acids. Catalyzes the acylation of L-methionine using acetyl-CoA or propanoyl-CoA as acyl donors, and the acetylation of L-phenylglycine (PubMed:27941785). Is also able to N-acylate other free L-amino acids and their derivatives using a CoA thioester as cosubstrate. Using acetyl-CoA as an acyl donor, substrate specificity is methionine sulfone > methionine sulfoximine > methionine sulfoxide > methionine. Asparagine, lysine, glutamine, aspartate and glutamate are very poor substrates. Using methionine as a substrate, acyl donor preference is propanoyl-CoA > acetyl-CoA >> butyryl-CoA (Ref.4). Likely plays a role in the resistance against the toxic effects of L-methionine sulfoximine (MSX), via its ability to catalyze its acetylation; MSX is a rare amino acid which inhibits glutamine synthetase (GlnA) (By similarity). {ECO:0000250|UniProtKB:Q8ZPD3, ECO:0000269|PubMed:27941785, ECO:0000269|Ref.4}. EcoCyc product frame: G6759-MONOMER. EcoCyc synonyms: yncA. Genomic coordinates: 1518328-1518846.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76112|protein.P76112]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004827,ECOCYC:G6759,GeneID:946010`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1518328-1518846:-; feature_type=gene
