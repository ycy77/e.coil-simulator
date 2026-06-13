---
entity_id: "complex.ecocyc.CPLX0-8252"
entity_type: "complex"
name: "D-alanyl-D-alanine carboxypeptidase DacA"
source_database: "EcoCyc"
source_id: "CPLX0-8252"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# D-alanyl-D-alanine carboxypeptidase DacA

`complex.ecocyc.CPLX0-8252`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8252`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AEB2|protein.P0AEB2]]

## Enriched Summary

Penicillin-binding protein 5 (PBP5) , the product of the dacA gene, is a penicillin-sensitive, membrane-bound D-alanyl D-alanine carboxypeptidase (DD-carboxypeptidase) which cleaves the carboxy-terminal D-alanine from peptidoglycan pentapeptides. PBP5 activity regulates the amount of pentapetide substrate available to peptidoglycan transpeptidases and is implicated in the maintenance of cell shape; it is also responsible for intrinsic β-lactam resistance in E. coli K-12. Purified PBP5 has D-alanine carboxypeptidase activity on various substrates including alanine-labeled linear, uncross-linked peptidoglycan, UDP-MurNAc-pentapeptide and synthetic peptidoglycan substrates . The enzyme also catalyses an in vitro transpeptidation reaction using diacetyl-L-lysyl-D-alanyl-D-alanine as a donor and glycine as acceptor . PBP5 catalyses the major D-alanine carboxypeptidase activity in wild-type cells . Purified PBP5 binds penicillin G , penicillin V, cloxacillin, cefoxitin, moxalactam, and imipenem . PBP5 binds 35S-labeled penicillin from pH 4 through to 11 with a maximum at pH 10 . PBP5 is capable of hydrolysing bound penicillin and functions as a weak β-lactamase (penicillinase) . PBP5 catalysed DD-carboxypeptidase actvity (using a soluble truncated enzyme with diacetyl-L-Lys-D-Ala-D-Ala as substrate) has a pH optimum between 9 and 10...

## Biological Role

Catalyzes 3.4.17.8-RXN (reaction.ecocyc.3.4.17.8-RXN), BETA-LACTAMASE-RXN (reaction.ecocyc.BETA-LACTAMASE-RXN), RXN-16649 (reaction.ecocyc.RXN-16649), RXN-19249 (reaction.ecocyc.RXN-19249), RXN-19253 (reaction.ecocyc.RXN-19253).

## Annotation

Penicillin-binding protein 5 (PBP5) , the product of the dacA gene, is a penicillin-sensitive, membrane-bound D-alanyl D-alanine carboxypeptidase (DD-carboxypeptidase) which cleaves the carboxy-terminal D-alanine from peptidoglycan pentapeptides. PBP5 activity regulates the amount of pentapetide substrate available to peptidoglycan transpeptidases and is implicated in the maintenance of cell shape; it is also responsible for intrinsic β-lactam resistance in E. coli K-12. Purified PBP5 has D-alanine carboxypeptidase activity on various substrates including alanine-labeled linear, uncross-linked peptidoglycan, UDP-MurNAc-pentapeptide and synthetic peptidoglycan substrates . The enzyme also catalyses an in vitro transpeptidation reaction using diacetyl-L-lysyl-D-alanyl-D-alanine as a donor and glycine as acceptor . PBP5 catalyses the major D-alanine carboxypeptidase activity in wild-type cells . Purified PBP5 binds penicillin G , penicillin V, cloxacillin, cefoxitin, moxalactam, and imipenem . PBP5 binds 35S-labeled penicillin from pH 4 through to 11 with a maximum at pH 10 . PBP5 is capable of hydrolysing bound penicillin and functions as a weak β-lactamase (penicillinase) . PBP5 catalysed DD-carboxypeptidase actvity (using a soluble truncated enzyme with diacetyl-L-Lys-D-Ala-D-Ala as substrate) has a pH optimum between 9 and 10 . Specificity (of the soluble enzyme lacking its membrane anchor) for the stem peptide of E. coli peptidoglycan has been studied - PBP5 does not show high reactivity or specificity towards model peptides or peptidoglycan mimetics (and ). PBP5 lacking its membrane anchor and full-length PBP5 are both active against a range of substrates including high molecular mass peptidoglycan, its soluble degradation products and peptidoglycan precursors . PBP5

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.3.4.17.8-RXN|reaction.ecocyc.3.4.17.8-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.BETA-LACTAMASE-RXN|reaction.ecocyc.BETA-LACTAMASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-16649|reaction.ecocyc.RXN-16649]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-19249|reaction.ecocyc.RXN-19249]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-19253|reaction.ecocyc.RXN-19253]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AEB2|protein.P0AEB2]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8252`
- `QSPROTEOME:QS00196983`

## Notes

2*protein.P0AEB2
