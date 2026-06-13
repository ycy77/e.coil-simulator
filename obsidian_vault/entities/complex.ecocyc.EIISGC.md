---
entity_id: "complex.ecocyc.EIISGC"
entity_type: "complex"
name: "putative PTS enzyme II SgcBCA"
source_database: "EcoCyc"
source_id: "EIISGC"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "EII<sup>Sgc</sup>"
  - "Enzyme II<sup>Sgc</sup>"
---

# putative PTS enzyme II SgcBCA

`complex.ecocyc.EIISGC`

## Static

- Type: `complex`
- Source: `EcoCyc:EIISGC`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P58035|protein.P58035]], [[protein.P39365|protein.P39365]], [[protein.P39363|protein.P39363]]

## Enriched Summary

SgcBCA, a putative PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its substrates in a process called group translocation (reviewed in . sgcA is homologous to the IIA domains of the fructose- and mannitol-specific PTS permeases. sgcA has the highest similarity to IIA domains of the L-ascorbate PTS and the cryptic mannitol PTS. sgcC has 40% identity with the IIC domain of the galactitol PTS. sgcC encodes a protein with 9 or 10 predicted transmembrane regions . sgcB shows sequence similarity to the IIB domain of the galactitol-specific PTS permease . The function of these proteins is not known . Please note that the expression of the sgc gene cluster (sgcREAQCBX) has not been studied and the presence of an sgcBCA encoded protein complex is hypothetical. SgcBCA, a putative PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its substrates in a process called group translocation (reviewed in . sgcA is homologous to the IIA domains of the fructose- and mannitol-specific PTS permeases...

## Annotation

SgcBCA, a putative PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its substrates in a process called group translocation (reviewed in . sgcA is homologous to the IIA domains of the fructose- and mannitol-specific PTS permeases. sgcA has the highest similarity to IIA domains of the L-ascorbate PTS and the cryptic mannitol PTS. sgcC has 40% identity with the IIC domain of the galactitol PTS. sgcC encodes a protein with 9 or 10 predicted transmembrane regions . sgcB shows sequence similarity to the IIB domain of the galactitol-specific PTS permease . The function of these proteins is not known . Please note that the expression of the sgc gene cluster (sgcREAQCBX) has not been studied and the presence of an sgcBCA encoded protein complex is hypothetical.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P39363|protein.P39363]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P39365|protein.P39365]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P58035|protein.P58035]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:EIISGC`
- `QSPROTEOME:QS00049490`

## Notes

protein.P58035|protein.P39365|protein.P39363
