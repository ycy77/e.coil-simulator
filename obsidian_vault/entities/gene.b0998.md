---
entity_id: "gene.b0998"
entity_type: "gene"
name: "torD"
source_database: "NCBI RefSeq"
source_id: "gene-b0998"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0998"
  - "torD"
---

# torD

`gene.b0998`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0998`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

torD (gene.b0998) is a gene entity. It encodes torD (protein.P36662). Encoded protein function: FUNCTION: Involved in the biogenesis of TorA. Acts on TorA before the insertion of the molybdenum cofactor and, as a result, probably favors a conformation of the apoenzyme that is competent for acquiring the cofactor. {ECO:0000269|PubMed:12766163, ECO:0000269|PubMed:9632735}. EcoCyc product frame: EG12195-MONOMER. Genomic coordinates: 1061799-1062398. EcoCyc protein note: TorD is the TORA-MONOMER TorA-specific redox enzyme maturation protein (REMP). TorD is encoded by the terminal open reading frame of the torCAD operon, which is involved in anaerobic respiration of trimethylamine N-oxide (TMAO) . TorD belongs to a family of structurally related bacterial proteins which appear to have coevolved with their specific molybdoprotein partners . TorD interacts directly with the TorA protein, the TMAO reductase, before TorA acquires its molybdenum cofactor . TorD acts as a private chaperone for TorA, making it competent to receive the molybdenum cofactor; TorD was shown to be sufficient for activation of TorA . TorD specifically recognizes the twin-arginine signal peptide of TorA, performing a Tat proofreading function .

## Biological Role

Activated by torR (protein.P38684).

## Enriched Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36662|protein.P36662]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P38684|protein.P38684]] `RegulonDB` `S` - regulator=TorR; target=torD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003374,ECOCYC:EG12195,GeneID:945625`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1061799-1062398:+; feature_type=gene
