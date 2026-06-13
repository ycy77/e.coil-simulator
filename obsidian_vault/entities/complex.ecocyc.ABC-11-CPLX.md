---
entity_id: "complex.ecocyc.ABC-11-CPLX"
entity_type: "complex"
name: "Fe(3+) hydroxamate ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-11-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# Fe(3+) hydroxamate ABC transporter

`complex.ecocyc.ABC-11-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-11-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P07821|protein.P07821]], [[protein.P06972|protein.P06972]], [[protein.P07822|protein.P07822]]

## Enriched Summary

FhuCDB is an ATP dependent, high-affinity transport system for the uptake of iron(III)-hydroxamate compounds such as ferrichrome and ferric coprogen. In the presence of oxygen, the essential nutrient Fe3+ is typically sequestered in insoluble iron oxyhydroxide polymers. Siderophores, including hydroxamate compounds, compete effectively with hydroxyl ions for Fe3+ (see ) and in E. coli K-12, iron(III) hydroxamate transport across the outer membrane (via the TonB dependent FhuA or FhuE proteins), coupled with FhuCDB-mediated iron(III) hydroxamate transport across the cytoplasmic membrane functions to supply the cell with this abundant but essentially unavailable nutrient. FhuCDB is a member of the ATP-Binding Cassette (ABC) superfamily of transporters. Early studies characterized fhuB mutants which were resistant to albomycin (a ferric hydroxamate antibiotic) and defective in the uptake of other ferric hydroxamate compounds such as ferrichrome and ferric coprogen . Further analysis resulted in the identification of three loci - fhuC, fhuD and fhuB which encode the protein components of an iron(III)-hydroxamate transport system: nucleotide sequence suggests that FhuC is an ATP-binding peripheral membrane protein; FhuD a periplasmic binding protein and FhuB an integral membrane protein...

## Biological Role

Catalyzes ABC-11-RXN (reaction.ecocyc.ABC-11-RXN), TRANS-RXN-297 (reaction.ecocyc.TRANS-RXN-297), TRANS-RXN-298 (reaction.ecocyc.TRANS-RXN-298). Transports ferrichrome (molecule.ecocyc.CPD0-2241), iron(III)-coprogen (molecule.ecocyc.CPD0-621), a ferric hydroxamate complex (molecule.ecocyc.Ferric-Hydroxamate-Complexes), hν (molecule.ecocyc.Light).

## Annotation

FhuCDB is an ATP dependent, high-affinity transport system for the uptake of iron(III)-hydroxamate compounds such as ferrichrome and ferric coprogen. In the presence of oxygen, the essential nutrient Fe3+ is typically sequestered in insoluble iron oxyhydroxide polymers. Siderophores, including hydroxamate compounds, compete effectively with hydroxyl ions for Fe3+ (see ) and in E. coli K-12, iron(III) hydroxamate transport across the outer membrane (via the TonB dependent FhuA or FhuE proteins), coupled with FhuCDB-mediated iron(III) hydroxamate transport across the cytoplasmic membrane functions to supply the cell with this abundant but essentially unavailable nutrient. FhuCDB is a member of the ATP-Binding Cassette (ABC) superfamily of transporters. Early studies characterized fhuB mutants which were resistant to albomycin (a ferric hydroxamate antibiotic) and defective in the uptake of other ferric hydroxamate compounds such as ferrichrome and ferric coprogen . Further analysis resulted in the identification of three loci - fhuC, fhuD and fhuB which encode the protein components of an iron(III)-hydroxamate transport system: nucleotide sequence suggests that FhuC is an ATP-binding peripheral membrane protein; FhuD a periplasmic binding protein and FhuB an integral membrane protein . FhuB mediates association of FhuC with the membrane: overexpression of fhuC results in random distribution of FhuC in the cytoplasm; simultaneous overexpression of fhuC and fhuB results in a preferential association of FhuC with the cytoplasmic membrane . A 3.4 Å-resolution cryo-electron microscopy structure of FhuCDB in the inward-open conformation has been determined . A ΔfhuACDB strain (also carrying an aroB mutation to block synthesis of enterobactin) is resistant to to the antibiotic,

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.ecocyc.ABC-11-RXN|reaction.ecocyc.ABC-11-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-297|reaction.ecocyc.TRANS-RXN-297]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-298|reaction.ecocyc.TRANS-RXN-298]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.CPD0-2241|molecule.ecocyc.CPD0-2241]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD0-621|molecule.ecocyc.CPD0-621]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Ferric-Hydroxamate-Complexes|molecule.ecocyc.Ferric-Hydroxamate-Complexes]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P06972|protein.P06972]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P07821|protein.P07821]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P07822|protein.P07822]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-11-CPLX`
- `PDB:7LB8`
- `PDB:7LB8`
- `QSPROTEOME:QS00049299`

## Notes

2*protein.P07821|1*protein.P06972|1*protein.P07822
