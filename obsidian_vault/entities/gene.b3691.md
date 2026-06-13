---
entity_id: "gene.b3691"
entity_type: "gene"
name: "dgoT"
source_database: "NCBI RefSeq"
source_id: "gene-b3691"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3691"
  - "dgoT"
---

# dgoT

`gene.b3691`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3691`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dgoT (gene.b3691) is a gene entity. It encodes dgoT (protein.P0AA76). Encoded protein function: FUNCTION: Involved in D-galactonate metabolism (PubMed:211976, PubMed:30455279). Catalyzes the proton-dependent uptake of galactonate into the cell (PubMed:31083648). {ECO:0000269|PubMed:211976, ECO:0000269|PubMed:30455279, ECO:0000269|PubMed:31083648}. EcoCyc product frame: YIDT-MONOMER. EcoCyc synonyms: yidT. Genomic coordinates: 3870438-3871730. EcoCyc protein note: DgoT is a D-galactonate:H+symporter; in the presence of D-galactonate, DgoT mediates uptake to support growth. Purified, reconstituted DgoT (from E. coli K-12 GM4792)* mediates D-galactonate:proton symport; transport is electrogenic - DgoT likely couples the import of D-galactonate to the movement of more than one proton (see also ). Crystal structures of the transporter in an inward open conformation showing a proton translocation pathway connected to the periplasm, and of a transport-inactive mutant in an outward facing, galactonate-bound conformation, have been reported . dgoT is part of a five gene operon (dgoRKADT) encoding proteins for the metablism of D-galactonate and a transcriptional regulator (DgoR); the operon is derepressed in the presence of D-galactonate . The dgoT::kan single gene deletion strain from the Keio library is unable to grow with D-galactonate as the carbon source...

## Biological Role

Repressed by dgoR (protein.P31460). Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA76|protein.P0AA76]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=dgoT; function=+
- `represses` <-- [[protein.P31460|protein.P31460]] `RegulonDB` `C` - regulator=DgoR; target=dgoT; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012072,ECOCYC:EG20053,GeneID:948196`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3870438-3871730:-; feature_type=gene
