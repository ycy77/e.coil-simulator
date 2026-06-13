---
entity_id: "gene.b2757"
entity_type: "gene"
name: "casD"
source_database: "NCBI RefSeq"
source_id: "gene-b2757"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2757"
  - "casD"
---

# casD

`gene.b2757`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2757`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

casD (gene.b2757) is a gene entity. It encodes casD (protein.Q46898). Encoded protein function: FUNCTION: CRISPR (clustered regularly interspaced short palindromic repeat), is an adaptive immune system that provides protection against mobile genetic elements (viruses, transposable elements and conjugative plasmids). CRISPR clusters contain sequences complementary to antecedent mobile elements and target invading nucleic acids. CRISPR clusters are transcribed and processed into CRISPR RNA (crRNA).; FUNCTION: A component of Cascade, which participates in CRISPR interference, the third stage of CRISPR immunity. Cascade binds both crRNA and in a sequence-specific manner negatively supercoiled dsDNA target. This leads to the formation of an R-loop in which the crRNA binds the target DNA, displacing the noncomplementary strand. Cas3 is recruited to Cascade, nicks target DNA and then unwinds and cleaves the target, leading to DNA degradation and invader neutralization. CasCDE alone is also able to form R-loops. EcoCyc product frame: G7427-MONOMER. EcoCyc synonyms: ygcI, cas5e. Genomic coordinates: 2880374-2881048. EcoCyc protein note: CasD interacts with one CasC subunit (Cas7.6) and with CasA to form the tail of the Cascade complex. CasD also contributes to crRNA binding . Residues in the L1-helix and the β-hairpin of CasD are required for dsDNA binding of Cascade...

## Biological Role

Repressed by hns (protein.P0ACF8), crp (protein.P0ACJ8). Activated by slyA (protein.P0A8W2), stpA (protein.P0ACG1), leuO (protein.P10151).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46898|protein.Q46898]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=casD; function=+
- `activates` <-- [[protein.P0ACG1|protein.P0ACG1]] `RegulonDB` `C` - regulator=StpA; target=casD; function=+
- `activates` <-- [[protein.P10151|protein.P10151]] `RegulonDB` `C` - regulator=LeuO; target=casD; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=casD; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=casD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009044,ECOCYC:G7427,GeneID:947225`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2880374-2881048:-; feature_type=gene
