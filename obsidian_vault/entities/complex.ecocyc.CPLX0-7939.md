---
entity_id: "complex.ecocyc.CPLX0-7939"
entity_type: "complex"
name: "regulator of KefC-mediated potassium transport and quinone oxidoreductase"
source_database: "EcoCyc"
source_id: "CPLX0-7939"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# regulator of KefC-mediated potassium transport and quinone oxidoreductase

`complex.ecocyc.CPLX0-7939`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7939`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A754|protein.P0A754]]

## Enriched Summary

KefF is an activator of potassium transport mediated by the CPLX0-7819 KefC antiporter . KefF also has enzymatic activity as a quinone oxidoreductase, thereby apparently reducing the redox toxicity of electrophilic quinones. This enzymatic activity of KefF is not required for its function as an activator of KefC . NAD(P)H dehydrogenase activity of KefF was predicted based on sequence similarity . Crystal structures of an artificially constructed KefF fusion with the C-terminal domain of KefC have been solved . KefF may exert its effect on the activity of KefC by influencing the angle of KefC's hinge domain . A kefF mutant exhibits a defect in KefC-mediated potassium transport . Expression in E. coli of a yabF gene of environmental origin results in carbonyl biosynthesis from polyols . KefF is an activator of potassium transport mediated by the CPLX0-7819 KefC antiporter . KefF also has enzymatic activity as a quinone oxidoreductase, thereby apparently reducing the redox toxicity of electrophilic quinones. This enzymatic activity of KefF is not required for its function as an activator of KefC . NAD(P)H dehydrogenase activity of KefF was predicted based on sequence similarity . Crystal structures of an artificially constructed KefF fusion with the C-terminal domain of KefC have been solved...

## Biological Role

Catalyzes NQOR-RXN (reaction.ecocyc.NQOR-RXN). Bound by FMN (molecule.C00061).

## Annotation

KefF is an activator of potassium transport mediated by the CPLX0-7819 KefC antiporter . KefF also has enzymatic activity as a quinone oxidoreductase, thereby apparently reducing the redox toxicity of electrophilic quinones. This enzymatic activity of KefF is not required for its function as an activator of KefC . NAD(P)H dehydrogenase activity of KefF was predicted based on sequence similarity . Crystal structures of an artificially constructed KefF fusion with the C-terminal domain of KefC have been solved . KefF may exert its effect on the activity of KefC by influencing the angle of KefC's hinge domain . A kefF mutant exhibits a defect in KefC-mediated potassium transport . Expression in E. coli of a yabF gene of environmental origin results in carbonyl biosynthesis from polyols .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.NQOR-RXN|reaction.ecocyc.NQOR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A754|protein.P0A754]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7939`
- `QSPROTEOME:QS00049680`

## Notes

2*protein.P0A754
