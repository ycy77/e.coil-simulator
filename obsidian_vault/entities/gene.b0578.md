---
entity_id: "gene.b0578"
entity_type: "gene"
name: "nfsB"
source_database: "NCBI RefSeq"
source_id: "gene-b0578"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0578"
  - "nfsB"
---

# nfsB

`gene.b0578`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0578`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nfsB (gene.b0578) is a gene entity. It encodes nfsB (protein.P38489). Encoded protein function: FUNCTION: Reduction of a variety of nitroaromatic compounds using NADH (and to lesser extent NADPH) as source of reducing equivalents; two electrons are transferred. Capable of reducing nitrofurazone, quinones and the anti-tumor agent CB1954 (5-(aziridin-1-yl)-2,4-dinitrobenzamide). The reduction of CB1954 results in the generation of cytotoxic species. {ECO:0000269|PubMed:15684426}. EcoCyc product frame: DIHYDROPTERIREDUCT-MONOMER. EcoCyc synonyms: ntr, dprA, nfnB. Genomic coordinates: 604771-605424. EcoCyc protein note: The nfsB-encoded nitroreductase is the minor oxygen-insensitive nitroreductase present in E. coli K-12. NfsB reduces a broad range of nitroaromatic compounds , including the antibiotics nitrofurazone and nitrofurantoin . NfsB is a flavin mononucleotide (FMN)-containing protein and uses both NADH and NADPH as a source of reducing equivalents . FAD can substitute for FMN as an effective prosthetic group . NfsB catalyzes the reduction of nitrocompounds using a ping-pong Bi-Bi mechanism . The reduction of nitroaromatic compounds consists of two successive, two-electron transfer reactions to reduce nitroaromatics to their hydroxylamine derivatives...

## Biological Role

Activated by soxS (protein.P0A9E2), marA (protein.P0ACH5).

## Enriched Pathways

- `eco00633` Nitrotoluene degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P38489|protein.P38489]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `S` - regulator=SoxS; target=nfsB; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=nfsB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001981,ECOCYC:EG50005,GeneID:945778`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:604771-605424:-; feature_type=gene
