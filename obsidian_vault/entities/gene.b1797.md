---
entity_id: "gene.b1797"
entity_type: "gene"
name: "yeaR"
source_database: "NCBI RefSeq"
source_id: "gene-b1797"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1797"
  - "yeaR"
---

# yeaR

`gene.b1797`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1797`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeaR (gene.b1797) is a gene entity. It encodes yeaR (protein.P64488). Encoded protein function: Uncharacterized protein YeaR EcoCyc product frame: G6983-MONOMER. Genomic coordinates: 1879589-1879948. EcoCyc protein note: Transcription of yeaR is induced in response to nitrate, nitrite , and nitric oxide . The G6983 gene was found to be commonly mutated in a laboratory evolution study aimed to increase tolerance to several industrial chemicals. The authors defined YeaR as a culturing-condition adaptation protein . A crystal structure of the protein is available in PDB.

## Biological Role

Repressed by fis (protein.P0A6R3). Activated by rpoD (protein.P00579), narL (protein.P0AF28).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64488|protein.P64488]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yeaR; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=yeaR; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=yeaR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005979,ECOCYC:G6983,GeneID:946317`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1879589-1879948:-; feature_type=gene
