---
entity_id: "gene.b3270"
entity_type: "gene"
name: "yhdY"
source_database: "NCBI RefSeq"
source_id: "gene-b3270"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3270"
  - "yhdY"
---

# yhdY

`gene.b3270`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3270`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhdY (gene.b3270) is a gene entity. It encodes yhdY (protein.P45768). Encoded protein function: FUNCTION: Probably part of the binding-protein-dependent transport system YdhWXYZ for an amino acid; probably responsible for the translocation of the substrate across the membrane. EcoCyc product frame: YHDY-MONOMER. Genomic coordinates: 3421325-3422428. EcoCyc protein note: YhdY is one of two predicted inner membrane subunits of a putative ABC transporter . YhdY is predicted to be an inner membrane protein with 8 transmembrane domains; topology analysis suggests the C-terminus is located in the cytoplasm .

## Biological Role

Activated by glnG (protein.P0AFB8).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45768|protein.P45768]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=yhdY; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010736,ECOCYC:EG12836,GeneID:947764`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3421325-3422428:+; feature_type=gene
