---
entity_id: "complex.ecocyc.CPLX0-7963"
entity_type: "complex"
name: "multidrug efflux pump EmrE / betaine:H+ antiporter"
source_database: "EcoCyc"
source_id: "CPLX0-7963"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# multidrug efflux pump EmrE / betaine:H+ antiporter

`complex.ecocyc.CPLX0-7963`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7963`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P23895|protein.P23895]]

## Enriched Summary

EmrE is a multidrug efflux protein with a broad substrate specificity. Overexpression of the gene confers resistance to a range of toxic polyaromatic compounds including ethidium , methyl viologen , tetracycline, tetraphenylphosphonium (TPP+), erythromycin, sulfadiazine , acriflavin, crystal violet, benzalkonium and the aminoglycoside antibiotics, streptomycin and tobramycin . EmrE transports the osmoprotectants betaine and choline and may function to prevent the build up of these compounds during or after significant osmotic stress . Purified, solubilised EmrE binds one TPP+ molecule per EmrE dimer . Purified EmrE, solubilised in detergent or reconstituted in liposomes, binds substrate (ethidium, methyl viologen, proflavin, TPP+) with µM affinity; EmrE monomers are capable of binding substrate . Binding of TPP+ to EmrE has been observed using NMR spectroscopy and electron crystallography . The regions involved in binding TPP+ as well as ethidium, propidium and dequalinium have been identified . NMR indicates that TPP+ bound EmrE interconverts between inward and outward-facing states consistent with a single-site alternating access model of transport . EmrE moves between its inward and outward facing states with varying kinetics; substrate identity influences the rate of transport by EmrE...

## Biological Role

Catalyzes ethidium:proton antiport (reaction.ecocyc.TRANS-RXN-344), sulfadiazine:proton antiport (reaction.ecocyc.TRANS-RXN0-493), glycine betaine:proton antiport (reaction.ecocyc.TRANS-RXN0-532), xenobiotic:proton antiport (electrogenic) (reaction.ecocyc.TRANS-RXN0-628), TRANS-RXN0-635 (reaction.ecocyc.TRANS-RXN0-635). Transports Betaine (molecule.C00719), tetraphenylphosphonium (molecule.ecocyc.CPD-20890), sulfadiazine (molecule.ecocyc.CPD-20940), ethidium (molecule.ecocyc.CPD0-1938), hν (molecule.ecocyc.Light).

## Annotation

EmrE is a multidrug efflux protein with a broad substrate specificity. Overexpression of the gene confers resistance to a range of toxic polyaromatic compounds including ethidium , methyl viologen , tetracycline, tetraphenylphosphonium (TPP+), erythromycin, sulfadiazine , acriflavin, crystal violet, benzalkonium and the aminoglycoside antibiotics, streptomycin and tobramycin . EmrE transports the osmoprotectants betaine and choline and may function to prevent the build up of these compounds during or after significant osmotic stress . Purified, solubilised EmrE binds one TPP+ molecule per EmrE dimer . Purified EmrE, solubilised in detergent or reconstituted in liposomes, binds substrate (ethidium, methyl viologen, proflavin, TPP+) with µM affinity; EmrE monomers are capable of binding substrate . Binding of TPP+ to EmrE has been observed using NMR spectroscopy and electron crystallography . The regions involved in binding TPP+ as well as ethidium, propidium and dequalinium have been identified . NMR indicates that TPP+ bound EmrE interconverts between inward and outward-facing states consistent with a single-site alternating access model of transport . EmrE moves between its inward and outward facing states with varying kinetics; substrate identity influences the rate of transport by EmrE . Purified EmrE, reconstituted in liposomes mediates the transport of ethidium and methyl viologen; transport is inhibited by the ionophore nigericin, suggesting that EmrE functions as a drug/proton antiporter . EmrE is a member of the small multidrug resistance (SMR) family of proton dependent multidrug efflux proteins . EmrE exchanges 2 protons for each drug molecule . The mechanism of ion-coupled transport, including the role played by the membrane embedded residue Glu-14, is the su

## Outgoing Edges (10)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-344|reaction.ecocyc.TRANS-RXN-344]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-493|reaction.ecocyc.TRANS-RXN0-493]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-532|reaction.ecocyc.TRANS-RXN0-532]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-628|reaction.ecocyc.TRANS-RXN0-628]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-635|reaction.ecocyc.TRANS-RXN0-635]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00719|molecule.C00719]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-20890|molecule.ecocyc.CPD-20890]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-20940|molecule.ecocyc.CPD-20940]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD0-1938|molecule.ecocyc.CPD0-1938]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P23895|protein.P23895]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX0-7963`
- `QSPROTEOME:QS00171727`
- `PDB:8UOZ`
- `PDB:8UWU`
- `PDB:7SZT`
- `PDB:7T00`
- `PDB:7SV9`
- `PDB:7SSU`
- `PDB:7SVX`
- `PDB:7MGX`

## Notes

2*protein.P23895
