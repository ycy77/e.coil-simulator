---
entity_id: "complex.ecocyc.AERGLYC3PDEHYDROG-CPLX"
entity_type: "complex"
name: "aerobic glycerol 3-phosphate dehydrogenase"
source_database: "EcoCyc"
source_id: "AERGLYC3PDEHYDROG-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "GlpD"
  - "glycerol-3-phosphate oxidase"
  - "glycerol-3-phosphate:ubiquinone oxidoreductase"
---

# aerobic glycerol 3-phosphate dehydrogenase

`complex.ecocyc.AERGLYC3PDEHYDROG-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:AERGLYC3PDEHYDROG-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `regulatory`
- Components: [[protein.P13035|protein.P13035]]

## Enriched Summary

glpD encodes aerobic glycerol 3-phosphate dehydrogenase which catalyses the oxidation of sn-glycerol 3-phosphate to dihydroxyacetone phosphate. GlpD is a respiratory enzyme and shuttles electrons via a noncovalently bound FAD cofactor to reduce ubiquinone . Mutants lacking glpD are unable to grow on glycerol or glycerol 3-phosphate . Glycerol 3-phosphate is an obligatory intermediate in phospholipid biosynthesis and thus glpD expression is regulated to ensure that phospholipid biosynthesis is maintained while the energy needs of the cell are met. Expression of glpD (along with other members of the glp regulon) is repressed by PD03576 "GlpR" and induced by glycerol 3-phosphate . Anaerobically glpD expression is repressed by the two-component regulatory system arcA and arcB . Both ubiquinone and menaquinone restore glycerol 3-phosphate oxidase activity in membranes isolated from an E. coli strain lacking quinones (ubiA- menA-) . GlpD is a homodimeric enzyme associated with the cytoplasmic membrane through binding to negatively-charged phopholipids . GlpD is composed of two domains, the soluble extramembranous C-terminal "cap" domain and a membrane-bound N-terminal domain which binds FAD and glycerol 3-phosphate and is also thought to be the ubiquinone docking domain...

## Biological Role

Catalyzes sn-glycerol 3-phosphate:ubiquinone oxidoreductase (reaction.ecocyc.RXN0-5260). Bound by FAD (molecule.C00016).

## Annotation

glpD encodes aerobic glycerol 3-phosphate dehydrogenase which catalyses the oxidation of sn-glycerol 3-phosphate to dihydroxyacetone phosphate. GlpD is a respiratory enzyme and shuttles electrons via a noncovalently bound FAD cofactor to reduce ubiquinone . Mutants lacking glpD are unable to grow on glycerol or glycerol 3-phosphate . Glycerol 3-phosphate is an obligatory intermediate in phospholipid biosynthesis and thus glpD expression is regulated to ensure that phospholipid biosynthesis is maintained while the energy needs of the cell are met. Expression of glpD (along with other members of the glp regulon) is repressed by PD03576 "GlpR" and induced by glycerol 3-phosphate . Anaerobically glpD expression is repressed by the two-component regulatory system arcA and arcB . Both ubiquinone and menaquinone restore glycerol 3-phosphate oxidase activity in membranes isolated from an E. coli strain lacking quinones (ubiA- menA-) . GlpD is a homodimeric enzyme associated with the cytoplasmic membrane through binding to negatively-charged phopholipids . GlpD is composed of two domains, the soluble extramembranous C-terminal "cap" domain and a membrane-bound N-terminal domain which binds FAD and glycerol 3-phosphate and is also thought to be the ubiquinone docking domain . Seven fully active structures of GlpD in the native state and with bound substrate analogues have been solved to at least 1.75 Å resolution . E. coli K-12 contains two glycerol 3-phosphate dehydrogenases encoded by the glpD and glpABC genes. GlpD is required for aerobic growth with glycerol or glycerol 3-phosphate while ANGLYC3PDEHYDROG-CPLX "GlpABC" is required for anaerobic growth with glycerol (or glycerol 3-phosphate) and fumarate. Either enzyme suffices for anaerobic growth on glycerol and nitrate (see

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5260|reaction.ecocyc.RXN0-5260]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P13035|protein.P13035]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:AERGLYC3PDEHYDROG-CPLX`
- `QSPROTEOME:QS00049346`
- `PDB:2R45`
- `PDB:2R46`
- `PDB:2R4E`
- `PDB:2R4J`
- `PDB:2QCU`

## Notes

2*protein.P13035
