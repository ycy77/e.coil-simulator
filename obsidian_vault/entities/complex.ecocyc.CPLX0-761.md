---
entity_id: "complex.ecocyc.CPLX0-761"
entity_type: "complex"
name: "putative xanthine dehydrogenase"
source_database: "EcoCyc"
source_id: "CPLX0-761"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# putative xanthine dehydrogenase

`complex.ecocyc.CPLX0-761`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-761`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.Q46799|protein.Q46799]], [[protein.Q46800|protein.Q46800]], [[protein.Q46801|protein.Q46801]]

## Enriched Summary

XdhA-XdhB-XdhC is a putative heterotrimeric xanthine dehydrogenase which may contribute to purine salvage . Degradation of hypoxanthine, xanthosine, inosine, or allantoin does not provide adequate nitrogen to support cell growth under aerobic conditions, in contrast to degradation of adenine or adenosine, which does support cell growth . Hypoxanthine, guanosine, inosine, or xanthosine (but not allantoin) speeds the growth of cells utilizing aspartate as the nitrogen source . Xanthine degradation to allantoin has been observed . It is suggested that xanthine dehydrogenase plays a role in purine salvage, perhaps by favoring production of GMP rather than AMP . Xanthine dehydrogenase may contribute to purine degradation under microaerobic and anaerobic conditions (see ). XdhA-XdhB-XdhC is a putative heterotrimeric xanthine dehydrogenase which may contribute to purine salvage . Degradation of hypoxanthine, xanthosine, inosine, or allantoin does not provide adequate nitrogen to support cell growth under aerobic conditions, in contrast to degradation of adenine or adenosine, which does support cell growth . Hypoxanthine, guanosine, inosine, or xanthosine (but not allantoin) speeds the growth of cells utilizing aspartate as the nitrogen source . Xanthine degradation to allantoin has been observed...

## Biological Role

Catalyzes RXN-7682 (reaction.ecocyc.RXN-7682), RXN0-901 (reaction.ecocyc.RXN0-901). Bound by FAD (molecule.C00016), Cytidylyl molybdenum cofactor (molecule.C21485), a [2Fe-2S] iron-sulfur cluster (molecule.ecocyc.CPD-6).

## Annotation

XdhA-XdhB-XdhC is a putative heterotrimeric xanthine dehydrogenase which may contribute to purine salvage . Degradation of hypoxanthine, xanthosine, inosine, or allantoin does not provide adequate nitrogen to support cell growth under aerobic conditions, in contrast to degradation of adenine or adenosine, which does support cell growth . Hypoxanthine, guanosine, inosine, or xanthosine (but not allantoin) speeds the growth of cells utilizing aspartate as the nitrogen source . Xanthine degradation to allantoin has been observed . It is suggested that xanthine dehydrogenase plays a role in purine salvage, perhaps by favoring production of GMP rather than AMP . Xanthine dehydrogenase may contribute to purine degradation under microaerobic and anaerobic conditions (see ).

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-7682|reaction.ecocyc.RXN-7682]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-901|reaction.ecocyc.RXN0-901]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (6)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C21485|molecule.C21485]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-6|molecule.ecocyc.CPD-6]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.Q46799|protein.Q46799]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.Q46800|protein.Q46800]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.Q46801|protein.Q46801]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-761`
- `QSPROTEOME:QS00049406`

## Notes

protein.Q46799|protein.Q46800|protein.Q46801
