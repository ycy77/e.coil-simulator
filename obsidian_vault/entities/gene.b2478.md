---
entity_id: "gene.b2478"
entity_type: "gene"
name: "dapA"
source_database: "NCBI RefSeq"
source_id: "gene-b2478"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2478"
  - "dapA"
---

# dapA

`gene.b2478`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2478`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dapA (gene.b2478) is a gene entity. It encodes dapA (protein.P0A6L2). Encoded protein function: FUNCTION: Catalyzes the condensation of (S)-aspartate-beta-semialdehyde [(S)-ASA] and pyruvate to 4-hydroxy-tetrahydrodipicolinate (HTPA). {ECO:0000255|HAMAP-Rule:MF_00418, ECO:0000269|PubMed:20503968, ECO:0000269|PubMed:8993314}. EcoCyc product frame: DIHYDRODIPICSYN-MONOMER. Genomic coordinates: 2598882-2599760. EcoCyc protein note: 4-hydroxy-tetrahydrodipicolinate synthase, historically called dihydrodipicolinate synthase (DHDPS, DapA) is the first enzyme unique to lysine biosynthesis, catalyzing the condensation of pyruvate and (S)-aspartate β-semialdehyde. This is thought to be the rate-limiting step in lysine biosynthesis after aspartate kinase III . The product of the reaction catalyzed by DapA was identified as (4S)-4-hydroxy-2,3,4,5-tetrahydro-(2S)-dipicolinate (HTPA) . The reaction proceeds via a ping-pong bi-bi mechanism; pyruvate initially binds to the enzyme via a Schiff base to the ε-amino group of the active site Lys161 residue . This is followed by addition of L-aspartate semialdehyde and transimination leading to cyclization and dissociation of HTPA . The kinetic mechanism was refined using initial velocity and dead-end inhibition studies at both high and low pH, confirming the ping-pong reaction mechanism of the enzyme...

## Enriched Pathways

- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6L2|protein.P0A6L2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008163,ECOCYC:EG10205,GeneID:946952`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2598882-2599760:-; feature_type=gene
