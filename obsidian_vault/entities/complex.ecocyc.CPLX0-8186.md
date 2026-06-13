---
entity_id: "complex.ecocyc.CPLX0-8186"
entity_type: "complex"
name: "galactitol-1-phosphate 5-dehydrogenase"
source_database: "EcoCyc"
source_id: "CPLX0-8186"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# galactitol-1-phosphate 5-dehydrogenase

`complex.ecocyc.CPLX0-8186`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8186`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9S3|protein.P0A9S3]]

## Enriched Summary

L-galactitol-1-phosphate 5-dehydrogenase (GatD) is an enantioselective polyol dehydrogenase that catalyzes NAD+-dependent oxidation of L-galactitol-1-phosphate, forming D-tagatose-6-phosphate . Some strains of E. coli K-12 are able to utilize galactitol as the sole source of carbon. After transport into the cell by a specific enzyme II of the PTS, galactitol-1-phosphate dehydrogenase converts galactitol-1-phosphate into tagatose-6-phosphate . Crystal structures of the enzyme have been solved. The homodimeric enzyme contains two metal ions per subunit, serving catalytic and structural roles, respectively . The role of various amino acid residues has been investigated by site-directed mutagenesis and kinetic analysis of the resulting mutants. A reaction mechanism was proposed . Endogenous GatD interacts with HisTrap nickel affinity columns . Mutants lacking galactitol-1-phosphate dehydrogenase are unable to grow on galactitol . L-galactitol-1-phosphate 5-dehydrogenase (GatD) is an enantioselective polyol dehydrogenase that catalyzes NAD+-dependent oxidation of L-galactitol-1-phosphate, forming D-tagatose-6-phosphate . Some strains of E. coli K-12 are able to utilize galactitol as the sole source of carbon. After transport into the cell by a specific enzyme II of the PTS, galactitol-1-phosphate dehydrogenase converts galactitol-1-phosphate into tagatose-6-phosphate...

## Biological Role

Catalyzes 1.1.1.251-RXN (reaction.ecocyc.1.1.1.251-RXN). Bound by Zinc cation (molecule.C00038).

## Annotation

L-galactitol-1-phosphate 5-dehydrogenase (GatD) is an enantioselective polyol dehydrogenase that catalyzes NAD+-dependent oxidation of L-galactitol-1-phosphate, forming D-tagatose-6-phosphate . Some strains of E. coli K-12 are able to utilize galactitol as the sole source of carbon. After transport into the cell by a specific enzyme II of the PTS, galactitol-1-phosphate dehydrogenase converts galactitol-1-phosphate into tagatose-6-phosphate . Crystal structures of the enzyme have been solved. The homodimeric enzyme contains two metal ions per subunit, serving catalytic and structural roles, respectively . The role of various amino acid residues has been investigated by site-directed mutagenesis and kinetic analysis of the resulting mutants. A reaction mechanism was proposed . Endogenous GatD interacts with HisTrap nickel affinity columns . Mutants lacking galactitol-1-phosphate dehydrogenase are unable to grow on galactitol .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.1.1.1.251-RXN|reaction.ecocyc.1.1.1.251-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A9S3|protein.P0A9S3]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8186`
- `QSPROTEOME:QS00157517`

## Notes

2*protein.P0A9S3
