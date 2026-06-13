---
entity_id: "complex.ecocyc.AIRS-CPLX"
entity_type: "complex"
name: "phosphoribosylformylglycinamide cyclo-ligase"
source_database: "EcoCyc"
source_id: "AIRS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# phosphoribosylformylglycinamide cyclo-ligase

`complex.ecocyc.AIRS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:AIRS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P08178|protein.P08178]]

## Enriched Summary

E. coli phosphoribosylformylglycinamidine cyclo-ligase (AIR synthetase) catalyzes the fifth step in the de novo purine biosynthesis pathway . It converts 5-phosphoribosyl-N-formylglycineamidine (FGAM) and ATP to 5-amino-1-(5-phospho-D-ribosyl)imidazole (AIR), ADP and phosphate. In this PurM catalyzed reaction, as with the PurL catalyzed reaction, ATP has been proposed to phosphorylate an amide oxygen, generating an intermediate that is activated for nucleophilic attack PurM uses the N-1 of FGAM to catalyze intramolecular ring formation, producing the imidazole ring . The kinetic mechanism was found to be sequential, in which ATP binds first and ADP is released last . Affinity labeling and site-directed mutagenesis studies were used to define the ATP binding site . The crystal structure of E. coli PurM has been determined at 2.5 Å resolution . Review: Jensen, K.F., G. Dandanell, B. Hove-Jensen, and M. Willemoes (2008) "Nucleotides, Nucleosides and Nucleobases" EcoSal 3.6.2 E. coli phosphoribosylformylglycinamidine cyclo-ligase (AIR synthetase) catalyzes the fifth step in the de novo purine biosynthesis pathway . It converts 5-phosphoribosyl-N-formylglycineamidine (FGAM) and ATP to 5-amino-1-(5-phospho-D-ribosyl)imidazole (AIR), ADP and phosphate...

## Biological Role

Catalyzes AIRS-RXN (reaction.ecocyc.AIRS-RXN). Bound by Potassium cation (molecule.C00238), Magnesium cation (molecule.C00305).

## Annotation

E. coli phosphoribosylformylglycinamidine cyclo-ligase (AIR synthetase) catalyzes the fifth step in the de novo purine biosynthesis pathway . It converts 5-phosphoribosyl-N-formylglycineamidine (FGAM) and ATP to 5-amino-1-(5-phospho-D-ribosyl)imidazole (AIR), ADP and phosphate. In this PurM catalyzed reaction, as with the PurL catalyzed reaction, ATP has been proposed to phosphorylate an amide oxygen, generating an intermediate that is activated for nucleophilic attack PurM uses the N-1 of FGAM to catalyze intramolecular ring formation, producing the imidazole ring . The kinetic mechanism was found to be sequential, in which ATP binds first and ADP is released last . Affinity labeling and site-directed mutagenesis studies were used to define the ATP binding site . The crystal structure of E. coli PurM has been determined at 2.5 Å resolution . Review: Jensen, K.F., G. Dandanell, B. Hove-Jensen, and M. Willemoes (2008) "Nucleotides, Nucleosides and Nucleobases" EcoSal 3.6.2

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.AIRS-RXN|reaction.ecocyc.AIRS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P08178|protein.P08178]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:AIRS-CPLX`
- `QSPROTEOME:QS00181697`

## Notes

2*protein.P08178
