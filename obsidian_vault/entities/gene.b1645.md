---
entity_id: "gene.b1645"
entity_type: "gene"
name: "ydhK"
source_database: "NCBI RefSeq"
source_id: "gene-b1645"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1645"
  - "ydhK"
---

# ydhK

`gene.b1645`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1645`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydhK (gene.b1645) is a gene entity. It encodes ydhK (protein.P76186). Encoded protein function: Uncharacterized transporter YdhK EcoCyc product frame: G6885-MONOMER. Genomic coordinates: 1722121-1724133. EcoCyc protein note: In the Transporter Classification Database, YdhK (from E. coli O157:H7) is an uncharacterized member of the Aromatic Acid Exporter (ArAE) family . A variety of potential substrates were identified using an untargeted metabolomics approach .

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76186|protein.P76186]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=ydhK; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005503,ECOCYC:G6885,GeneID:946528`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1722121-1724133:+; feature_type=gene
