---
entity_id: "gene.b3900"
entity_type: "gene"
name: "frvA"
source_database: "NCBI RefSeq"
source_id: "gene-b3900"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3900"
  - "frvA"
---

# frvA

`gene.b3900`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3900`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

frvA (gene.b3900) is a gene entity. It encodes frvA (protein.P32155). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II FrvAB PTS system is involved in fructose transport. {ECO:0000305|PubMed:8019415}. EcoCyc product frame: FRVA-MONOMER. EcoCyc synonyms: yiiK. Genomic coordinates: 4092377-4092823. EcoCyc protein note: frvA is predicted to encode a hydrophilic protein with similarity to the IIA domain of the PTS Enzyme IIs specific for mannitol and fructose. FrvA contains a conserved histidine (His64) .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32155|protein.P32155]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012727,ECOCYC:EG11864,GeneID:948391`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4092377-4092823:-; feature_type=gene
