---
entity_id: "gene.b1118"
entity_type: "gene"
name: "lolE"
source_database: "NCBI RefSeq"
source_id: "gene-b1118"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1118"
  - "lolE"
---

# lolE

`gene.b1118`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1118`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lolE (gene.b1118) is a gene entity. It encodes lolE (protein.P75958). Encoded protein function: FUNCTION: Part of an ATP-dependent transport system LolCDE responsible for the release of lipoproteins targeted to the outer membrane from the inner membrane. Such a release is dependent of the sorting-signal (absence of an Asp at position 2 of the mature lipoprotein) and of LolA. EcoCyc product frame: YCFW-MONOMER. EcoCyc synonyms: ycfW. Genomic coordinates: 1177320-1178564. EcoCyc protein note: LolE is an inner membrane subunit of the LolCDE lipoprotein release complex . LolE contains 4 predicted transmembrane regions; a large loop region between the first and second transmembrane regions is predicted to be in the periplasm .

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75958|protein.P75958]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003776,ECOCYC:G6575,GeneID:945665`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1177320-1178564:+; feature_type=gene
