---
entity_id: "gene.b4687"
entity_type: "gene"
name: "shoB"
source_database: "NCBI RefSeq"
source_id: "gene-b4687"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4687"
  - "shoB"
---

# shoB

`gene.b4687`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4687`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

shoB (gene.b4687) is a gene entity. It encodes shoB (protein.C1P611). Encoded protein function: FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system. May be a toxic protein; overexpression causes cessation of growth and rapid membrane depolarization. Overexpression induces stress-response and a number of membrane protein genes. {ECO:0000269|PubMed:18710431}. EcoCyc product frame: MONOMER0-2860. EcoCyc synonyms: yphI, ryfB, b4681. Genomic coordinates: 2700117-2700197. EcoCyc protein note: The small hydrophobic peptide ShoB is encoded within the small RNA sequence of ryfB . RyfB was identified in a cloning-based screen for small RNAs and shown to be expressed during exponential growth . Overexpression of ShoB is toxic to the cell by disrupting membrane integrity. Whole-genome gene expression analysis after induction of ShoB expression shows changes in expression of many stress response and membrane proteins . Overexpression of "RyfB" decreases swimming and swarming motility . ShoB is predicted to be a bitopic inner membrane protein . Regulatory elements are highly conserved across pathogenic and commensal E. coli . ShoB: "small hydrophobic ORF" Reviews:

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748). Activated by rpoD (protein.P00579), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.C1P611|protein.C1P611]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=shoB; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=shoB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ECOCYC:G0-10634,GeneID:7751620`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2700117-2700197:-; feature_type=gene
