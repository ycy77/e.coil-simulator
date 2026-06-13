---
entity_id: "gene.b2452"
entity_type: "gene"
name: "eutH"
source_database: "NCBI RefSeq"
source_id: "gene-b2452"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2452"
  - "eutH"
---

# eutH

`gene.b2452`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2452`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

eutH (gene.b2452) is a gene entity. It encodes eutH (protein.P76552). Encoded protein function: FUNCTION: Probably involved in the diffusion of protonated ethanolamine (EA) into the cell at low pH. At low pH most EA is protonated, and this permease becomes necessary. {ECO:0000250|UniProtKB:P41796}. EcoCyc product frame: G7282-MONOMER. EcoCyc synonyms: yffU. Genomic coordinates: 2566881-2568107. EcoCyc protein note: Sequence analysis has identified EutH as a membrane protein with 11 transmembrane helices . A possible ethanolamine transport function for EutH has been suggested . Although it was initially found that a eutH mutant in Salmonella enterica is not defective for ethanolamine utilization , further studies showed a pH-dependent effect, and it is now thought that EutH facilitates diffusion of protonated ethanolamine across the cytoplasmic membrane .

## Biological Role

Repressed by hipB (protein.P23873).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76552|protein.P76552]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P23873|protein.P23873]] `RegulonDB` `S` - regulator=HipB; target=eutH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008081,ECOCYC:G7282,GeneID:944979`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2566881-2568107:-; feature_type=gene
