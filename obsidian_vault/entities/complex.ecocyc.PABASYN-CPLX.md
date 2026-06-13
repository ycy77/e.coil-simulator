---
entity_id: "complex.ecocyc.PABASYN-CPLX"
entity_type: "complex"
name: "4-amino-4-deoxychorismate synthase"
source_database: "EcoCyc"
source_id: "PABASYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "ADCS"
---

# 4-amino-4-deoxychorismate synthase

`complex.ecocyc.PABASYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PABASYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P05041|protein.P05041]], [[protein.P00903|protein.P00903]]

## Enriched Summary

PabA and PabB form a heterodimeric complex that catalyzes the conversion of chorismate and glutamine to 4-amino-4-deoxychorismate . PabA functions as a glutaminase, but only when in complex with PabB . PabB acts as a stoichiometric positive allosteric effector on the PabA subunit ; the presence of chorismate allosterically stimulates the glutaminase activity of PabA further . PabB is an aminodeoxychorismate synthase that utilizes chorismate and the nascent ammonia derived from glutamine hydrolysis by PabA as substrates . Both subreactions involve the formation of a covalently bound intermediate . A complex between PabA and PabB that was stable to gel filtration chromatography could initially not be demonstrated , although a later report found gel filtration conditions that demonstrated a complex . A homology model for the PabA-PabB complex was constructed. Alanine scanning mutagenesis revealed residues within an interdomain hydrogen bonding network that are important for PabA-PabB complex formation, residues that are important for allosteric signaling between the subunits, as well as residues involved in ammonia channeling from the PabA to the PabB active site . PabA and PabB were previously thought to be responsible for 4-aminobenzoate (para-aminobenzoate) synthesis in a single step...

## Biological Role

Catalyzes PABASYN-RXN (reaction.ecocyc.PABASYN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

PabA and PabB form a heterodimeric complex that catalyzes the conversion of chorismate and glutamine to 4-amino-4-deoxychorismate . PabA functions as a glutaminase, but only when in complex with PabB . PabB acts as a stoichiometric positive allosteric effector on the PabA subunit ; the presence of chorismate allosterically stimulates the glutaminase activity of PabA further . PabB is an aminodeoxychorismate synthase that utilizes chorismate and the nascent ammonia derived from glutamine hydrolysis by PabA as substrates . Both subreactions involve the formation of a covalently bound intermediate . A complex between PabA and PabB that was stable to gel filtration chromatography could initially not be demonstrated , although a later report found gel filtration conditions that demonstrated a complex . A homology model for the PabA-PabB complex was constructed. Alanine scanning mutagenesis revealed residues within an interdomain hydrogen bonding network that are important for PabA-PabB complex formation, residues that are important for allosteric signaling between the subunits, as well as residues involved in ammonia channeling from the PabA to the PabB active site . PabA and PabB were previously thought to be responsible for 4-aminobenzoate (para-aminobenzoate) synthesis in a single step . Later work revised this, showing that these gene products form a heterodimeric enzyme that catalyzes the formation of the intermediate 4-amino-4-deoxychorismate. A second enzyme, ADCLY-CPLX (PabC), catalyzes the conversion of this intermediate to 4-aminobenzoate (see pathway PWY-6543). PabA, PabB and PabC have been functionally described as three subunits of a 4-aminobenzoate (p-aminobenzoate) synthase multienzyme complex . Although no such complex has been isolated, the possibility of a

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PABASYN-RXN|reaction.ecocyc.PABASYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P00903|protein.P00903]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P05041|protein.P05041]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:PABASYN-CPLX`
- `QSPROTEOME:QS00170461`

## Notes

1*protein.P05041|1*protein.P00903
