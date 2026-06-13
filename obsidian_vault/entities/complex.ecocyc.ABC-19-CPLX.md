---
entity_id: "complex.ecocyc.ABC-19-CPLX"
entity_type: "complex"
name: "molybdate ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-19-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# molybdate ABC transporter

`complex.ecocyc.ABC-19-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-19-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P09833|protein.P09833]], [[protein.P0AF01|protein.P0AF01]], [[protein.P37329|protein.P37329]]

## Enriched Summary

Molybdate is an essential micronutrient which is incorporated (as molybdenum cofactor or Moco) into redox active molybdoenzymes (see . ModABC is a high-affinity molybdate transporter that is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters. ModA is the periplasmic molybdate binding component , ModB is the predicted integral membrane component and ModC is the predicted ATP-binding component, of the transporter complex . Early work characterized mod (chlD) mutants which lacked molybdoenzyme (nitrate reductase, formate dehydrogenase and trimethylamine-N-oxide) activity (and see also ). In cells lacking the high affinity ModABC transporter, molybdate appears to be transported by either the sulfate ABC transporter or a nonspecific anion transporter . The mod operon is expressed when molybdate is limiting ; molybdate-dependent repression of the mod operon is mediated by CPLX0-6 ModE . The annotation of modD as a fourth gene in the mod operon was later adjusted; an open reading frame in the reverse direction, yhbA, is now annotated at this location . The complex stoichiometry depicted here (ModAModB2ModC) has not been experimentally demonstrated but represents an archetypal ABC transporter. chlD: chlorate resistant (see for a description of chl mutants)...

## Biological Role

Catalyzes ABC-19-RXN (reaction.ecocyc.ABC-19-RXN).

## Annotation

Molybdate is an essential micronutrient which is incorporated (as molybdenum cofactor or Moco) into redox active molybdoenzymes (see . ModABC is a high-affinity molybdate transporter that is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters. ModA is the periplasmic molybdate binding component , ModB is the predicted integral membrane component and ModC is the predicted ATP-binding component, of the transporter complex . Early work characterized mod (chlD) mutants which lacked molybdoenzyme (nitrate reductase, formate dehydrogenase and trimethylamine-N-oxide) activity (and see also ). In cells lacking the high affinity ModABC transporter, molybdate appears to be transported by either the sulfate ABC transporter or a nonspecific anion transporter . The mod operon is expressed when molybdate is limiting ; molybdate-dependent repression of the mod operon is mediated by CPLX0-6 ModE . The annotation of modD as a fourth gene in the mod operon was later adjusted; an open reading frame in the reverse direction, yhbA, is now annotated at this location . The complex stoichiometry depicted here (ModAModB2ModC) has not been experimentally demonstrated but represents an archetypal ABC transporter. chlD: chlorate resistant (see for a description of chl mutants). Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ABC-19-RXN|reaction.ecocyc.ABC-19-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P09833|protein.P09833]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AF01|protein.P0AF01]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P37329|protein.P37329]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:ABC-19-CPLX`
- `QSPROTEOME:QS00049305`

## Notes

1*protein.P09833|2*protein.P0AF01|1*protein.P37329
