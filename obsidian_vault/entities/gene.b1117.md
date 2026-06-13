---
entity_id: "gene.b1117"
entity_type: "gene"
name: "lolD"
source_database: "NCBI RefSeq"
source_id: "gene-b1117"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1117"
  - "lolD"
---

# lolD

`gene.b1117`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1117`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lolD (gene.b1117) is a gene entity. It encodes lolD (protein.P75957). Encoded protein function: FUNCTION: Part of the ABC transporter complex LolCDE involved in the translocation of mature outer membrane-directed lipoproteins, from the inner membrane to the periplasmic chaperone, LolA. Responsible for the formation of the LolA-lipoprotein complex in an ATP-dependent manner. Such a release is dependent of the sorting-signal (absence of an Asp at position 2 of the mature lipoprotein) and of LolA. EcoCyc product frame: YCFV-MONOMER. EcoCyc synonyms: ycfV. Genomic coordinates: 1176619-1177320. EcoCyc protein note: LolD is the ATP-binding component of the LolCDE lipoprotein release complex. LolD contains signature motifs conserved in ATP-binding cassette domains .

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75957|protein.P75957]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003774,ECOCYC:G6574,GeneID:945670`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1176619-1177320:+; feature_type=gene
