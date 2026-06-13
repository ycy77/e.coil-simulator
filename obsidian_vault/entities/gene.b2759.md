---
entity_id: "gene.b2759"
entity_type: "gene"
name: "casB"
source_database: "NCBI RefSeq"
source_id: "gene-b2759"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2759"
  - "casB"
---

# casB

`gene.b2759`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2759`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

casB (gene.b2759) is a gene entity. It encodes casB (protein.P76632). Encoded protein function: FUNCTION: CRISPR (clustered regularly interspaced short palindromic repeat), is an adaptive immune system that provides protection against mobile genetic elements (viruses, transposable elements and conjugative plasmids). CRISPR clusters contain sequences complementary to antecedent mobile elements and target invading nucleic acids. CRISPR clusters are transcribed and processed into CRISPR RNA (crRNA).; FUNCTION: A component of Cascade, which participates in CRISPR interference, the third stage of CRISPR immunity. Cascade binds both crRNA and in a sequence-specific manner negatively supercoiled dsDNA target. This leads to the formation of an R-loop in which the crRNA binds the target DNA, displacing the noncomplementary strand. Cas3 is recruited to Cascade, nicks target DNA and then unwinds and cleaves the target, leading to DNA degradation and invader neutralization. EcoCyc product frame: G7429-MONOMER. EcoCyc synonyms: ygcK, cse2. Genomic coordinates: 2882155-2882637. EcoCyc protein note: The two CasB subunits (Cse2.1 and Cse2.2) form a head to tail dimer that contacts the CasC helical backbone of the Cascade complex; the CasB subunits do not contact crRNA but may function to stabilise bound target DNA . An insertion mutant in casB/ygcK shows lower transposition of IS903...

## Biological Role

Repressed by hns (protein.P0ACF8), crp (protein.P0ACJ8). Activated by slyA (protein.P0A8W2), stpA (protein.P0ACG1), leuO (protein.P10151).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76632|protein.P76632]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=casB; function=+
- `activates` <-- [[protein.P0ACG1|protein.P0ACG1]] `RegulonDB` `C` - regulator=StpA; target=casB; function=+
- `activates` <-- [[protein.P10151|protein.P10151]] `RegulonDB` `C` - regulator=LeuO; target=casB; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=casB; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=casB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009048,ECOCYC:G7429,GeneID:947223`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2882155-2882637:-; feature_type=gene
