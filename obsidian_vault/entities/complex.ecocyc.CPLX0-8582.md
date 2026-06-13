---
entity_id: "complex.ecocyc.CPLX0-8582"
entity_type: "complex"
name: "UDP-galactopyranose mutase"
source_database: "EcoCyc"
source_id: "CPLX0-8582"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# UDP-galactopyranose mutase

`complex.ecocyc.CPLX0-8582`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8582`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P37747|protein.P37747]]

## Enriched Summary

UDP-D-galactopyranose mutase catalyzes the reversible interconversion of UDP-galactopyranose and UDP-galactofuranose . UDP-galactofuranose is required for repeat-unit synthesis in O antigen biosynthesis . When the rfb-50 mutation, an IS5 insertion in the gene encoding rhamnosyl transferase, wbbL, is complemented with a wild type wbbL gene, E. coli K-12 produces the O16 variant of O antigen, with a β-D-galactofuranosyl moiety in the repeating unit . The reaction mechanism of UDP-D-galactopyranose mutase has been studied, and it was shown that FAD plays an active role in regulating catalysis . Studies using deaza-FAD analogs support a radical mechanism for catalysis . The reaction mechanism involves concerted breaking and formation of a bond between the substrate and the FAD coenzyme . A crystal structure of the enzyme has been solved at 2.4 Å resolution . Glf: "galactofuranose" UDP-D-galactopyranose mutase catalyzes the reversible interconversion of UDP-galactopyranose and UDP-galactofuranose . UDP-galactofuranose is required for repeat-unit synthesis in O antigen biosynthesis . When the rfb-50 mutation, an IS5 insertion in the gene encoding rhamnosyl transferase, wbbL, is complemented with a wild type wbbL gene, E. coli K-12 produces the O16 variant of O antigen, with a β-D-galactofuranosyl moiety in the repeating unit...

## Biological Role

Catalyzes GALPMUT-RXN (reaction.ecocyc.GALPMUT-RXN). Bound by FAD (molecule.C00016).

## Annotation

UDP-D-galactopyranose mutase catalyzes the reversible interconversion of UDP-galactopyranose and UDP-galactofuranose . UDP-galactofuranose is required for repeat-unit synthesis in O antigen biosynthesis . When the rfb-50 mutation, an IS5 insertion in the gene encoding rhamnosyl transferase, wbbL, is complemented with a wild type wbbL gene, E. coli K-12 produces the O16 variant of O antigen, with a β-D-galactofuranosyl moiety in the repeating unit . The reaction mechanism of UDP-D-galactopyranose mutase has been studied, and it was shown that FAD plays an active role in regulating catalysis . Studies using deaza-FAD analogs support a radical mechanism for catalysis . The reaction mechanism involves concerted breaking and formation of a bond between the substrate and the FAD coenzyme . A crystal structure of the enzyme has been solved at 2.4 Å resolution . Glf: "galactofuranose"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GALPMUT-RXN|reaction.ecocyc.GALPMUT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P37747|protein.P37747]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8582`
- `QSPROTEOME:QS00182027`

## Notes

2*protein.P37747
