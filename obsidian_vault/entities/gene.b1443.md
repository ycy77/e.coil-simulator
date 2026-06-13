---
entity_id: "gene.b1443"
entity_type: "gene"
name: "ydcV"
source_database: "NCBI RefSeq"
source_id: "gene-b1443"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1443"
  - "ydcV"
---

# ydcV

`gene.b1443`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1443`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydcV (gene.b1443) is a gene entity. It encodes ydcV (protein.P0AFR9). Encoded protein function: FUNCTION: Involved in natural transformation (PubMed:26826386). Probably part of the ABC transporter complex YdcSTUV. Probably responsible for the translocation of the substrate across the membrane. During natural transformation, may serve as the channel for dsDNA uptake (Probable). {ECO:0000269|PubMed:26826386, ECO:0000305|PubMed:26826386}. EcoCyc product frame: YDCV-MONOMER. Genomic coordinates: 1514762-1515556. EcoCyc protein note: YdcV is the predicted inner membrane component of an uncharacterized ABC transporter . YdcV is implicated in double strand (ds) DNA transport across the inner membrane during natural transformation; a ydcV deletion mutant has significantly decreased rates of natural transformation compared to wild type .

## Biological Role

Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFR9|protein.P0AFR9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ydcV; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004809,ECOCYC:G6754,GeneID:945903`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1514762-1515556:+; feature_type=gene
