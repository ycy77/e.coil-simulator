---
entity_id: "gene.b1283"
entity_type: "gene"
name: "osmB"
source_database: "NCBI RefSeq"
source_id: "gene-b1283"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1283"
  - "osmB"
---

# osmB

`gene.b1283`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1283`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

osmB (gene.b1283) is a gene entity. It encodes osmB (protein.P0ADA7). Encoded protein function: FUNCTION: Provides resistance to osmotic stress. May be important for stationary-phase survival. EcoCyc product frame: EG10679-MONOMER. Genomic coordinates: 1343110-1343328. EcoCyc protein note: osmB encodes an outer membrane lipoprotein . An osmB::TnphoA fusion is induced after growth in a medium of high osmolarity (0.3 M NaCl or 0.6 M sucrose) . osmB transcription is induced in response to hyperosmolarity or upon entry into stationary phase (see also ). osmB transcription increases following activation of the PWY0-1493 "RcsCDB phosphorelay; osmB belongs to the RcsA-independent subfamily of RcsB targets (see also ). OsmB plays a role in protection against the Vibrio cholerae type 6 secretion system effector, TseH osmB: osmo-inducible gene B .

## Biological Role

Activated by rpoD (protein.P00579), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADA7|protein.P0ADA7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=osmB; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=osmB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004309,ECOCYC:EG10679,GeneID:945866`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1343110-1343328:-; feature_type=gene
