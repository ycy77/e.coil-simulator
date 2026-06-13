---
entity_id: "complex.ecocyc.2OXOGLUTARATEDEH-CPLX"
entity_type: "complex"
name: "2-oxoglutarate dehydrogenase complex"
source_database: "EcoCyc"
source_id: "2OXOGLUTARATEDEH-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "OGDH"
---

# 2-oxoglutarate dehydrogenase complex

`complex.ecocyc.2OXOGLUTARATEDEH-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:2OXOGLUTARATEDEH-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.E1O|complex.ecocyc.E1O]], [[complex.ecocyc.E2O|complex.ecocyc.E2O]], [[complex.ecocyc.E3-CPLX|complex.ecocyc.E3-CPLX]]

## Enriched Summary

The 2-oxoglutarate (2-ketoglutarate) dehydrogenase complex is similar in enzyme composition and complex reactions to the pyruvate dehydrogenase complex reactions (see PWY-5084 and PYRUVDEHYD-PWY). SUBREACTIONS: E1(o) + TPP = E1(o).TPP E1(o).TPP + succinate = E1(o).hydroxycarboxypropylTPP + CO(2) E1(o).hydroxycarboxypropylTPP + E2(o).lipoate(S2) = E1(o).TPP + E2(o).lipoate(SH)(S-succinyl) E2(o).lipoate(SH)(S-succinyl) + CoA = E2(o).lip(SH)2 + succinylCoA E3 + FAD = E3.FAD E3.FAD + E2(o).lip(SH)2 = E3.FADH(2) + E2(o).lip(S)2 E3.FADH(2) + NAD(+) = E3.FAD + NADH + H(+) (see . The 2-oxoglutarate (2-ketoglutarate) dehydrogenase complex is similar in enzyme composition and complex reactions to the pyruvate dehydrogenase complex reactions (see PWY-5084 and PYRUVDEHYD-PWY). SUBREACTIONS: E1(o) + TPP = E1(o).TPP E1(o).TPP + succinate = E1(o).hydroxycarboxypropylTPP + CO(2) E1(o).hydroxycarboxypropylTPP + E2(o).lipoate(S2) = E1(o).TPP + E2(o).lipoate(SH)(S-succinyl) E2(o).lipoate(SH)(S-succinyl) + CoA = E2(o).lip(SH)2 + succinylCoA E3 + FAD = E3.FAD E3.FAD + E2(o).lip(SH)2 = E3.FADH(2) + E2(o).lip(S)2 E3.FADH(2) + NAD(+) = E3.FAD + NADH + H(+) (see .

## Biological Role

Catalyzes 2-oxoglutarate dehydrogenase complex (reaction.ecocyc.2OXOGLUTARATEDEH-RXN). Bound by FAD (molecule.C00016), Thiamin diphosphate (molecule.C00068), Magnesium cation (molecule.C00305), (R)-Lipoate (molecule.C16241).

## Annotation

The 2-oxoglutarate (2-ketoglutarate) dehydrogenase complex is similar in enzyme composition and complex reactions to the pyruvate dehydrogenase complex reactions (see PWY-5084 and PYRUVDEHYD-PWY). SUBREACTIONS: E1(o) + TPP = E1(o).TPP E1(o).TPP + succinate = E1(o).hydroxycarboxypropylTPP + CO(2) E1(o).hydroxycarboxypropylTPP + E2(o).lipoate(S2) = E1(o).TPP + E2(o).lipoate(SH)(S-succinyl) E2(o).lipoate(SH)(S-succinyl) + CoA = E2(o).lip(SH)2 + succinylCoA E3 + FAD = E3.FAD E3.FAD + E2(o).lip(SH)2 = E3.FADH(2) + E2(o).lip(S)2 E3.FADH(2) + NAD(+) = E3.FAD + NADH + H(+) (see .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2OXOGLUTARATEDEH-RXN|reaction.ecocyc.2OXOGLUTARATEDEH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (10)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00068|molecule.C00068]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C16241|molecule.C16241]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[complex.ecocyc.E1O|complex.ecocyc.E1O]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.E2O|complex.ecocyc.E2O]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.E3-CPLX|complex.ecocyc.E3-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P0A9P0|protein.P0A9P0]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0AFG3|protein.P0AFG3]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` <-- [[protein.P0AFG6|protein.P0AFG6]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=24

## External IDs

- `EcoCyc:2OXOGLUTARATEDEH-CPLX`

## Notes

1*complex.ecocyc.E1O|1*complex.ecocyc.E2O|1*complex.ecocyc.E3-CPLX
