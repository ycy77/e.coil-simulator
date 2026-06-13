---
entity_id: "gene.b1801"
entity_type: "gene"
name: "yeaV"
source_database: "NCBI RefSeq"
source_id: "gene-b1801"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1801"
  - "yeaV"
---

# yeaV

`gene.b1801`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1801`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeaV (gene.b1801) is a gene entity. It encodes yeaV (protein.P0ABD1). Encoded protein function: FUNCTION: Probable transporter whose substrate is unknown. Is not involved in aerobic D-malate transport. EcoCyc product frame: YEAV-MONOMER. Genomic coordinates: 1883188-1884633. EcoCyc protein note: YeaV is an uncharacterized putative transport protein. The identical protein, YeaV from Escherichia coli O157:H7 is an uncharacterised member of the Betaine/Carnitine/Choline Transporter (BCCT) family . YeaV may import a broad range of substrates; candidates identified using an untargeted metabolomics approach include CPD-511, KYNURENATE, CARBAMYUL-L-ASPARTATE ureidosuccinate, L-ASPARTATE aspartate, CPD-183 and others A yeaV mutation does not affect aerobic growth on D-malate as the sole source of carbon .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABD1|protein.P0ABD1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005995,ECOCYC:G6987,GeneID:947326`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1883188-1884633:+; feature_type=gene
