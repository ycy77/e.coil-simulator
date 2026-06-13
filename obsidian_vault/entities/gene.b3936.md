---
entity_id: "gene.b3936"
entity_type: "gene"
name: "rpmE"
source_database: "NCBI RefSeq"
source_id: "gene-b3936"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3936"
  - "rpmE"
---

# rpmE

`gene.b3936`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3936`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpmE (gene.b3936) is a gene entity. It encodes rpmE (protein.P0A7M9). Encoded protein function: FUNCTION: Binds the 23S rRNA. {ECO:0000250}. EcoCyc product frame: EG10889-MONOMER. Genomic coordinates: 4127013-4127225. EcoCyc protein note: The L31 protein is a component of the 50S subunit of the ribosome. An atomic model for L31 within the 70S ribosome was obtained by single-particle cryo-EM. L31 bridges the 30S and 50S subunits between the 30S head and the 50S central protuberance. A flexible linker region in L31 accomodates large-scale rearrangements during ratcheting of the ribosome . L31 is involved in translation initiation, reading frame maintenance , stabilization of subunit association , and formation of 100S ribosomes in stationary phase . L31 also counteracts intrinsic ribosome destabilization by certain nascent peptide sequences . L31 can be isolated in a complex with 5S rRNA and L5, L18, and L25 and can be crosslinked to tRNA in the P site . Modeling shows that L31 may participate in the formation, dynamics and stabilization of the S13-L5 bridge . L31 may only be loosely associated with the ribosome . An extensive crosslinking and mass spectrometry study of ribosomal proteins clarified the localization and flexibility of L31 within the ribosome . Expression of L31 is autoregulated. The N-terminal residues 2-8 of L31 are required for autoregulatory activity...

## Biological Role

Repressed by rpmE (protein.P0A7M9).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7M9|protein.P0A7M9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A7M9|protein.P0A7M9]] `RegulonDB` `S` - regulator=RpmE; target=rpmE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012867,ECOCYC:EG10889,GeneID:948425`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4127013-4127225:+; feature_type=gene
