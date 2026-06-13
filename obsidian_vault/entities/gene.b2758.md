---
entity_id: "gene.b2758"
entity_type: "gene"
name: "casC"
source_database: "NCBI RefSeq"
source_id: "gene-b2758"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2758"
  - "casC"
---

# casC

`gene.b2758`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2758`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

casC (gene.b2758) is a gene entity. It encodes casC (protein.Q46899). Encoded protein function: FUNCTION: CRISPR (clustered regularly interspaced short palindromic repeat), is an adaptive immune system that provides protection against mobile genetic elements (viruses, transposable elements and conjugative plasmids). CRISPR clusters contain sequences complementary to antecedent mobile elements and target invading nucleic acids. CRISPR clusters are transcribed and processed into CRISPR RNA (crRNA).; FUNCTION: A component of Cascade, which participates in CRISPR interference, the third stage of CRISPR immunity. Cascade binds both crRNA and in a sequence-specific manner negatively supercoiled dsDNA target. This leads to the formation of an R-loop in which the crRNA binds the target DNA, displacing the noncomplementary strand. Cas3 is recruited to Cascade, nicks target DNA and then unwinds and cleaves the target, leading to DNA degradation and invader neutralization. CasCDE alone is also able to form R-loops. EcoCyc product frame: G7428-MONOMER. EcoCyc synonyms: ygcJ, cse4, cas7. Genomic coordinates: 2881051-2882142. EcoCyc protein note: The 6 CasC (Cas7.1 - Cas7.6) subunits of the Cascade complex form a helical structure that binds crRNA and presents it for target DNA binding. Bound crRNA presents as 6 segments with a kink occurring at every 6th ribonucleotide...

## Biological Role

Repressed by hns (protein.P0ACF8), crp (protein.P0ACJ8). Activated by slyA (protein.P0A8W2), stpA (protein.P0ACG1), leuO (protein.P10151).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46899|protein.Q46899]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=casC; function=+
- `activates` <-- [[protein.P0ACG1|protein.P0ACG1]] `RegulonDB` `C` - regulator=StpA; target=casC; function=+
- `activates` <-- [[protein.P10151|protein.P10151]] `RegulonDB` `C` - regulator=LeuO; target=casC; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=casC; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=casC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009046,ECOCYC:G7428,GeneID:947224`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2881051-2882142:-; feature_type=gene
