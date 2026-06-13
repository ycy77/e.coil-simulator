---
entity_id: "gene.b4208"
entity_type: "gene"
name: "cycA"
source_database: "NCBI RefSeq"
source_id: "gene-b4208"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4208"
  - "cycA"
---

# cycA

`gene.b4208`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4208`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cycA (gene.b4208) is a gene entity. It encodes cycA (protein.P0AAE0). Encoded protein function: FUNCTION: Permease that is involved in the transport across the cytoplasmic membrane of D-alanine, D-serine, glycine and beta-alanine (PubMed:15221223, PubMed:23316042, PubMed:4574696, PubMed:4583203, PubMed:4926674). Also contributes to L-alanine uptake (PubMed:4574696, PubMed:4583203). In addition, in minimal media, transports the broad spectrum antibiotic D-cycloserine into the cell (PubMed:23316042, PubMed:4574696, PubMed:4926674). Transports D-cycloserine only in minimal media, and not in a complex medium, suggesting that CycA does not play a role in D-cycloserine transport when E.coli is grown in a complex or biologically relevant medium, probably due to competition from other CycA substrates present in the medium (PubMed:23316042). {ECO:0000269|PubMed:15221223, ECO:0000269|PubMed:23316042, ECO:0000269|PubMed:4574696, ECO:0000269|PubMed:4583203, ECO:0000269|PubMed:4926674}. EcoCyc product frame: CYCA-MONOMER. EcoCyc synonyms: ytfD, dagA. Genomic coordinates: 4429864-4431276. EcoCyc protein note: CycA is an inner membrane protein which mediates the uptake of D-serine, D-alanine, and glycine; it also contributes to L-alanine uptake, is the major transporter for β-alanine uptake and is implicated in the uptake of D-cycloserine...

## Biological Role

Repressed by arcA (protein.P0A9Q1), lrp (protein.P0ACJ0). Activated by CRP-cyclic-AMP DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-226), DNA-binding transcriptional dual regulator IHF (complex.ecocyc.PC00027), hns (protein.P0ACF8), crp (protein.P0ACJ8), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAE0|protein.P0AAE0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[complex.ecocyc.CPLX0-226|complex.ecocyc.CPLX0-226]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[complex.ecocyc.PC00027|complex.ecocyc.PC00027]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=cycA; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=cycA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=cycA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=cycA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013764,ECOCYC:EG12504,GeneID:948725`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4429864-4431276:+; feature_type=gene
