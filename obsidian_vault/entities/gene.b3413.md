---
entity_id: "gene.b3413"
entity_type: "gene"
name: "yhgH"
source_database: "NCBI RefSeq"
source_id: "gene-b3413"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3413"
  - "yhgH"
---

# yhgH

`gene.b3413`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3413`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhgH (gene.b3413) is a gene entity. It encodes gntX (protein.P46846). Encoded protein function: FUNCTION: Required for the use of extracellular DNA as a nutrient (PubMed:16707682). Has been suggested to be involved in gluconate metabolism (PubMed:9871335). {ECO:0000269|PubMed:16707682, ECO:0000305|PubMed:9871335}. EcoCyc product frame: G7747-MONOMER. EcoCyc synonyms: gntX. Genomic coordinates: 3544882-3545565. EcoCyc protein note: The yhgH gene product is required for utilization of DNA as the sole source of carbon and energy; yhgH is homologous to genes involved in natural competence and genetic transformation in other bacteria . Based on complementation experiments, YhgH/GntX is also thought to be involved in high-affinity gluconate transport . A yhgH null mutant has a normal growth phenotype in complex media, but has a stationary phase competition-defective (SPCD) phenotype in co-culture with the wild-type strain. A yhgI null mutant can not utilize DNA as the sole source of carbon and energy .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46846|protein.P46846]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011139,ECOCYC:G7747,GeneID:947915`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3544882-3545565:+; feature_type=gene
