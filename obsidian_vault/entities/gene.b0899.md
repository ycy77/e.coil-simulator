---
entity_id: "gene.b0899"
entity_type: "gene"
name: "ycaM"
source_database: "NCBI RefSeq"
source_id: "gene-b0899"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0899"
  - "ycaM"
---

# ycaM

`gene.b0899`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0899`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycaM (gene.b0899) is a gene entity. It encodes ycaM (protein.P75835). Encoded protein function: Inner membrane transporter YcaM EcoCyc product frame: YCAM. Genomic coordinates: 947229-948659. EcoCyc protein note: Random transposon mutagenesis indicates that ycaM is required for growth in optimum conditions (rich medium at 37°C) but not in minimal medium or at low temperature (15°C) . YcaM is a member of the Glutamate:GABA Antiporter (GGA) Family within the Amino Acid-Polyamine-Organocation (APC) Superfamily; YcaM is a XASA-MONOMER "GadC" homolog .

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75835|protein.P75835]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=ycaM; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003058,ECOCYC:G6466,GeneID:945518`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:947229-948659:+; feature_type=gene
