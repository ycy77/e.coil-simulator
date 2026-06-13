---
entity_id: "gene.b0604"
entity_type: "gene"
name: "dsbG"
source_database: "NCBI RefSeq"
source_id: "gene-b0604"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0604"
  - "dsbG"
---

# dsbG

`gene.b0604`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0604`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dsbG (gene.b0604) is a gene entity. It encodes dsbG (protein.P77202). Encoded protein function: FUNCTION: Involved in disulfide bond formation. DsbG and DsbC are part of a periplasmic reducing system that controls the level of cysteine sulfenylation, and provides reducing equivalents to rescue oxidatively damaged secreted proteins such as ErfK, YbiS and YnhG. Probably also functions as a disulfide isomerase with a narrower substrate specificity than DsbC. DsbG is maintained in a reduced state by DsbD. Displays chaperone activity in both redox states in vitro. {ECO:0000269|PubMed:19965429}. EcoCyc product frame: DSBG-MONOMER. EcoCyc synonyms: ybdP. Genomic coordinates: 637827-638573.

## Biological Role

Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), oxyR (protein.P0ACQ4), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77202|protein.P77202]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `S` - regulator=OxyR; target=dsbG; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=dsbG; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002084,ECOCYC:G6333,GeneID:945224`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:637827-638573:-; feature_type=gene
