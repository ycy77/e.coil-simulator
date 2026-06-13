---
entity_id: "protein.P04036"
entity_type: "protein"
name: "dapB"
source_database: "UniProt"
source_id: "P04036"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dapB b0031 JW0029"
---

# dapB

`protein.P04036`

## Static

- Type: `protein`
- Source: `UniProt:P04036`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the conversion of 4-hydroxy-tetrahydrodipicolinate (HTPA) to tetrahydrodipicolinate. Can use both NADH and NADPH as a reductant, with NADH being twice as effective as NADPH. {ECO:0000255|HAMAP-Rule:MF_00102, ECO:0000269|PubMed:20503968, ECO:0000269|PubMed:7893644}. 4-hydroxy-tetrahydrodipicolinate reductase, historically called dihydrodipicolinate reductase (DHDPR, DapB) catalyzes a step in lysine biosynthesis via diaminopimelate. The substrate for DapB is (4S)-4-hydroxy-2,3,4,5-tetrahydro-(2S)-dipicolinate (HTPA) . Given the discovery of HTPA as the true substrate of DapB , previous data on the reaction mechanism of the enzyme, e.g. in , need to be re-evaluated. Crystal structures of the enzyme have been solved . The enzyme consists of two domains; the N-terminal domain binds the dinucleotide cosubstrate, while the C-terminal domain is thought to bind dihydrodipicolinate . Conformational change upon substrate binding may be essential for catalysis ; a reaction mechansim was proposed . Interactions of DapB with a variety of nucleotide substrates were investigated by isothermal titration calorimetry and crystallography . The enzyme follows an ordered reaction mechanism, first binding NADPH . The DapB homotetramer appears to bind NADH sequentially with negative cooperativity between the subunits . Expression of dapB is repressed by lysine via ArgP...

## Biological Role

Component of 4-hydroxy-tetrahydrodipicolinate reductase (complex.ecocyc.DIHYDROPICRED-CPLX).

## Enriched Pathways

- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of 4-hydroxy-tetrahydrodipicolinate (HTPA) to tetrahydrodipicolinate. Can use both NADH and NADPH as a reductant, with NADH being twice as effective as NADPH. {ECO:0000255|HAMAP-Rule:MF_00102, ECO:0000269|PubMed:20503968, ECO:0000269|PubMed:7893644}.

## Pathways

- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.DIHYDROPICRED-CPLX|complex.ecocyc.DIHYDROPICRED-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0031|gene.b0031]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P04036`
- `KEGG:ecj:JW0029;eco:b0031;ecoc:C3026_00150;`
- `GeneID:944762;`
- `GO:GO:0005829; GO:0008652; GO:0008839; GO:0009089; GO:0016726; GO:0019877; GO:0042802; GO:0050661; GO:0051287`
- `EC:1.17.1.8`

## Notes

4-hydroxy-tetrahydrodipicolinate reductase (HTPA reductase) (EC 1.17.1.8)
