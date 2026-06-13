---
entity_id: "gene.b2595"
entity_type: "gene"
name: "bamD"
source_database: "NCBI RefSeq"
source_id: "gene-b2595"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2595"
  - "bamD"
---

# bamD

`gene.b2595`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2595`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bamD (gene.b2595) is a gene entity. It encodes bamD (protein.P0AC02). Encoded protein function: FUNCTION: Part of the outer membrane protein assembly complex (Bam), which is involved in assembly and insertion of beta-barrel proteins into the outer membrane. Constitutes, with BamA, the core component of the assembly machinery. Probably involved in transient protein interactions. Efficient substrate folding and insertion into the outer membrane requires all 5 subunits (PubMed:20378773, PubMed:21823654, PubMed:27686148). A lateral gate may open between the first and last strands of the BamA beta-barrel that allows substrate to insert into the outer membrane; comparison of the structures of complete and nearly complete Bam complexes show there is considerable movement of all 5 proteins (PubMed:26744406, PubMed:26900875, PubMed:26901871, PubMed:27686148). {ECO:0000269|PubMed:16824102, ECO:0000269|PubMed:20378773, ECO:0000269|PubMed:21586578, ECO:0000269|PubMed:21823654, ECO:0000269|PubMed:22281737, ECO:0000269|PubMed:26744406, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871, ECO:0000269|PubMed:27686148}. EcoCyc product frame: G7352-MONOMER. EcoCyc synonyms: ecfD, yfiO. Genomic coordinates: 2736146-2736883. EcoCyc protein note: The BamD lipoprotein is part of the large multi-protein BAM complex responsible for the assembly and insertion of outer membrane β-barrel proteins...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC02|protein.P0AC02]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=bamD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008536,ECOCYC:G7352,GeneID:947086`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2736146-2736883:+; feature_type=gene
