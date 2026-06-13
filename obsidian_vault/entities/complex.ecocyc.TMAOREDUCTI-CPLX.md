---
entity_id: "complex.ecocyc.TMAOREDUCTI-CPLX"
entity_type: "complex"
name: "menaquinol:trimethylamine N-oxide oxidoreductase I"
source_database: "EcoCyc"
source_id: "TMAOREDUCTI-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "TorCA"
---

# menaquinol:trimethylamine N-oxide oxidoreductase I

`complex.ecocyc.TMAOREDUCTI-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:TMAOREDUCTI-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P33226|protein.P33226]], [[protein.P33225|protein.P33225]]

## Enriched Summary

This complex represents the interaction between membrane associated cytochrome c menaquinol dehydrogenase TorC and periplasmic trimethylamine N-oxide (TMAO) reductase TorA. During anaerobic TMAO respiration TorC shuttles electrons from the membrane menaquinone pool to TorA for the reduction of TMAO to trimethylamine in the periplasm. TorC binds TorA in vitro ; the TorCA interaction is considered to be transient in vivo (see ). TorCA abundance is reduced under iron-limiting conditions; the CPD-15873 is required for induction of torCAD expression, likely acting at a transcriptional level . This complex represents the interaction between membrane associated cytochrome c menaquinol dehydrogenase TorC and periplasmic trimethylamine N-oxide (TMAO) reductase TorA. During anaerobic TMAO respiration TorC shuttles electrons from the membrane menaquinone pool to TorA for the reduction of TMAO to trimethylamine in the periplasm. TorC binds TorA in vitro ; the TorCA interaction is considered to be transient in vivo (see ). TorCA abundance is reduced under iron-limiting conditions; the CPD-15873 is required for induction of torCAD expression, likely acting at a transcriptional level .

## Biological Role

Catalyzes Trimethylamine-N-oxide reductase (menaquinone) (reaction.ecocyc.RXN0-5264). Bound by bis(guanylyl molybdopterin) cofactor (molecule.ecocyc.CPD-15873), heme c (molecule.ecocyc.HEME_C).

## Annotation

This complex represents the interaction between membrane associated cytochrome c menaquinol dehydrogenase TorC and periplasmic trimethylamine N-oxide (TMAO) reductase TorA. During anaerobic TMAO respiration TorC shuttles electrons from the membrane menaquinone pool to TorA for the reduction of TMAO to trimethylamine in the periplasm. TorC binds TorA in vitro ; the TorCA interaction is considered to be transient in vivo (see ). TorCA abundance is reduced under iron-limiting conditions; the CPD-15873 is required for induction of torCAD expression, likely acting at a transcriptional level .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5264|reaction.ecocyc.RXN0-5264]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `binds` <-- [[molecule.ecocyc.CPD-15873|molecule.ecocyc.CPD-15873]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.HEME_C|molecule.ecocyc.HEME_C]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P33225|protein.P33225]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P33226|protein.P33226]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:TMAOREDUCTI-CPLX`
- `QSPROTEOME:QS00049531`

## Notes

protein.P33226|protein.P33225
