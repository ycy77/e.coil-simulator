---
entity_id: "complex.ecocyc.CPLX0-243"
entity_type: "complex"
name: "inorganic pyrophosphatase"
source_database: "EcoCyc"
source_id: "CPLX0-243"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-CYTOSOL-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# inorganic pyrophosphatase

`complex.ecocyc.CPLX0-243`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-243`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-CYTOSOL-GN
- Complex type: `structural`
- Components: [[protein.P0A7A9|protein.P0A7A9]]

## Enriched Summary

Inorganic pyrophosphatase (PPase) specifically catalyzes the hydrolysis of inorganic pyrophosphate to two orthophosphates. This reaction plays an important role in energy metabolism, providing a thermodynamic pull for biosynthetic reactions such as protein, RNA and DNA synthesis . Proteins interacting with PPase have been identified . Crystal structures of PPase have been solved . The enzyme is a hexamer, arranged as a dimer of trimers in the crystal structure . Amino acid residues that are required for structural integrity, substrate and effector binding, or catalytic activity have been identified by site-directed mutagenesis and analysis of the wild-type and mutant enzymes . Steady-state rates of PPase enzymatic activity with respect to pH and Mg2+ concentration have been measured exhaustively . The reaction mechanism has been analyzed using density functional theory . The intracellular concentration of pyrophosphate did not appear to depend on the activity of PPase . In contrast, it was shown that pyrophosphate levels increased after depletion of PPase . ppa is essential for growth in E. coli . Review: Inorganic pyrophosphatase (PPase) specifically catalyzes the hydrolysis of inorganic pyrophosphate to two orthophosphates...

## Biological Role

Catalyzes INORGPYROPHOSPHAT-RXN (reaction.ecocyc.INORGPYROPHOSPHAT-RXN), TRIPHOSPHATASE-RXN (reaction.ecocyc.TRIPHOSPHATASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Inorganic pyrophosphatase (PPase) specifically catalyzes the hydrolysis of inorganic pyrophosphate to two orthophosphates. This reaction plays an important role in energy metabolism, providing a thermodynamic pull for biosynthetic reactions such as protein, RNA and DNA synthesis . Proteins interacting with PPase have been identified . Crystal structures of PPase have been solved . The enzyme is a hexamer, arranged as a dimer of trimers in the crystal structure . Amino acid residues that are required for structural integrity, substrate and effector binding, or catalytic activity have been identified by site-directed mutagenesis and analysis of the wild-type and mutant enzymes . Steady-state rates of PPase enzymatic activity with respect to pH and Mg2+ concentration have been measured exhaustively . The reaction mechanism has been analyzed using density functional theory . The intracellular concentration of pyrophosphate did not appear to depend on the activity of PPase . In contrast, it was shown that pyrophosphate levels increased after depletion of PPase . ppa is essential for growth in E. coli . Review:

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.INORGPYROPHOSPHAT-RXN|reaction.ecocyc.INORGPYROPHOSPHAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRIPHOSPHATASE-RXN|reaction.ecocyc.TRIPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A7A9|protein.P0A7A9]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-243`
- `QSPROTEOME:QS00182055`

## Notes

6*protein.P0A7A9
