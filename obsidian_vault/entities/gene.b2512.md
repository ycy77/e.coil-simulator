---
entity_id: "gene.b2512"
entity_type: "gene"
name: "bamB"
source_database: "NCBI RefSeq"
source_id: "gene-b2512"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2512"
  - "bamB"
---

# bamB

`gene.b2512`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2512`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bamB (gene.b2512) is a gene entity. It encodes bamB (protein.P77774). Encoded protein function: FUNCTION: Part of the outer membrane protein assembly complex (Bam), which is involved in assembly and insertion of beta-barrel proteins into the outer membrane. Nonessential member of the complex, which may orient the flexible periplasmic domain of BamA for interaction with other Bam components, chaperones and nascent outer membrane proteins. Efficient substrate folding and insertion into the outer membrane requires all 5 subunits (PubMed:20378773, PubMed:21823654, PubMed:27686148). A lateral gate may open between the first and last strands of the BamA beta-barrel that allows substrate to insert into the outer membrane; comparison of the structures of complete and nearly complete Bam complexes show there is considerable movement of all 5 proteins (PubMed:26900875, PubMed:26901871, PubMed:27686148). {ECO:0000269|PubMed:20378773, ECO:0000269|PubMed:21277859, ECO:0000269|PubMed:21586578, ECO:0000269|PubMed:21823654, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871, ECO:0000269|PubMed:27686148}. EcoCyc product frame: G7320-MONOMER. EcoCyc synonyms: yfgL. Genomic coordinates: 2637474-2638652. EcoCyc protein note: The BamB (formerly YfgL) lipoprotein is part of the large multi-protein BAM complex responsible for the assembly and insertion of outer membrane β-barrel proteins in E...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77774|protein.P77774]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=bamB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008272,ECOCYC:G7320,GeneID:946982`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2637474-2638652:-; feature_type=gene
