---
entity_id: "protein.P0A6L2"
entity_type: "protein"
name: "dapA"
source_database: "UniProt"
source_id: "P0A6L2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dapA b2478 JW2463"
---

# dapA

`protein.P0A6L2`

## Static

- Type: `protein`
- Source: `UniProt:P0A6L2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the condensation of (S)-aspartate-beta-semialdehyde [(S)-ASA] and pyruvate to 4-hydroxy-tetrahydrodipicolinate (HTPA). {ECO:0000255|HAMAP-Rule:MF_00418, ECO:0000269|PubMed:20503968, ECO:0000269|PubMed:8993314}. 4-hydroxy-tetrahydrodipicolinate synthase, historically called dihydrodipicolinate synthase (DHDPS, DapA) is the first enzyme unique to lysine biosynthesis, catalyzing the condensation of pyruvate and (S)-aspartate β-semialdehyde. This is thought to be the rate-limiting step in lysine biosynthesis after aspartate kinase III . The product of the reaction catalyzed by DapA was identified as (4S)-4-hydroxy-2,3,4,5-tetrahydro-(2S)-dipicolinate (HTPA) . The reaction proceeds via a ping-pong bi-bi mechanism; pyruvate initially binds to the enzyme via a Schiff base to the ε-amino group of the active site Lys161 residue . This is followed by addition of L-aspartate semialdehyde and transimination leading to cyclization and dissociation of HTPA . The kinetic mechanism was refined using initial velocity and dead-end inhibition studies at both high and low pH, confirming the ping-pong reaction mechanism of the enzyme . Surprisingly, Lys161 is not absolutely essential for catalysis . Crystal structures of the apo-enzyme and in complexes with substrates, substrate analogs and inhibitors, as well as of mutant enzymes have been solved...

## Biological Role

Component of 4-hydroxy-tetrahydrodipicolinate synthase (complex.ecocyc.DIHYDRODIPICSYN-CPLX).

## Enriched Pathways

- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the condensation of (S)-aspartate-beta-semialdehyde [(S)-ASA] and pyruvate to 4-hydroxy-tetrahydrodipicolinate (HTPA). {ECO:0000255|HAMAP-Rule:MF_00418, ECO:0000269|PubMed:20503968, ECO:0000269|PubMed:8993314}.

## Pathways

- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.DIHYDRODIPICSYN-CPLX|complex.ecocyc.DIHYDRODIPICSYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2478|gene.b2478]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6L2`
- `KEGG:ecj:JW2463;eco:b2478;ecoc:C3026_13755;`
- `GeneID:946952;`
- `GO:GO:0005829; GO:0008840; GO:0009089; GO:0019877; GO:0042802`
- `EC:4.3.3.7`

## Notes

4-hydroxy-tetrahydrodipicolinate synthase (HTPA synthase) (EC 4.3.3.7)
