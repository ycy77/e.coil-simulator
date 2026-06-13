---
entity_id: "gene.b3400"
entity_type: "gene"
name: "hslR"
source_database: "NCBI RefSeq"
source_id: "gene-b3400"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3400"
  - "hslR"
---

# hslR

`gene.b3400`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3400`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hslR (gene.b3400) is a gene entity. It encodes hslR (protein.P0ACG8). Encoded protein function: FUNCTION: Involved in the recycling of free 50S ribosomal subunits that still carry a nascent chain. Binds RNA more specifically than DNA. Binds with very high affinity to the free 50S ribosomal subunit. Does not bind it when it is part of the 70S ribosome. EcoCyc product frame: G7743-MONOMER. EcoCyc synonyms: hsp15, yrfH. Genomic coordinates: 3529348-3529749. EcoCyc protein note: Hsp15 is an abundant, highly conserved heat shock protein with DNA and RNA binding activity . In vivo, Hsp15 specifically interacts with the CPLX0-3962 when it contains a nascent polypeptide chain and is involved in recycling such complexes . The crystal structure of Hsp15 has been determined at 2 Å resolution, revealing a novel RNA binding motif that is widely shared among stress proteins, ribosomal proteins and tRNA synthetases . The structure of the 50S ribosomal subunit-nascent chain tRNA complex alone and with Hsp15 has been reconstructed using cryo-electron microscopy . The levels of hslR mRNA and Hsp15 protein are strongly upregulated after heat shock treatment . HslR: "heat shock locus R"

## Biological Role

Activated by rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACG8|protein.P0ACG8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=hslR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011094,ECOCYC:G7743,GeneID:947912`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3529348-3529749:+; feature_type=gene
