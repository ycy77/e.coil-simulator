---
entity_id: "complex.ecocyc.CPLX0-7989"
entity_type: "complex"
name: "murein tripeptide amidase A"
source_database: "EcoCyc"
source_id: "CPLX0-7989"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# murein tripeptide amidase A

`complex.ecocyc.CPLX0-7989`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7989`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0ACV6|protein.P0ACV6]]

## Enriched Summary

MpaA is a zinc carboxypeptidase that specifically hydrolyzes the γ-D-Glu-meso-Dap amide bond of the murein tripeptide L-Ala-γ-D-Glu-meso-Dap . An mpaA mutation greatly increases cytoplasmic accumulation of murein tripeptide in an mpl mutant . mpaA expression is increased during growth under nitrogen starvation conditions; PgrR represses expression of mpaA in the presence of good nitrogen sources . MpaA: "murein peptide amidase A" Review: MpaA is a zinc carboxypeptidase that specifically hydrolyzes the γ-D-Glu-meso-Dap amide bond of the murein tripeptide L-Ala-γ-D-Glu-meso-Dap . An mpaA mutation greatly increases cytoplasmic accumulation of murein tripeptide in an mpl mutant . mpaA expression is increased during growth under nitrogen starvation conditions; PgrR represses expression of mpaA in the presence of good nitrogen sources . MpaA: "murein peptide amidase A" Review:

## Biological Role

Catalyzes RXN0-961 (reaction.ecocyc.RXN0-961).

## Annotation

MpaA is a zinc carboxypeptidase that specifically hydrolyzes the γ-D-Glu-meso-Dap amide bond of the murein tripeptide L-Ala-γ-D-Glu-meso-Dap . An mpaA mutation greatly increases cytoplasmic accumulation of murein tripeptide in an mpl mutant . mpaA expression is increased during growth under nitrogen starvation conditions; PgrR represses expression of mpaA in the presence of good nitrogen sources . MpaA: "murein peptide amidase A" Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-961|reaction.ecocyc.RXN0-961]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0ACV6|protein.P0ACV6]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7989`
- `QSPROTEOME:QS00195935`

## Notes

2*protein.P0ACV6
