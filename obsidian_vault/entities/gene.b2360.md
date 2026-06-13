---
entity_id: "gene.b2360"
entity_type: "gene"
name: "yfdQ"
source_database: "NCBI RefSeq"
source_id: "gene-b2360"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2360"
  - "yfdQ"
---

# yfdQ

`gene.b2360`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2360`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfdQ (gene.b2360) is a gene entity. It encodes yfdQ (protein.P76513). Encoded protein function: Uncharacterized protein YfdQ EcoCyc product frame: G7229-MONOMER. Genomic coordinates: 2474032-2474856. EcoCyc protein note: The genomic region comprising yfdQRST was found to act as a multicopy suppressor of the hda-185 ΔsfiA mutation. A ΔyfdQRST deletion mutant has no obvious growth defect . The T1-type lytic phage SW1 utilizes the YfdQ protein of the cryptic prophage CPS-53 to replicate .

## Biological Role

Activated by ygfI (protein.P52044).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76513|protein.P76513]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=yfdQ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007788,ECOCYC:G7229,GeneID:946827`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2474032-2474856:+; feature_type=gene
