---
entity_id: "complex.ecocyc.HISTDEHYD-CPLX"
entity_type: "complex"
name: "histidinol dehydrogenase"
source_database: "EcoCyc"
source_id: "HISTDEHYD-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# histidinol dehydrogenase

`complex.ecocyc.HISTDEHYD-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:HISTDEHYD-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P06988|protein.P06988]]

## Enriched Summary

The bifunctional histidinol / histidinal dehydrogenase (HisD) carries out the final two steps in histidine biosynthesis. HisD catalyzes both the dehydrogenation of histidinol to yield histidinal and the subsequent dehydrogenation of histidinal to generate L-histidine . HisD exists as a homodimer . Crystal structures have been determined for the apo form of the enzyme, as well as for HisD complexed with substrate, NAD+, and divalent cation . This is an example of a bifunctional NAD-linke dehydrogenase, with both an alcohol dehydrogenase and an aldehyde dehydrogenase on the same protein. Based on work in Salmonella, HisD appears to function by carrying out the first oxidation step at an active site on one subunit, and then passing the intermediate to a vicinal site on the adjacent subunit, where the second oxidation step takes places . Since the histidine biosynthetic pathway is found in bacteria, but not in humans, it is an attractive target for the developement of anti-infectives. hisD has been found to be essential in Mycobacterium tuberculosis . The bifunctional histidinol / histidinal dehydrogenase (HisD) carries out the final two steps in histidine biosynthesis. HisD catalyzes both the dehydrogenation of histidinol to yield histidinal and the subsequent dehydrogenation of histidinal to generate L-histidine . HisD exists as a homodimer...

## Biological Role

Catalyzes RXN-8001 (reaction.ecocyc.RXN-8001). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

The bifunctional histidinol / histidinal dehydrogenase (HisD) carries out the final two steps in histidine biosynthesis. HisD catalyzes both the dehydrogenation of histidinol to yield histidinal and the subsequent dehydrogenation of histidinal to generate L-histidine . HisD exists as a homodimer . Crystal structures have been determined for the apo form of the enzyme, as well as for HisD complexed with substrate, NAD+, and divalent cation . This is an example of a bifunctional NAD-linke dehydrogenase, with both an alcohol dehydrogenase and an aldehyde dehydrogenase on the same protein. Based on work in Salmonella, HisD appears to function by carrying out the first oxidation step at an active site on one subunit, and then passing the intermediate to a vicinal site on the adjacent subunit, where the second oxidation step takes places . Since the histidine biosynthetic pathway is found in bacteria, but not in humans, it is an attractive target for the developement of anti-infectives. hisD has been found to be essential in Mycobacterium tuberculosis .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-8001|reaction.ecocyc.RXN-8001]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P06988|protein.P06988]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:HISTDEHYD-CPLX`
- `QSPROTEOME:QS00181851`

## Notes

2*protein.P06988
