---
entity_id: "gene.b2756"
entity_type: "gene"
name: "casE"
source_database: "NCBI RefSeq"
source_id: "gene-b2756"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2756"
  - "casE"
---

# casE

`gene.b2756`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2756`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

casE (gene.b2756) is a gene entity. It encodes casE (protein.Q46897). Encoded protein function: FUNCTION: CRISPR (clustered regularly interspaced short palindromic repeat), is an adaptive immune system that provides protection against mobile genetic elements (viruses, transposable elements and conjugative plasmids). CRISPR clusters contain sequences complementary to antecedent mobile elements and target invading nucleic acids. CRISPR clusters are transcribed and processed into CRISPR RNA (crRNA).; FUNCTION: CasE is required to process the pre-crRNA into single repeat-spacer units, with an 8-nt 5'-repeat DNA tag that may help other proteins recognize the crRNA. This subunit alone will cleave pre-crRNA, as will CasCDE or CasCE; cleavage does not require divalent metals or ATP. CasCDE alone is also able to form R-loops. Partially inhibits the cleavage of Holliday junctions by YgbT (Cas1). Yields a 5'-hydroxy group and a 2',3'-cyclic phosphate terminus.; FUNCTION: A component of Cascade, which participates in CRISPR interference, the third stage of CRISPR immunity. Cascade binds both crRNA and in a sequence-specific manner negatively supercoiled dsDNA target. This leads to the formation of an R-loop in which the crRNA binds the target DNA, displacing the noncomplementary strand...

## Biological Role

Repressed by hns (protein.P0ACF8), crp (protein.P0ACJ8). Activated by slyA (protein.P0A8W2), stpA (protein.P0ACG1), leuO (protein.P10151).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46897|protein.Q46897]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=casE; function=+
- `activates` <-- [[protein.P0ACG1|protein.P0ACG1]] `RegulonDB` `C` - regulator=StpA; target=casE; function=+
- `activates` <-- [[protein.P10151|protein.P10151]] `RegulonDB` `S` - regulator=LeuO; target=casE; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=casE; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=casE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009042,ECOCYC:G7426,GeneID:947226`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2879788-2880387:-; feature_type=gene
