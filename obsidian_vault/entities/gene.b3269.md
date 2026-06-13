---
entity_id: "gene.b3269"
entity_type: "gene"
name: "yhdX"
source_database: "NCBI RefSeq"
source_id: "gene-b3269"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3269"
  - "yhdX"
---

# yhdX

`gene.b3269`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3269`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhdX (gene.b3269) is a gene entity. It encodes yhdX (protein.P45767). Encoded protein function: FUNCTION: Probably part of the binding-protein-dependent transport system YdhWXYZ for an amino acid; probably responsible for the translocation of the substrate across the membrane. EcoCyc product frame: YHDX-MONOMER. Genomic coordinates: 3420134-3421315. EcoCyc protein note: YhdX is one of two predicted inner membrane subunits of a putative ABC transporter .

## Biological Role

Activated by glnG (protein.P0AFB8).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45767|protein.P45767]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=yhdX; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010733,ECOCYC:EG12835,GeneID:947765`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3420134-3421315:+; feature_type=gene
