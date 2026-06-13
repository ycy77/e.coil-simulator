---
entity_id: "gene.b0856"
entity_type: "gene"
name: "potH"
source_database: "NCBI RefSeq"
source_id: "gene-b0856"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0856"
  - "potH"
---

# potH

`gene.b0856`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0856`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

potH (gene.b0856) is a gene entity. It encodes potH (protein.P31135). Encoded protein function: FUNCTION: Part of the ABC transporter complex PotFGHI involved in putrescine uptake (PubMed:23719730, PubMed:8416922). Responsible for the translocation of the substrate across the membrane (Probable). Imports putrescine for maintenance of the optimal concentration of polyamines necessary for cell growth in the presence of glucose (PubMed:23719730). {ECO:0000269|PubMed:23719730, ECO:0000269|PubMed:8416922, ECO:0000305}. EcoCyc product frame: POTH-MONOMER. Genomic coordinates: 896134-897087. EcoCyc protein note: potH encodes one of two integral membrane subunits of an ATP-dependent putrescine uptake system; PotH is predicted to contain 6 transmembrane regions; PotH has 37% sequence similarity with PotB - the integral membrane subunit of the spermidine ABC transporter PotABCD .

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31135|protein.P31135]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002917,ECOCYC:EG11631,GeneID:945475`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:896134-897087:+; feature_type=gene
