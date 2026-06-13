---
entity_id: "gene.b1971"
entity_type: "gene"
name: "msrP"
source_database: "NCBI RefSeq"
source_id: "gene-b1971"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1971"
  - "msrP"
---

# msrP

`gene.b1971`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1971`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

msrP (gene.b1971) is a gene entity. It encodes msrP (protein.P76342). Encoded protein function: FUNCTION: Part of the MsrPQ system that repairs oxidized periplasmic proteins containing methionine sulfoxide residues (Met-O), using respiratory chain electrons (PubMed:26641313). Thus protects these proteins from oxidative-stress damage caused by reactive species of oxygen and chlorine (PubMed:26641313). MsrPQ is essential for the maintenance of envelope integrity under bleach stress, rescuing a wide series of structurally unrelated periplasmic proteins from methionine oxidation, including the primary periplasmic chaperone SurA and the lipoprotein Pal (PubMed:26641313). The catalytic subunit MsrP is non-stereospecific, being able to reduce both (R-) and (S-) diastereoisomers of methionine sulfoxide (PubMed:26641313). Can catalyze the reduction of a variety of substrates in vitro, including dimethyl sulfoxide, trimethylamine N-oxide, phenylmethyl sulfoxide and L-methionine sulfoxide (PubMed:15355966, PubMed:30945846). Cannot reduce cyclic N-oxides (PubMed:15355966). Shows no activity as sulfite oxidase (PubMed:15355966). {ECO:0000269|PubMed:15355966, ECO:0000269|PubMed:26641313, ECO:0000269|PubMed:30945846}. EcoCyc product frame: G7059-MONOMER. EcoCyc synonyms: yedY. Genomic coordinates: 2039478-2040482...

## Biological Role

Activated by cusR (protein.P0ACZ8), phoB (protein.P0AFJ5), hprR (protein.P76340).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76342|protein.P76342]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACZ8|protein.P0ACZ8]] `RegulonDB` `S` - regulator=CusR; target=msrP; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=msrP; function=+
- `activates` <-- [[protein.P76340|protein.P76340]] `RegulonDB` `C` - regulator=HprR; target=msrP; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006540,ECOCYC:G7059,GeneID:946484`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2039478-2040482:+; feature_type=gene
