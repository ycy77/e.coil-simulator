---
entity_id: "gene.b4355"
entity_type: "gene"
name: "tsr"
source_database: "NCBI RefSeq"
source_id: "gene-b4355"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4355"
  - "tsr"
---

# tsr

`gene.b4355`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4355`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tsr (gene.b4355) is a gene entity. It encodes tsr (protein.P02942). Encoded protein function: FUNCTION: Receptor for the attractant L-serine and related amino acids. Is also responsible for chemotaxis away from a wide range of repellents, including leucine, indole, and weak acids.; FUNCTION: Chemotactic-signal transducers respond to changes in the concentration of attractants and repellents in the environment, transduce a signal from the outside to the inside of the cell, and facilitate sensory adaptation through the variation of the level of methylation. Attractants increase the level of methylation while repellents decrease the level of methylation, the methyl groups are added by the methyltransferase CheR and removed by the methylesterase CheB. EcoCyc product frame: TSR-MONOMER. EcoCyc synonyms: cheD. Genomic coordinates: 4591657-4593312.

## Biological Role

Repressed by cpxR (protein.P0AE88). Activated by fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P02942|protein.P02942]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=tsr; function=+
- `represses` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=tsr; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014282,ECOCYC:EG11034,GeneID:948884`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4591657-4593312:+; feature_type=gene
