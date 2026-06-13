---
entity_id: "complex.ecocyc.ABC-34-CPLX"
entity_type: "complex"
name: "sn-glycerol 3-phosphate / glycerophosphodiester ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-34-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# sn-glycerol 3-phosphate / glycerophosphodiester ABC transporter

`complex.ecocyc.ABC-34-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-34-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `structural`
- Components: [[protein.P10907|protein.P10907]], [[protein.P10905|protein.P10905]], [[protein.P10906|protein.P10906]], [[protein.P0AG80|protein.P0AG80]]

## Enriched Summary

UgpBAEC is an ATP-dependent sn-glycerol 3-phosphate (G3P) and glycerophosphodiester uptake system that is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters . UgpA and UgpE are the predicted inner membrane subunits of the transporter complex, UgpC is the predicted ATP-binding subunit and UgpB is the periplasmic binding protein . The binding protein dependent G3P transport system was initially characterized in glpT::Mucts strains which had regained the capacity to grow on G3P . sn-Glycerol 3-phosphate can be used as a carbon source and a phosphate source and is also an essential intermediate in phospholipid biosynthesis .The Ugp system can supply G3P as a sole phosphate source but is unable to supply enough carbon for bacterial growth . Ugp-mediated uptake of G3P is inhibited by increased internal phosphate concentration which may explain why G3P transported by the Ugp system can serve as a sole phosphate source but not a sole carbon source . The ATPase activity of the Ugp system reconstituted in vitro is insensitive to the putative inhibitors phosphate, PhoU or UgpQ . Glycerophosphodiesters, such as glycerophosphoethanolamaine (GPE), glycerophosphocholine (GPC) and glycerophosphoglycerol (GPG) are high affinity substrates of the Ugp transport system...

## Biological Role

Catalyzes ABC-34-RXN (reaction.ecocyc.ABC-34-RXN), TRANS-RXN0-573 (reaction.ecocyc.TRANS-RXN0-573). Transports sn-Glycerol 3-phosphate (molecule.C00093), an sn-glycerophosphodiester (molecule.ecocyc.Glycerophosphodiesters), hν (molecule.ecocyc.Light).

## Annotation

UgpBAEC is an ATP-dependent sn-glycerol 3-phosphate (G3P) and glycerophosphodiester uptake system that is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters . UgpA and UgpE are the predicted inner membrane subunits of the transporter complex, UgpC is the predicted ATP-binding subunit and UgpB is the periplasmic binding protein . The binding protein dependent G3P transport system was initially characterized in glpT::Mucts strains which had regained the capacity to grow on G3P . sn-Glycerol 3-phosphate can be used as a carbon source and a phosphate source and is also an essential intermediate in phospholipid biosynthesis .The Ugp system can supply G3P as a sole phosphate source but is unable to supply enough carbon for bacterial growth . Ugp-mediated uptake of G3P is inhibited by increased internal phosphate concentration which may explain why G3P transported by the Ugp system can serve as a sole phosphate source but not a sole carbon source . The ATPase activity of the Ugp system reconstituted in vitro is insensitive to the putative inhibitors phosphate, PhoU or UgpQ . Glycerophosphodiesters, such as glycerophosphoethanolamaine (GPE), glycerophosphocholine (GPC) and glycerophosphoglycerol (GPG) are high affinity substrates of the Ugp transport system. Glycerophosphodiesters transported by the Ugp system are hydrolysed very quickly at the inner face of the cytoplasmic membrane, the G3P moiety can be detected in the cytoplasm whereas the corresponding alcohol is usually found in the culture medium . G3P uptake via the Ugp system does not operate in membrane vesicles but can be observed in whole cell experiments . Purified UgpAEC2 displays UgpB/G3P stimulated ATPase activity in proteoliposomes . ugpBAEC likely forms an operon with ugpQ encoding a cytosol

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.ABC-34-RXN|reaction.ecocyc.ABC-34-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-573|reaction.ecocyc.TRANS-RXN0-573]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Glycerophosphodiesters|molecule.ecocyc.Glycerophosphodiesters]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P0AG80|protein.P0AG80]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P10905|protein.P10905]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P10906|protein.P10906]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P10907|protein.P10907]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:ABC-34-CPLX`
- `QSPROTEOME:QS00185113`

## Notes

2*protein.P10907|1*protein.P10905|1*protein.P10906|1*protein.P0AG80
