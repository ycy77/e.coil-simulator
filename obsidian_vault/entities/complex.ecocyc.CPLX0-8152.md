---
entity_id: "complex.ecocyc.CPLX0-8152"
entity_type: "complex"
name: "cystine ABC transporter"
source_database: "EcoCyc"
source_id: "CPLX0-8152"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# cystine ABC transporter

`complex.ecocyc.CPLX0-8152`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8152`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P37774|protein.P37774]], [[protein.P0AFT2|protein.P0AFT2]], [[protein.P0AEM9|protein.P0AEM9]]

## Enriched Summary

tcyJ, tcyL and tcyN encode proteins that constitute a cystine transporter complex in E. coli K-12. The complex is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters; TcyJ (formerly FliY) is the periplasmic binding protein and sequence analysis suggests that TcyN (formerly YecC) and TcyL (formerlyYecS) are the ATP binding subunit and integral membrane subunit respectively . TcyJLN functions to replenish cysteine pools in sulfur starved cells; TcyJLN is a high-affinity transporter that functions when cystine is scarce whereas a second cystine transporter, G6934-MONOMER "TcyP", is the primary transporter when cystine is abundant . Under aerobic growth conditions, E. coli imports cystine as an economical alternative to sulfate assimilation; E. coli lacks a dedicated cysteine importer and under anaerobic conditions when cysteine remains in the reduced form cells may assimilate sulfur from hydrogen sulfide . TcyJLN, G6934-MONOMER "TcyP" and the L-cysteine exporter EG11639 "EamA" participate in an L-cystine/L-cysteine shuttle system which is suggested to protect the cell membrane under oxidative stress conditions; L-cystine importers (TcyJLN and TcyP) cooperate with an L-cysteine exporter (EamA) to supply reducing equivalents to the periplasm; operation of the shuttle is implicated in the protection against periplasmic H2O2 . An E...

## Biological Role

Catalyzes TRANS-RXN-290 (reaction.ecocyc.TRANS-RXN-290), TRANS-RXN-291 (reaction.ecocyc.TRANS-RXN-291), TRANS-RXN0-508 (reaction.ecocyc.TRANS-RXN0-508), TRANS-RXN0-513 (reaction.ecocyc.TRANS-RXN0-513), TRANS-RXN0-593 (reaction.ecocyc.TRANS-RXN0-593), TRANS-RXN0-617 (reaction.ecocyc.TRANS-RXN0-617). Transports L-Cystine (molecule.C00491), meso-2,6-Diaminoheptanedioate (molecule.C00680), L-Homocystine (molecule.C01817), lanthionine (molecule.ecocyc.CPD-3736), L-djenkolate (molecule.ecocyc.CPD-3740), D-cystine (molecule.ecocyc.CPD0-1564), hν (molecule.ecocyc.Light).

## Annotation

tcyJ, tcyL and tcyN encode proteins that constitute a cystine transporter complex in E. coli K-12. The complex is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters; TcyJ (formerly FliY) is the periplasmic binding protein and sequence analysis suggests that TcyN (formerly YecC) and TcyL (formerlyYecS) are the ATP binding subunit and integral membrane subunit respectively . TcyJLN functions to replenish cysteine pools in sulfur starved cells; TcyJLN is a high-affinity transporter that functions when cystine is scarce whereas a second cystine transporter, G6934-MONOMER "TcyP", is the primary transporter when cystine is abundant . Under aerobic growth conditions, E. coli imports cystine as an economical alternative to sulfate assimilation; E. coli lacks a dedicated cysteine importer and under anaerobic conditions when cysteine remains in the reduced form cells may assimilate sulfur from hydrogen sulfide . TcyJLN, G6934-MONOMER "TcyP" and the L-cysteine exporter EG11639 "EamA" participate in an L-cystine/L-cysteine shuttle system which is suggested to protect the cell membrane under oxidative stress conditions; L-cystine importers (TcyJLN and TcyP) cooperate with an L-cysteine exporter (EamA) to supply reducing equivalents to the periplasm; operation of the shuttle is implicated in the protection against periplasmic H2O2 . An E. coli ΔtcyJ ΔtcyP strain displays minimal (or no) L-cystine uptake and cannot grow using cystine as sole sulfur source . The complex is also able to transport D-cystine, djenkolic acid, lanthionine, diaminopimelic acid, homocystine (for use as a methionine precursor) and the toxic compounds L-selenaproline and L-selenocystine . tcyJ lies upstream, and separate from, tcyLN; tcyJ is expressed as a monocistronic transcript; expressio

## Outgoing Edges (13)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-290|reaction.ecocyc.TRANS-RXN-290]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-291|reaction.ecocyc.TRANS-RXN-291]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-508|reaction.ecocyc.TRANS-RXN0-508]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-513|reaction.ecocyc.TRANS-RXN0-513]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-593|reaction.ecocyc.TRANS-RXN0-593]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-617|reaction.ecocyc.TRANS-RXN0-617]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00491|molecule.C00491]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00680|molecule.C00680]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C01817|molecule.C01817]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-3736|molecule.ecocyc.CPD-3736]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-3740|molecule.ecocyc.CPD-3740]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD0-1564|molecule.ecocyc.CPD0-1564]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P0AEM9|protein.P0AEM9]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AFT2|protein.P0AFT2]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P37774|protein.P37774]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX0-8152`
- `QSPROTEOME:QS00049460`

## Notes

2*protein.P37774|2*protein.P0AFT2|1*protein.P0AEM9
