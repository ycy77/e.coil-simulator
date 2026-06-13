---
entity_id: "complex.ecocyc.ABC-6-CPLX"
entity_type: "complex"
name: "heme ABC transporter CydDC"
source_database: "EcoCyc"
source_id: "ABC-6-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# heme ABC transporter CydDC

`complex.ecocyc.ABC-6-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-6-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P29018|protein.P29018]], [[protein.P23886|protein.P23886]]

## Enriched Summary

CydDC is a heme transporter that is required for CYT-D-UBIOX-CPLX cytochrome bd-I and APP-UBIOX-CPLX cytochrome bd-II maturation; CydDC exports heme via a binding and flipping mechanism and a model of the transport cycle has been proposed . Sequence analysis suggests the cydDC genes encode the protein components of a transporter belonging to the ATP binding cassette (ABC) family of transporters . Both proteins have an N-terminal domain containing 6 transmembrane helices (linked by two large periplasmic loops and three small cytoplasmic loops) and a hydrophilic C-terminal domain containing an ATP binding site . The CydD and CydC proteins are 50% similar and 27% identical and the cydDC genes form an operon that is highly expressed when a functional aerobic or anaerobic respiratory chain is needed . Cryo-EM structures of nucleotide and substrate-free CydDC exhibit an asymmetrical structure with the defining features of a type IV ABC exporter; each subunit consists of 6 transmembrane helices, an N-terminal cytoplasmic helix lying parallel to the membrane and a cytoplasmic nucleotide-binding domain . CydC contains a canonical ATP hydrolysis site while CydD likely contains a degenerate nucleotide binding domain . CydDC is important for maintenance of the optimum redox balance in the periplasm...

## Biological Role

Catalyzes RXN0-21 (reaction.ecocyc.RXN0-21), RXN0-3 (reaction.ecocyc.RXN0-3), heme export (reaction.ecocyc.TRANS-RXN-1540). Transports Glutathione (molecule.C00051), L-Cysteine (molecule.C00097), hν (molecule.ecocyc.Light), protoheme (molecule.ecocyc.PROTOHEME).

## Annotation

CydDC is a heme transporter that is required for CYT-D-UBIOX-CPLX cytochrome bd-I and APP-UBIOX-CPLX cytochrome bd-II maturation; CydDC exports heme via a binding and flipping mechanism and a model of the transport cycle has been proposed . Sequence analysis suggests the cydDC genes encode the protein components of a transporter belonging to the ATP binding cassette (ABC) family of transporters . Both proteins have an N-terminal domain containing 6 transmembrane helices (linked by two large periplasmic loops and three small cytoplasmic loops) and a hydrophilic C-terminal domain containing an ATP binding site . The CydD and CydC proteins are 50% similar and 27% identical and the cydDC genes form an operon that is highly expressed when a functional aerobic or anaerobic respiratory chain is needed . Cryo-EM structures of nucleotide and substrate-free CydDC exhibit an asymmetrical structure with the defining features of a type IV ABC exporter; each subunit consists of 6 transmembrane helices, an N-terminal cytoplasmic helix lying parallel to the membrane and a cytoplasmic nucleotide-binding domain . CydC contains a canonical ATP hydrolysis site while CydD likely contains a degenerate nucleotide binding domain . CydDC is important for maintenance of the optimum redox balance in the periplasm . Periplasmic redox control is particularly important for heme ligation during cytochrome assembly: a cydD null mutant fails to synthesize periplasmic c-type cytochromes and lacks cytochromes d and b-595 ; the heme components of cytochrome bd cannot be detected in cydC null mutants . Purified CydDC has weak ATPase activity in solution and when reconstituted in liposomes; ATPase activity is stimulated by the presence of thiol (GSH and cysteine) and heme compounds; CydDC copurifies with ha

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.ecocyc.RXN0-21|reaction.ecocyc.RXN0-21]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-3|reaction.ecocyc.RXN0-3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-1540|reaction.ecocyc.TRANS-RXN-1540]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.PROTOHEME|molecule.ecocyc.PROTOHEME]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P23886|protein.P23886]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P29018|protein.P29018]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-6-CPLX`
- `QSPROTEOME:QS00049294`
- `PDB:7ZEC`
- `PDB:7ZE5`
- `PDB:7ZDW`
- `PDB:7ZDV`
- `PDB:7ZDU`
- `PDB:7ZDT`
- `PDB:7ZDS`
- `PDB:7ZDR`

## Notes

1*protein.P29018|1*protein.P23886
