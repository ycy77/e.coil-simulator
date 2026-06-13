---
entity_id: "complex.ecocyc.CPLX0-8254"
entity_type: "complex"
name: "D-alanyl-D-alanine carboxypeptidase DacC"
source_database: "EcoCyc"
source_id: "CPLX0-8254"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# D-alanyl-D-alanine carboxypeptidase DacC

`complex.ecocyc.CPLX0-8254`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8254`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P08506|protein.P08506]]

## Enriched Summary

Penicillin-binding protein 6 (PBP6, also known as PBP6a), the product of the dacC gene, is a penicillin-sensitive, membrane-bound, putative D-alanyl D-alanine carboxypeptidase (DD-carboxypeptidase). The physiological role of the enzyme remains uncertain and there is contradictory evidence regarding DD-carboxpeptidase activity. In isogenic strains containing various combinations of PBPs, the presence of PBP6a is associated with an increased percentage of pentapeptide-containing muropeptides and a decreasd percentage of tetrapeptide-containing muropeptides . Early characterization of the protein purified from E. coli K-12 strain PA3092 indicated that PBP6 has D-alanine carboxypeptidase activity on various substrates including UDP-MurNAc-pentapeptide, alanine-labeled linear uncross-linked peptidoglycan and the model substrate diacetyl-lysyl-D-alanyl-D-alanine (see also ). The enzyme also catalysed an in vitro transpeptidation reaction using diacetyl-lysyl-D-alanyl-D-alanine as a donor and glycine as acceptor . In contrast, later work failed to detect DD-carboxypeptidase activity for both a membrane bound and a soluble PBP6 using UDP-muramyl-pentapeptide, diacetyl-lysyl-D-alanyl-D-alanine and other test substrates . PBP6 has a lower level of carboxypeptidase activity than PBP5 . DacC activity and stability increases at alkaline pH (pH 9...

## Biological Role

Catalyzes 3.4.17.8-RXN (reaction.ecocyc.3.4.17.8-RXN), RXN-16649 (reaction.ecocyc.RXN-16649), RXN-19249 (reaction.ecocyc.RXN-19249), RXN-19256 (reaction.ecocyc.RXN-19256).

## Annotation

Penicillin-binding protein 6 (PBP6, also known as PBP6a), the product of the dacC gene, is a penicillin-sensitive, membrane-bound, putative D-alanyl D-alanine carboxypeptidase (DD-carboxypeptidase). The physiological role of the enzyme remains uncertain and there is contradictory evidence regarding DD-carboxpeptidase activity. In isogenic strains containing various combinations of PBPs, the presence of PBP6a is associated with an increased percentage of pentapeptide-containing muropeptides and a decreasd percentage of tetrapeptide-containing muropeptides . Early characterization of the protein purified from E. coli K-12 strain PA3092 indicated that PBP6 has D-alanine carboxypeptidase activity on various substrates including UDP-MurNAc-pentapeptide, alanine-labeled linear uncross-linked peptidoglycan and the model substrate diacetyl-lysyl-D-alanyl-D-alanine (see also ). The enzyme also catalysed an in vitro transpeptidation reaction using diacetyl-lysyl-D-alanyl-D-alanine as a donor and glycine as acceptor . In contrast, later work failed to detect DD-carboxypeptidase activity for both a membrane bound and a soluble PBP6 using UDP-muramyl-pentapeptide, diacetyl-lysyl-D-alanyl-D-alanine and other test substrates . PBP6 has a lower level of carboxypeptidase activity than PBP5 . DacC activity and stability increases at alkaline pH (pH 9.0); DacC is required for normal morphology under alkaline stress (pH 9.0); DacC physically interacts with CPLX0-7717 PBP1a, CPLX0-3951 PBP1b, EG10606-MONOMER PBP2, and EG10341-MONOMER PBP3 . Purified PBP6 binds penicillin G ; purified PBP6 catalyses the release of bound penicillin . Soluble PBP6 (lacking its signal sequence and C-terminal membrane anchor) binds and releases penicillin less efficiently than soluble PBP5; soluble PBP6 binds th

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.3.4.17.8-RXN|reaction.ecocyc.3.4.17.8-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-16649|reaction.ecocyc.RXN-16649]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-19249|reaction.ecocyc.RXN-19249]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-19256|reaction.ecocyc.RXN-19256]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P08506|protein.P08506]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8254`
- `QSPROTEOME:QS00196917`

## Notes

2*protein.P08506
