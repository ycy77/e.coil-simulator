---
entity_id: "gene.b0287"
entity_type: "gene"
name: "yagU"
source_database: "NCBI RefSeq"
source_id: "gene-b0287"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0287"
  - "yagU"
---

# yagU

`gene.b0287`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0287`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yagU (gene.b0287) is a gene entity. It encodes yagU (protein.P0AAA1). Encoded protein function: Inner membrane protein YagU EcoCyc product frame: G6158-MONOMER. Genomic coordinates: 302991-303605. EcoCyc protein note: Membrane topology predictions using experimentally determined C terminus locations indicate that YagU has 4 transmembrane helices and the C-terminus is located in the cytoplasm . YagU has been found as a dimer in the inner membrane . Expression of yagU is induced by acid and repressed after induction of expression of the toxic peptide IbsC . A yagU mutant shows lower resistance to acid than wild type .

## Biological Role

Activated by lrp (protein.P0ACJ0), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAA1|protein.P0AAA1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yagU; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000995,ECOCYC:G6158,GeneID:945677`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:302991-303605:+; feature_type=gene
