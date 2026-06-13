---
entity_id: "gene.b1886"
entity_type: "gene"
name: "tar"
source_database: "NCBI RefSeq"
source_id: "gene-b1886"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1886"
  - "tar"
---

# tar

`gene.b1886`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1886`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tar (gene.b1886) is a gene entity. It encodes tar (protein.P07017). Encoded protein function: FUNCTION: Receptor for the attractant L-aspartate and related amino and dicarboxylic acids. Tar also mediates taxis to the attractant maltose via an interaction with the periplasmic maltose binding protein. Tar mediates taxis away from the repellents cobalt and nickel.; FUNCTION: Chemotactic-signal transducers respond to changes in the concentration of attractants and repellents in the environment, transduce a signal from the outside to the inside of the cell, and facilitate sensory adaptation through the variation of the level of methylation. Attractants increase the level of methylation while repellents decrease the level of methylation, the methyl groups are added by the methyltransferase CheR and removed by the methylesterase CheB. EcoCyc product frame: TAR-MONOMER. EcoCyc synonyms: cheM. Genomic coordinates: 1971030-1972691.

## Biological Role

Repressed by glaR (protein.P37338). Activated by fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07017|protein.P07017]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=tar; function=+
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=tar; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006290,ECOCYC:EG10988,GeneID:946399`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1971030-1972691:-; feature_type=gene
