---
entity_id: "gene.b1549"
entity_type: "gene"
name: "ydfO"
source_database: "NCBI RefSeq"
source_id: "gene-b1549"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1549"
  - "ydfO"
---

# ydfO

`gene.b1549`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1549`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydfO (gene.b1549) is a gene entity. It encodes ydfO (protein.P76156). Encoded protein function: Uncharacterized protein YdfO EcoCyc product frame: G6822-MONOMER. Genomic coordinates: 1637047-1637457. EcoCyc protein note: No information about this protein was found by a literature search conducted on September 20, 2018.

## Biological Role

Activated by DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76156|protein.P76156]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=ydfO; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005175,ECOCYC:G6822,GeneID:945992`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1637047-1637457:+; feature_type=gene
