---
entity_id: "complex.ecocyc.CPLX0-7744"
entity_type: "complex"
name: "3-keto-L-gulonate-6-phosphate decarboxylase UlaD"
source_database: "EcoCyc"
source_id: "CPLX0-7744"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 3-keto-L-gulonate-6-phosphate decarboxylase UlaD

`complex.ecocyc.CPLX0-7744`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7744`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P39304|protein.P39304]]

## Enriched Summary

3-keto-L-gulonate 6-phosphate decarboxylase is an enzyme in the pathway of anaerobic L-ascorbate degradation. Crystal structures of the UlaD protein , UlaD complexed with substrate, reaction intermediate and product analogs , and several mutants have been determined. The enzyme is as a dimer of antiparallel (β/α)8 barrels in the crystal structure . Active site residues and catalytic mechanisms involving a Mg2+ ion-stabilized cis-1,2-enediolate intermediate have been studied . Kinetic properties of active site mutants have been analyzed . Certain changes to active site residues can enhance the D-arabino-hex-3-ulose 6-phosphate synthase (HPS) activity of the enzyme . The structural basis of the effect on the catalytic properties of the enzyme has been explored . UlaD: "utilization of L-ascorbate" 3-keto-L-gulonate 6-phosphate decarboxylase is an enzyme in the pathway of anaerobic L-ascorbate degradation. Crystal structures of the UlaD protein , UlaD complexed with substrate, reaction intermediate and product analogs , and several mutants have been determined. The enzyme is as a dimer of antiparallel (β/α)8 barrels in the crystal structure . Active site residues and catalytic mechanisms involving a Mg2+ ion-stabilized cis-1,2-enediolate intermediate have been studied . Kinetic properties of active site mutants have been analyzed...

## Biological Role

Catalyzes RXN0-705 (reaction.ecocyc.RXN0-705). Bound by Magnesium cation (molecule.C00305).

## Annotation

3-keto-L-gulonate 6-phosphate decarboxylase is an enzyme in the pathway of anaerobic L-ascorbate degradation. Crystal structures of the UlaD protein , UlaD complexed with substrate, reaction intermediate and product analogs , and several mutants have been determined. The enzyme is as a dimer of antiparallel (β/α)8 barrels in the crystal structure . Active site residues and catalytic mechanisms involving a Mg2+ ion-stabilized cis-1,2-enediolate intermediate have been studied . Kinetic properties of active site mutants have been analyzed . Certain changes to active site residues can enhance the D-arabino-hex-3-ulose 6-phosphate synthase (HPS) activity of the enzyme . The structural basis of the effect on the catalytic properties of the enzyme has been explored . UlaD: "utilization of L-ascorbate"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-705|reaction.ecocyc.RXN0-705]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P39304|protein.P39304]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7744`
- `QSPROTEOME:QS00181793`

## Notes

2*protein.P39304
