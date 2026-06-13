---
entity_id: "gene.b0177"
entity_type: "gene"
name: "bamA"
source_database: "NCBI RefSeq"
source_id: "gene-b0177"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0177"
  - "bamA"
---

# bamA

`gene.b0177`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0177`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bamA (gene.b0177) is a gene entity. It encodes bamA (protein.P0A940). Encoded protein function: FUNCTION: Part of the outer membrane protein assembly complex (Bam), which is involved in assembly and insertion of beta-barrel proteins into the outer membrane. Constitutes, with BamD, the core component of the assembly machinery. Efficient substrate folding and insertion into the outer membrane requires all 5 subunits (PubMed:20378773, PubMed:21823654, PubMed:27686148). A lateral gate may open between the first and last strands of the BamA beta-barrel that allows substrate to insert into the outer membrane; comparison of the structures of complete and nearly complete Bam complexes show there is considerable movement of all 5 proteins (PubMed:26744406, PubMed:26900875, PubMed:26901871, PubMed:27686148). {ECO:0000269|PubMed:15951436, ECO:0000269|PubMed:16102012, ECO:0000269|PubMed:16824102, ECO:0000269|PubMed:20378773, ECO:0000269|PubMed:21823654, ECO:0000269|PubMed:26744406, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871, ECO:0000269|PubMed:27686148}.; FUNCTION: (Microbial infection) Acts as a receptor for CdiA-EC93, the contact-dependent growth inhibition (CDI) effector of E.coli strain EC93; antibodies against extracellular epitopes decrease CDI. Its role in CDI is independent of the other Bam complex components (PubMed:18761695). Is not the receptor for CdiA from E...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A940|protein.P0A940]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=bamA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000605,ECOCYC:G6093,GeneID:944870`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:197928-200360:+; feature_type=gene
