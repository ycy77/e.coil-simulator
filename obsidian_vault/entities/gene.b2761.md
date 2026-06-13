---
entity_id: "gene.b2761"
entity_type: "gene"
name: "cas3"
source_database: "NCBI RefSeq"
source_id: "gene-b2761"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2761"
  - "cas3"
---

# cas3

`gene.b2761`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2761`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cas3 (gene.b2761) is a gene entity. It encodes ygcB (protein.P38036). Encoded protein function: FUNCTION: CRISPR (clustered regularly interspaced short palindromic repeat), is an adaptive immune system that provides protection against mobile genetic elements (viruses, transposable elements and conjugative plasmids). CRISPR clusters contain sequences complementary to antecedent mobile elements and target invading nucleic acids. CRISPR clusters are transcribed and processed into CRISPR RNA (crRNA). Cas3 plus Cascade participate in CRISPR interference, the third stage of CRISPR immunity.; FUNCTION: Acts as an endonuclease, a 3'-5'exonuclease, and an ATP-dependent dsDNA helicase. Anneals and unwinds R-loops (in which crRNA binds the target DNA, displacing the noncomplementary strand). Unwinding requires ATP, annealing does not. Required along with the Cascade complex for resistance to bacteriophage lambda infection as well as the ability to cure CRISPR-encoding high-copy number plasmid. A Cas3-CasA fusion protein purified with the Cascade complex nicks target plasmid in the presence but not absence of Mg(2+), and degrades plasmid fully in the presence of Mg(2+) and ATP, suggesting the helicase activity is required for complete degradation. EcoCyc product frame: EG12634-MONOMER. EcoCyc synonyms: ygcB. Genomic coordinates: 2884553-2887219...

## Biological Role

Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P38036|protein.P38036]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=cas3; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009054,ECOCYC:EG12634,GeneID:947229`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2884553-2887219:-; feature_type=gene
