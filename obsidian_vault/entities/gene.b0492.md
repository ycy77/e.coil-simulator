---
entity_id: "gene.b0492"
entity_type: "gene"
name: "cnoX"
source_database: "NCBI RefSeq"
source_id: "gene-b0492"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0492"
  - "cnoX"
---

# cnoX

`gene.b0492`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0492`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cnoX (gene.b0492) is a gene entity. It encodes cnoX (protein.P77395). Encoded protein function: FUNCTION: Chaperedoxin that combines a chaperone activity with a redox-protective function (PubMed:16563353, PubMed:18657513, PubMed:29754824). Involved in the protection against hypochlorous acid (HOCl), the active ingredient of bleach, which kills bacteria by causing protein aggregation (PubMed:29754824). Functions as an efficient holdase chaperone that protects the substrates of the major folding systems GroEL/GroES and DnaK/DnaJ/GrpE from aggregation. In addition, it prevents the irreversible oxidation of its substrates through the formation of mixed disulfide complexes (PubMed:29754824). After bleach stress, it transfers its substrates to the GroEL/GroES and DnaK/DnaJ/GrpE foldases (PubMed:29754824). Lacks oxidoreductase activity (PubMed:21498507, PubMed:29754824). {ECO:0000269|PubMed:16563353, ECO:0000269|PubMed:18657513, ECO:0000269|PubMed:21498507, ECO:0000269|PubMed:29754824}. EcoCyc product frame: G6268-MONOMER. EcoCyc synonyms: ybbN. Genomic coordinates: 517425-518279. EcoCyc protein note: CnoX (formerly YbbN) is a chaperedoxin - a protein which functions as a holdase and also provides redox protection to its substrates through the formation of mixed disulfide complexes...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77395|protein.P77395]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001707,ECOCYC:G6268,GeneID:947119`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:517425-518279:-; feature_type=gene
