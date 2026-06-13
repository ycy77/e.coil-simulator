---
entity_id: "gene.b2760"
entity_type: "gene"
name: "casA"
source_database: "NCBI RefSeq"
source_id: "gene-b2760"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2760"
  - "casA"
---

# casA

`gene.b2760`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2760`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

casA (gene.b2760) is a gene entity. It encodes casA (protein.Q46901). Encoded protein function: FUNCTION: CRISPR (clustered regularly interspaced short palindromic repeat), is an adaptive immune system that provides protection against mobile genetic elements (viruses, transposable elements and conjugative plasmids). CRISPR clusters contain sequences complementary to antecedent mobile elements and target invading nucleic acids. CRISPR clusters are transcribed and processed into CRISPR RNA (crRNA).; FUNCTION: A component of Cascade, which participates in CRISPR interference, the third stage of CRISPR immunity. Cascade binds both crRNA and in a sequence-specific manner negatively supercoiled dsDNA target. This leads to the formation of an R-loop in which the crRNA binds the target DNA, displacing the noncomplementary strand. Cas3 is recruited to Cascade, probably via interactions with CasA, nicks target DNA and then unwinds and cleaves the target, leading to DNA degradation and invader neutralization. CasA is not required for formation of Cascade, but probably enhances binding to and subsequent recognition of both target dsDNA and ssDNA. EcoCyc product frame: G7430-MONOMER. EcoCyc synonyms: ygcL, cse1. Genomic coordinates: 2882630-2884138. EcoCyc protein note: CasA interacts with CasB and with CasD in the Cascade complex...

## Biological Role

Repressed by hns (protein.P0ACF8), crp (protein.P0ACJ8), glaR (protein.P37338). Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), slyA (protein.P0A8W2), stpA (protein.P0ACG1), leuO (protein.P10151).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46901|protein.Q46901]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=casA; function=+
- `activates` <-- [[protein.P0ACG1|protein.P0ACG1]] `RegulonDB` `C` - regulator=StpA; target=casA; function=+
- `activates` <-- [[protein.P10151|protein.P10151]] `RegulonDB` `S` - regulator=LeuO; target=casA; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=casA; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=casA; function=-
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=casA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009050,ECOCYC:G7430,GeneID:947222`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2882630-2884138:-; feature_type=gene
