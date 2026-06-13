---
entity_id: "gene.b1972"
entity_type: "gene"
name: "msrQ"
source_database: "NCBI RefSeq"
source_id: "gene-b1972"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1972"
  - "msrQ"
---

# msrQ

`gene.b1972`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1972`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

msrQ (gene.b1972) is a gene entity. It encodes msrQ (protein.P76343). Encoded protein function: FUNCTION: Part of the MsrPQ system that repairs oxidized periplasmic proteins containing methionine sulfoxide residues (Met-O), using respiratory chain electrons. Thus protects these proteins from oxidative-stress damage caused by reactive species of oxygen and chlorine. MsrPQ is essential for the maintenance of envelope integrity under bleach stress, rescuing a wide series of structurally unrelated periplasmic proteins from methionine oxidation, including the primary periplasmic chaperone SurA and the lipoprotein Pal. MsrQ provides electrons for reduction to the reductase catalytic subunit MsrP, using the quinone pool of the respiratory chain. {ECO:0000269|PubMed:26641313}. EcoCyc product frame: G7060-MONOMER. EcoCyc synonyms: yedZ. Genomic coordinates: 2040483-2041118. EcoCyc protein note: MsrQ (formerly YedZ) is a heme-binding, inner membrane quinol dehydrogenase that provides reducing equivalents to MsrP which in turn, reduces oxidized methionine residues of functionally diverse periplasmic proteins. The MsrPQ system protects periplasmic proteins, including SurA and Pal, from oxidative damage...

## Biological Role

Activated by cusR (protein.P0ACZ8), phoB (protein.P0AFJ5), hprR (protein.P76340).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76343|protein.P76343]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACZ8|protein.P0ACZ8]] `RegulonDB` `S` - regulator=CusR; target=msrQ; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=msrQ; function=+
- `activates` <-- [[protein.P76340|protein.P76340]] `RegulonDB` `C` - regulator=HprR; target=msrQ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006542,ECOCYC:G7060,GeneID:946483`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2040483-2041118:+; feature_type=gene
