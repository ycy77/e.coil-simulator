---
entity_id: "complex.ecocyc.ABC-49-CPLX"
entity_type: "complex"
name: "glutathione ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-49-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glutathione ABC transporter

`complex.ecocyc.ABC-49-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-49-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `structural`
- Components: [[protein.P75796|protein.P75796]], [[protein.P75797|protein.P75797]], [[protein.P75799|protein.P75799]], [[protein.P75798|protein.P75798]]

## Enriched Summary

GsiABCD is glutathione (GSH) uptake system that is a member of the ATP Binding Cassette (ABC) superfamily of transporters. GsiABCD is the major transporter of oxidized (OXIDIZED-GLUTATHIONE GSSG), but not reduced glutathione (GLUTATHIONE GSG) . Extracellular GSH accumulates during aerobic growth of E. coli K-12; the concentration of external GSH reaches a maximum during early stationary phase and declines thereafter . The GsiABCD transporter and a periplasmic CPLX0-7885 (GGT) both contribute to GSH salvage; in a (GSH overproducing) strain lacking both these systems (ΔggtΔgsiAB) the concentration of external GSH increases even during stationary phase and this phenotype is partially complemented by expression of the ABC transporter from a plasmid . The GsiABCD transporter catalyses uptake of labeled GSH in a GGT deficient background; uptake is inhibited by the ATPase inhibitor, verapamil . GsiABCD contributes to the growth of E. coli K-12 with GSH as a sole sulfur source . GsiC and GsiD are the predicted integral membrane subunits of the transporter complex, GsiA is the predicted ATP-binding subunit and GsiB is the periplasmic glutathione binding protein . iaaA encoding CPLX0-263 and gsiABCD may constitute an operon . gsi: glutathione (GSH) importer . GsiABCD is glutathione (GSH) uptake system that is a member of the ATP Binding Cassette (ABC) superfamily of transporters...

## Biological Role

Catalyzes RXN0-11 (reaction.ecocyc.RXN0-11), TRANS-RXN0-637 (reaction.ecocyc.TRANS-RXN0-637). Transports Glutathione (molecule.C00051), Glutathione disulfide (molecule.C00127), hν (molecule.ecocyc.Light).

## Annotation

GsiABCD is glutathione (GSH) uptake system that is a member of the ATP Binding Cassette (ABC) superfamily of transporters. GsiABCD is the major transporter of oxidized (OXIDIZED-GLUTATHIONE GSSG), but not reduced glutathione (GLUTATHIONE GSG) . Extracellular GSH accumulates during aerobic growth of E. coli K-12; the concentration of external GSH reaches a maximum during early stationary phase and declines thereafter . The GsiABCD transporter and a periplasmic CPLX0-7885 (GGT) both contribute to GSH salvage; in a (GSH overproducing) strain lacking both these systems (ΔggtΔgsiAB) the concentration of external GSH increases even during stationary phase and this phenotype is partially complemented by expression of the ABC transporter from a plasmid . The GsiABCD transporter catalyses uptake of labeled GSH in a GGT deficient background; uptake is inhibited by the ATPase inhibitor, verapamil . GsiABCD contributes to the growth of E. coli K-12 with GSH as a sole sulfur source . GsiC and GsiD are the predicted integral membrane subunits of the transporter complex, GsiA is the predicted ATP-binding subunit and GsiB is the periplasmic glutathione binding protein . iaaA encoding CPLX0-263 and gsiABCD may constitute an operon . gsi: glutathione (GSH) importer .

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.RXN0-11|reaction.ecocyc.RXN0-11]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-637|reaction.ecocyc.TRANS-RXN0-637]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00127|molecule.C00127]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P75796|protein.P75796]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P75797|protein.P75797]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P75798|protein.P75798]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P75799|protein.P75799]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-49-CPLX`
- `QSPROTEOME:QS00049326`

## Notes

1*protein.P75796|1*protein.P75797|1*protein.P75799|1*protein.P75798
