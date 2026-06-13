---
entity_id: "gene.b2361"
entity_type: "gene"
name: "yfdR"
source_database: "NCBI RefSeq"
source_id: "gene-b2361"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2361"
  - "yfdR"
---

# yfdR

`gene.b2361`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2361`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfdR (gene.b2361) is a gene entity. It encodes yfdR (protein.P76514). Encoded protein function: Uncharacterized protein YfdR EcoCyc product frame: G7230-MONOMER. Genomic coordinates: 2474984-2475520. EcoCyc protein note: YfdR is a deoxyribonucleoside 5'-monophosphate phosphatase with a conserved HD domain. The enzyme has a broader substrate range than YfbR . YfdR was found to interact with DnaA . The genomic region comprising yfdQRST was found to act as a multicopy suppressor of the hda-185 ΔsfiA mutation. A ΔyfdQRST deletion mutant has no obvious growth defect .

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76514|protein.P76514]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007791,ECOCYC:G7230,GeneID:946834`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2474984-2475520:+; feature_type=gene
