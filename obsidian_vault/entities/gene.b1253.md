---
entity_id: "gene.b1253"
entity_type: "gene"
name: "yciA"
source_database: "NCBI RefSeq"
source_id: "gene-b1253"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1253"
  - "yciA"
---

# yciA

`gene.b1253`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1253`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yciA (gene.b1253) is a gene entity. It encodes yciA (protein.P0A8Z0). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of the thioester bond in palmitoyl-CoA and malonyl-CoA. {ECO:0000269|PubMed:15808744}. EcoCyc product frame: EG11121-MONOMER. Genomic coordinates: 1311848-1312246. EcoCyc protein note: YciA is an acyl-CoA thioesterase with broad substrate specificity . Esterase activity of YciA was first discovered in a high-throughput screen of purified proteins . YciA homologs exist in a wide variety of bacteria. The Haemophilus influenzae enzyme is a homohexamer and has been crystallized . A yciA null mutant does not have an obvious growth defect . A yciA deletion mutant in the EB228 strain background produces significantly less butyrate than its parent .

## Enriched Pathways

- `eco01040` Biosynthesis of unsaturated fatty acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8Z0|protein.P0A8Z0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004198,ECOCYC:EG11121,GeneID:946634`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1311848-1312246:-; feature_type=gene
