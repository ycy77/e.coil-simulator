---
entity_id: "complex.ecocyc.SULFITE-REDUCT-CPLX"
entity_type: "complex"
name: "assimilatory sulfite reductase (NADPH)"
source_database: "EcoCyc"
source_id: "SULFITE-REDUCT-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# assimilatory sulfite reductase (NADPH)

`complex.ecocyc.SULFITE-REDUCT-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:SULFITE-REDUCT-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.CPLX0-7841|complex.ecocyc.CPLX0-7841]], [[protein.P17846|protein.P17846]]

## Enriched Summary

Sulfite reductase (NADPH) (SiR), an oligomeric oxidoreductase, catalyzes the 6-electron reduction of sulfite to sulfide, one of several activities necessary for the biosynthesis of cysteine from sulfate. The enzyme is a complex hemoflavoprotein, composed of two subunits with the structure α8β4, where the α subunit is the flavoprotein and the β subunit the hemoprotein . The enzyme is also able to catalyze the reduction of a variety of diaphorase acceptors. One of which, cytochrome c, may be identical to the reaction of E.C. number 1.6.2.5 . Sulfite reductase has been shown to have additional enzymatic activities. The enzyme can catalyze the reduction of various ferrisiderophores including ferric citrate, ferriaerobactin, ferrioxamin, ferricrocin, ferrichrome, ferrifusarinin and paraquat . It has been established that the enzyme also has flavin reductase activity using NADPH. The enzyme is able to reduce free riboflavin, FMN and FAD, with riboflavin being the better substrate . The α subunit, ALPHACOMP-MONOMER, binds two flavin prosthetic groups, one FAD and one FMN. FAD receives electrons from NADPH, while FMN transfers them to the hemoprotein component in the β subunit, BETACOMP-MONOMER. However, electrons can be transferred from FMN to other acceptors or from FAD directly to free flavins...

## Biological Role

Catalyzes SULFITE-REDUCT-RXN (reaction.ecocyc.SULFITE-REDUCT-RXN). Bound by FAD (molecule.C00016), FMN (molecule.C00061), Siroheme (molecule.C00748), a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

Sulfite reductase (NADPH) (SiR), an oligomeric oxidoreductase, catalyzes the 6-electron reduction of sulfite to sulfide, one of several activities necessary for the biosynthesis of cysteine from sulfate. The enzyme is a complex hemoflavoprotein, composed of two subunits with the structure α8β4, where the α subunit is the flavoprotein and the β subunit the hemoprotein . The enzyme is also able to catalyze the reduction of a variety of diaphorase acceptors. One of which, cytochrome c, may be identical to the reaction of E.C. number 1.6.2.5 . Sulfite reductase has been shown to have additional enzymatic activities. The enzyme can catalyze the reduction of various ferrisiderophores including ferric citrate, ferriaerobactin, ferrioxamin, ferricrocin, ferrichrome, ferrifusarinin and paraquat . It has been established that the enzyme also has flavin reductase activity using NADPH. The enzyme is able to reduce free riboflavin, FMN and FAD, with riboflavin being the better substrate . The α subunit, ALPHACOMP-MONOMER, binds two flavin prosthetic groups, one FAD and one FMN. FAD receives electrons from NADPH, while FMN transfers them to the hemoprotein component in the β subunit, BETACOMP-MONOMER. However, electrons can be transferred from FMN to other acceptors or from FAD directly to free flavins . Sulfite reductase can substitute for FMNREDUCT-MONOMER to regenerate the tyrosine radical in B2-CPLX that is essential for the activity of RIBONUCLEOSIDE-DIP-REDUCTI-CPLX .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.SULFITE-REDUCT-RXN|reaction.ecocyc.SULFITE-REDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (7)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00748|molecule.C00748]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[complex.ecocyc.CPLX0-7841|complex.ecocyc.CPLX0-7841]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P17846|protein.P17846]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4
- `is_component_of` <-- [[protein.P38038|protein.P38038]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=8

## External IDs

- `EcoCyc:SULFITE-REDUCT-CPLX`

## Notes

1*complex.ecocyc.CPLX0-7841|4*protein.P17846
