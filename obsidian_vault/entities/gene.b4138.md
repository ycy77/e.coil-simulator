---
entity_id: "gene.b4138"
entity_type: "gene"
name: "dcuA"
source_database: "NCBI RefSeq"
source_id: "gene-b4138"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4138"
  - "dcuA"
---

# dcuA

`gene.b4138`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4138`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dcuA (gene.b4138) is a gene entity. It encodes dcuA (protein.P0ABN5). Encoded protein function: FUNCTION: Responsible for the transport of C4-dicarboxylates during aerobic and anaerobic growth (PubMed:29995997, PubMed:7961398, PubMed:8131924, PubMed:8955408). Required for the uptake of L-aspartate as a nitrogen source during aerobic growth (PubMed:29995997). The uptake of L-aspartate in aerobic conditions is coupled to the excretion of fumarate, resulting in the net uptake of nitrogen without carbon uptake (PubMed:29995997). In addition, during anaerobic growth, catalyzes the uptake of fumarate, malate or aspartate coupled to the export of succinate (PubMed:7961398, PubMed:8955408). Can also catalyze the uptake (without exchange) of fumarate (PubMed:8955408). May play a a general role in anaerobic C4-dicarboxylate transport (PubMed:9852003). {ECO:0000269|PubMed:29995997, ECO:0000269|PubMed:7961398, ECO:0000269|PubMed:8131924, ECO:0000269|PubMed:8955408, ECO:0000269|PubMed:9852003}. EcoCyc product frame: DCUA-MONOMER. EcoCyc synonyms: genA. Genomic coordinates: 4365472-4366773...

## Biological Role

Repressed by narL (protein.P0AF28). Activated by fnr (protein.P0A9E5), arcA (protein.P0A9Q1).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABN5|protein.P0ABN5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=dcuA; function=+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=dcuA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=dcuA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013546,ECOCYC:EG11225,GeneID:948659`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4365472-4366773:-; feature_type=gene
