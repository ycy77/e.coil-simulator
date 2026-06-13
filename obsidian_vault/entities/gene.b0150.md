---
entity_id: "gene.b0150"
entity_type: "gene"
name: "fhuA"
source_database: "NCBI RefSeq"
source_id: "gene-b0150"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0150"
  - "fhuA"
---

# fhuA

`gene.b0150`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0150`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fhuA (gene.b0150) is a gene entity. It encodes fhuA (protein.P06971). Encoded protein function: FUNCTION: Involved in the uptake of iron in complex with ferrichrome, a hydroxamate-type siderophore. Binds and transports ferrichrome-iron across the outer membrane (PubMed:1089064, PubMed:2066336). In addition to its role in ferrichrome-iron transport, transports the antibiotic albomycin, which is a structural analog of ferrichrome, and acts as a receptor for colicin M, microcin J25 and bacteriophages T1, T5, phi80 and UC-1 (PubMed:1089064, PubMed:2066336, PubMed:353030, PubMed:8617231). The energy source, which is required for all FhuA functions except infection by phage T5, is provided by the inner membrane TonB system (PubMed:12427941, PubMed:353030, PubMed:9353297). {ECO:0000269|PubMed:1089064, ECO:0000269|PubMed:12427941, ECO:0000269|PubMed:2066336, ECO:0000269|PubMed:353030, ECO:0000269|PubMed:8617231, ECO:0000269|PubMed:9353297}. EcoCyc product frame: EG10302-MONOMER. EcoCyc synonyms: T1, T5rec, tonA. Genomic coordinates: 167484-169727...

## Biological Role

Repressed by fur (protein.P0A9A9), zraR (protein.P14375).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06971|protein.P06971]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=fhuA; function=-
- `represses` <-- [[protein.P14375|protein.P14375]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000520,ECOCYC:EG10302,GeneID:944856`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:167484-169727:+; feature_type=gene
