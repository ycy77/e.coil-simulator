---
entity_id: "gene.b0655"
entity_type: "gene"
name: "gltI"
source_database: "NCBI RefSeq"
source_id: "gene-b0655"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0655"
  - "gltI"
---

# gltI

`gene.b0655`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0655`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gltI (gene.b0655) is a gene entity. It encodes gltI (protein.P37902). Encoded protein function: FUNCTION: Part of the ABC transporter complex GltIJKL involved in glutamate and aspartate uptake. Binds to both glutamate and aspartate. {ECO:0000269|PubMed:1091635, ECO:0000269|PubMed:1091636, ECO:0000269|PubMed:336628, ECO:0000305|PubMed:9593292}. EcoCyc product frame: G6359-MONOMER. EcoCyc synonyms: yzzK, ybeJ. Genomic coordinates: 686839-687747. EcoCyc protein note: GltI is the periplasmic binding protein of a glutamate/aspartate ABC transport system. Purified GltI (released from E. coli K-12 strains by osmotic shock treatment) binds L-glutamate and L-aspartate with µM affinity; binding is competitively inhibited by L-glutamine and L-asparagine . The amount of GltI is significantly reduced when E. coli W strain D2W is grown with glucose rather than succinate [Willis75]. Synthesis of GltI is repressed when the small regulatory RNA, GCVB-RNA "GcvB" is expressed from a plasmid in a ΔgcvA ΔgcvB background .

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37902|protein.P37902]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002241,ECOCYC:G6359,GeneID:946938`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:686839-687747:-; feature_type=gene
