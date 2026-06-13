---
entity_id: "complex.ecocyc.ABC-10-CPLX"
entity_type: "complex"
name: "ferric enterobactin ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-10-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ferric enterobactin ABC transporter

`complex.ecocyc.ABC-10-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-10-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `regulatory`
- Components: [[protein.P23878|protein.P23878]], [[protein.P23876|protein.P23876]], [[protein.P23877|protein.P23877]], [[protein.P0AEL6|protein.P0AEL6]]

## Enriched Summary

FepBCDG are components of a ferric enterobactin transport complex that is a member of the ATP-binding cassette (ABC) family of transporters . FepD and FepG are the integral membrane subunits of the complex , FepC is the ATP-binding subunit and FepB is the periplasmic binding protein . When intracellular iron is limiting, E. coli K-12 and several other species of Enterobacteriaceae secrete the catecholate siderophore enterobactin - a small organic molecule with a high affinity for Fe 3+. Together with the TonB-dependent outer-membrane transporter, EG10293-MONOMER "FepA" , the FepBCDG complex forms a system responsible for the import of ferric enterobactin across the cell envelope. The subsequent mobilization of iron from ferric enterobactin requires hydrolysis of the siderophore scaffold and/or reduction of the coordinated ferric iron species (see ). Early studies characterised fep mutants (fepA and fepB) which were defective in the assimilation of iron from ferrienterochelin (ferric enterobactin) . Enterobactin is implicated in the protection against oxidative stress; strains with impaired enterobactin uptake show increased sensitivity to H2O2, paraquat, and copper compared to wild-type (see also ). fepDGC form an operon in E...

## Biological Role

Catalyzes ABC-10-RXN (reaction.ecocyc.ABC-10-RXN). Transports Fe-enterobactin (molecule.C06230), hν (molecule.ecocyc.Light).

## Annotation

FepBCDG are components of a ferric enterobactin transport complex that is a member of the ATP-binding cassette (ABC) family of transporters . FepD and FepG are the integral membrane subunits of the complex , FepC is the ATP-binding subunit and FepB is the periplasmic binding protein . When intracellular iron is limiting, E. coli K-12 and several other species of Enterobacteriaceae secrete the catecholate siderophore enterobactin - a small organic molecule with a high affinity for Fe 3+. Together with the TonB-dependent outer-membrane transporter, EG10293-MONOMER "FepA" , the FepBCDG complex forms a system responsible for the import of ferric enterobactin across the cell envelope. The subsequent mobilization of iron from ferric enterobactin requires hydrolysis of the siderophore scaffold and/or reduction of the coordinated ferric iron species (see ). Early studies characterised fep mutants (fepA and fepB) which were defective in the assimilation of iron from ferrienterochelin (ferric enterobactin) . Enterobactin is implicated in the protection against oxidative stress; strains with impaired enterobactin uptake show increased sensitivity to H2O2, paraquat, and copper compared to wild-type (see also ). fepDGC form an operon in E. coli K-12; fepDGC and fepB are not co-transcribed and are located within a cluster of genes that is reponsible for enterobactin synthesis and ferric entrerobactin transport . fepDGC and fepB are members of the CPLX0-7639 "Fur" regulon - under iron replete conditions their transcription is repressed by Fur-Fe2+; transcription is derepressed when intracellular iron is limiting . Related reviews:

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ABC-10-RXN|reaction.ecocyc.ABC-10-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C06230|molecule.C06230]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P0AEL6|protein.P0AEL6]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P23876|protein.P23876]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P23877|protein.P23877]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P23878|protein.P23878]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:ABC-10-CPLX`
- `QSPROTEOME:QS00185123`

## Notes

2*protein.P23878|1*protein.P23876|1*protein.P23877|1*protein.P0AEL6
