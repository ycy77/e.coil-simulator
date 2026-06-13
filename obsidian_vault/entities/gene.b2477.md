---
entity_id: "gene.b2477"
entity_type: "gene"
name: "bamC"
source_database: "NCBI RefSeq"
source_id: "gene-b2477"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2477"
  - "bamC"
---

# bamC

`gene.b2477`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2477`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bamC (gene.b2477) is a gene entity. It encodes bamC (protein.P0A903). Encoded protein function: FUNCTION: Part of the outer membrane protein assembly complex (Bam), which is involved in assembly and insertion of beta-barrel proteins into the outer membrane. Nonessential member of the complex that stabilizes the interaction between the essential proteins BamA and BamD. Efficient substrate folding and insertion into the outer membrane requires all 5 subunits (PubMed:20378773, PubMed:21823654, PubMed:27686148). A lateral gate may open between the first and last strands of the BamA beta-barrel that allows substrate to insert into the outer membrane; comparison of the structures of complete and nearly complete Bam complexes show there is considerable movement of all 5 proteins (PubMed:26744406, PubMed:26900875, PubMed:26901871, PubMed:27686148). {ECO:0000269|PubMed:20378773, ECO:0000269|PubMed:21823654, ECO:0000269|PubMed:22178970, ECO:0000269|PubMed:26744406, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871, ECO:0000269|PubMed:27686148}. EcoCyc product frame: EG10658-MONOMER. EcoCyc synonyms: dapX, nlpB. Genomic coordinates: 2597831-2598865. EcoCyc protein note: The BamC (formerly NlpB) lipoprotein is part of the large multi-protein BAM complex responsible for the assembly and insertion of outer membrane β-barrel proteins in E.coli...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A903|protein.P0A903]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=bamC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008161,ECOCYC:EG10658,GeneID:946954`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2597831-2598865:-; feature_type=gene
