---
entity_id: "complex.ecocyc.ASPAMINOTRANS-DIMER"
entity_type: "complex"
name: "aspartate aminotransferase"
source_database: "EcoCyc"
source_id: "ASPAMINOTRANS-DIMER"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-CYTOSOL-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# aspartate aminotransferase

`complex.ecocyc.ASPAMINOTRANS-DIMER`

## Static

- Type: `complex`
- Source: `EcoCyc:ASPAMINOTRANS-DIMER`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-CYTOSOL-GN
- Complex type: `regulatory`
- Components: [[protein.P00509|protein.P00509]]

## Enriched Summary

Aspartate aminotransferase (AspC) is a multifunctional enzyme that catalyzes the synthesis of aspartate, phenylalanine, tyrosine and other compounds via a transamination reaction. AspC was reported to catalyze the synthesis of L-ASPARTATE, PHE, TYR and KYNURENATE . Studies with a ΔEG10372 Δ EG10403-EG10404 strain, which is not able to use GLT as an amine donor, showed that the presence of EG10096 enables the cells to use HIS, TYR, PHE, TRP, MET, ILE, and LEU as amine donors, demonstrating that AspC is even more versatile than previously reported . The reaction is catalyzed via a ping-pong Bi-Bi mechanism in which the cofactor alternates between the pyridoxal phosphate and pyridoxamine forms . An amino acid substrate binds via an aldimine bond to pyridoxal phosphate, after which a hydrogen atom is removed from the substrate. This deprotonation yields a quinonoid intermediate, which is followed by addition of a proton to the coenzyme and the formation of a ketimine intermediate. This intermediate is then hydrolyzed to form a keto acid substrate and the pyridoxamine form of the enzyme. This reaction mechanism has been studied extensively . AspC is catalytically active as a dimer . A crystal structure of AspC to 2.5 Å resolution showed that each of its subunits has a large and a small domain as well as one bound pyridoxal 5'-phosphate...

## Biological Role

Catalyzes ASPAMINOTRANS-RXN (reaction.ecocyc.ASPAMINOTRANS-RXN), CYSTEINE-AMINOTRANSFERASE-RXN (reaction.ecocyc.CYSTEINE-AMINOTRANSFERASE-RXN), RXN-10814 (reaction.ecocyc.RXN-10814), RXN-21858 (reaction.ecocyc.RXN-21858), TYROSINE-AMINOTRANSFERASE-RXN (reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

Aspartate aminotransferase (AspC) is a multifunctional enzyme that catalyzes the synthesis of aspartate, phenylalanine, tyrosine and other compounds via a transamination reaction. AspC was reported to catalyze the synthesis of L-ASPARTATE, PHE, TYR and KYNURENATE . Studies with a ΔEG10372 Δ EG10403-EG10404 strain, which is not able to use GLT as an amine donor, showed that the presence of EG10096 enables the cells to use HIS, TYR, PHE, TRP, MET, ILE, and LEU as amine donors, demonstrating that AspC is even more versatile than previously reported . The reaction is catalyzed via a ping-pong Bi-Bi mechanism in which the cofactor alternates between the pyridoxal phosphate and pyridoxamine forms . An amino acid substrate binds via an aldimine bond to pyridoxal phosphate, after which a hydrogen atom is removed from the substrate. This deprotonation yields a quinonoid intermediate, which is followed by addition of a proton to the coenzyme and the formation of a ketimine intermediate. This intermediate is then hydrolyzed to form a keto acid substrate and the pyridoxamine form of the enzyme. This reaction mechanism has been studied extensively . AspC is catalytically active as a dimer . A crystal structure of AspC to 2.5 Å resolution showed that each of its subunits has a large and a small domain as well as one bound pyridoxal 5'-phosphate . Many crystal structures have been generated for AspC and mutant variants of AspC, in both bound and unbound states, usually to resolutions in the 2-3 Å range . Crystal structures of AspC bound to inhibitors reveal that they operate by closing up the active site . In the case of maleate, this occurs after maleate itself occupies the active site . Structures of several cysteine mutants show that alteration of non-active-site residues can also

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.ASPAMINOTRANS-RXN|reaction.ecocyc.ASPAMINOTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.CYSTEINE-AMINOTRANSFERASE-RXN|reaction.ecocyc.CYSTEINE-AMINOTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-10814|reaction.ecocyc.RXN-10814]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-21858|reaction.ecocyc.RXN-21858]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN|reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P00509|protein.P00509]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ASPAMINOTRANS-DIMER`
- `QSPROTEOME:QS00188583`

## Notes

2*protein.P00509
