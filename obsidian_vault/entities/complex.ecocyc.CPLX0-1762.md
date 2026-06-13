---
entity_id: "complex.ecocyc.CPLX0-1762"
entity_type: "complex"
name: "phenylacetyl-CoA 1,2-epoxidase"
source_database: "EcoCyc"
source_id: "CPLX0-1762"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# phenylacetyl-CoA 1,2-epoxidase

`complex.ecocyc.CPLX0-1762`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1762`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76081|protein.P76081]], [[protein.P76077|protein.P76077]], [[protein.P76079|protein.P76079]], [[protein.P76078|protein.P76078]]

## Enriched Summary

The ring 1,2-phenylacetyl-CoA epoxidase, comprised of the PaaA, PaaB, PaaC, and PaaE polypeptides, catalyzes the second step in the aerobic degradation of phenylacetate . Stable subcomplexes composed of PaaABC, PaaAC and PaaBC can be purified, but only the combination of the PaaABC complex together with PaaE has full activity . Crystal structures of the PaaAC subcomplex alone and together with a variety of ligands have been solved . The ring 1,2-phenylacetyl-CoA epoxidase, comprised of the PaaA, PaaB, PaaC, and PaaE polypeptides, catalyzes the second step in the aerobic degradation of phenylacetate . Stable subcomplexes composed of PaaABC, PaaAC and PaaBC can be purified, but only the combination of the PaaABC complex together with PaaE has full activity . Crystal structures of the PaaAC subcomplex alone and together with a variety of ligands have been solved .

## Biological Role

Catalyzes RXN0-2042 (reaction.ecocyc.RXN0-2042). Bound by FAD (molecule.C00016), a [2Fe-2S] iron-sulfur cluster (molecule.ecocyc.CPD-6).

## Annotation

The ring 1,2-phenylacetyl-CoA epoxidase, comprised of the PaaA, PaaB, PaaC, and PaaE polypeptides, catalyzes the second step in the aerobic degradation of phenylacetate . Stable subcomplexes composed of PaaABC, PaaAC and PaaBC can be purified, but only the combination of the PaaABC complex together with PaaE has full activity . Crystal structures of the PaaAC subcomplex alone and together with a variety of ligands have been solved .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-2042|reaction.ecocyc.RXN0-2042]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (6)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-6|molecule.ecocyc.CPD-6]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P76077|protein.P76077]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P76078|protein.P76078]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P76079|protein.P76079]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P76081|protein.P76081]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-1762`
- `QSPROTEOME:QS00049412`

## Notes

protein.P76081|protein.P76077|protein.P76079|protein.P76078
