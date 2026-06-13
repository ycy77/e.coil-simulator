---
entity_id: "gene.b4372"
entity_type: "gene"
name: "holD"
source_database: "NCBI RefSeq"
source_id: "gene-b4372"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4372"
  - "holD"
---

# holD

`gene.b4372`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4372`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

holD (gene.b4372) is a gene entity. It encodes holD (protein.P28632). Encoded protein function: FUNCTION: Part of the beta sliding clamp loading complex, which hydrolyzes ATP to load the beta clamp onto primed DNA to form the DNA replication pre-initiation complex (PubMed:2040637). DNA polymerase III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria. This DNA polymerase also exhibits 3' to 5' exonuclease activity. {ECO:0000269|PubMed:2040637}. EcoCyc product frame: EG11414-MONOMER. Genomic coordinates: 4607803-4608216.

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28632|protein.P28632]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0014340,ECOCYC:EG11414,GeneID:948890`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4607803-4608216:+; feature_type=gene
