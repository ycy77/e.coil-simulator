---
entity_id: "complex.ecocyc.ABC-35-CPLX"
entity_type: "complex"
name: "CcmCDE complex"
source_database: "EcoCyc"
source_id: "ABC-35-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# CcmCDE complex

`complex.ecocyc.ABC-35-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-35-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0ABM1|protein.P0ABM1]], [[protein.P0ABM5|protein.P0ABM5]], [[protein.P69490|protein.P69490]]

## Enriched Summary

In E. coli K-12 the major proteins of a PWY-8147 "Type I cytochrome c biogenesis" pathway are encoded in a single operon (ccmABCDEFG). Numerous studies have examined the interaction between Ccm proteins; various complexes have been reported and the possibility of a large 'maturase' complex has also been considered (see ). The CcmCDE complex represented here is an intermediate complex of the pathway; it consists of the periplasmic heme chaperone CcmE, the heme-binding inner membrane protein CcmC and the small inner membrane protein CcmD. During cyctochrome c biosynthesis, heme is moved across the inner membrane concomitant with the formation of a CcmC-heme-CcmE-CcmD complex (CcmCDE-Complex-Heme "holo-CcmCDE"); subsequent release of holo-CcmE (for eventual heme transfer to apocytochromes c in the periplasm) requires CcmAB-Complex "CcmAB"-mediated ATP hydolysis (reviewed in ) Purification and characterization of the complexes of the Ccm pathway has helped elucidate the mechanisms of heme binding and trafficking. A stable (intermediate) holo-CcmCDE complex (isolated in the absence of CcmAB) contains oxidized heme (Fe3+) bound to CcmC via His-60 and His-184 axial ligands and to CcmE via a His-130 adduct; heme binding to CcmC is only detected when CcmE is present (see also ). In E...

## Biological Role

Catalyzes RXN-21407 (reaction.ecocyc.RXN-21407). Transports hν (molecule.ecocyc.Light), protoheme (molecule.ecocyc.PROTOHEME).

## Annotation

In E. coli K-12 the major proteins of a PWY-8147 "Type I cytochrome c biogenesis" pathway are encoded in a single operon (ccmABCDEFG). Numerous studies have examined the interaction between Ccm proteins; various complexes have been reported and the possibility of a large 'maturase' complex has also been considered (see ). The CcmCDE complex represented here is an intermediate complex of the pathway; it consists of the periplasmic heme chaperone CcmE, the heme-binding inner membrane protein CcmC and the small inner membrane protein CcmD. During cyctochrome c biosynthesis, heme is moved across the inner membrane concomitant with the formation of a CcmC-heme-CcmE-CcmD complex (CcmCDE-Complex-Heme "holo-CcmCDE"); subsequent release of holo-CcmE (for eventual heme transfer to apocytochromes c in the periplasm) requires CcmAB-Complex "CcmAB"-mediated ATP hydolysis (reviewed in ) Purification and characterization of the complexes of the Ccm pathway has helped elucidate the mechanisms of heme binding and trafficking. A stable (intermediate) holo-CcmCDE complex (isolated in the absence of CcmAB) contains oxidized heme (Fe3+) bound to CcmC via His-60 and His-184 axial ligands and to CcmE via a His-130 adduct; heme binding to CcmC is only detected when CcmE is present (see also ).

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-21407|reaction.ecocyc.RXN-21407]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.PROTOHEME|molecule.ecocyc.PROTOHEME]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P0ABM1|protein.P0ABM1]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0ABM5|protein.P0ABM5]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P69490|protein.P69490]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-35-CPLX`
- `PDB:7VFP`
- `PDB:7VFJ`
- `PDB:7F04`
- `PDB:7F03`
- `PDB:7F02`
- `QSPROTEOME:QS00195909`

## Notes

1*protein.P0ABM1|1*protein.P0ABM5|1*protein.P69490
