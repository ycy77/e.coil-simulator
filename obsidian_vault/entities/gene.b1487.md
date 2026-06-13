---
entity_id: "gene.b1487"
entity_type: "gene"
name: "ddpA"
source_database: "NCBI RefSeq"
source_id: "gene-b1487"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1487"
  - "ddpA"
---

# ddpA

`gene.b1487`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1487`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ddpA (gene.b1487) is a gene entity. It encodes ddpA (protein.P76128). Encoded protein function: FUNCTION: Part of the ABC transporter complex DdpABCDF, which is probably involved in D,D-dipeptide transport. EcoCyc product frame: YDDS-MONOMER. EcoCyc synonyms: yddS. Genomic coordinates: 1560931-1562481. EcoCyc protein note: DdpA is the predicted periplasmic binding protein of a putative ATP-dependent D,D-dipeptide uptake system that may function to import D-alanyl-D-alanine for use as an energy source under starvation conditions . ArcA appears to activate ddpA gene expression under anaerobiosis. A putative ArcA binding site was identified 103 bp upstream of this gene ; but no promoter upstream of it has been identified. Instead, ddpA is transcribed from a promoter that is located usptream of ddpX gene. ddp: D,D-dipeptide

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76128|protein.P76128]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004958,ECOCYC:G6781,GeneID:946052`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1560931-1562481:-; feature_type=gene
