---
entity_id: "complex.ecocyc.CPLX0-9871"
entity_type: "complex"
name: "PFL-GrcA complex"
source_database: "EcoCyc"
source_id: "CPLX0-9871"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# PFL-GrcA complex

`complex.ecocyc.CPLX0-9871`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-9871`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P68066|protein.P68066]], [[complex.ecocyc.PYRUVFORMLY-CPLX|complex.ecocyc.PYRUVFORMLY-CPLX]]

## Enriched Summary

The relatively stable glycyl radical of PYRUVFORMLY-CPLX pyruvate formate-lyase (PFL), which is essential for catalysis, is sensitive to OXYGEN-MOLECULE . Destruction of the glycyl radical by oxygen results in cleavage of the 85 kDa polypeptide to 83 kDa and a 3 kDa fragment and consequent inactivation of the enzyme . GrcA is a small (14 kDa) glycyl radical enzyme (GRE) that can restore activity of oxygen-damaged PYRUVFORMLY-CPLX pyruvate formate-lyase (PFL). GrcA forms a complex with the oxygen-damaged PFL enzyme and displaces the damaged C-terminal glycyl radical domain . After activation by PFLACTENZ-MONOMER (PflA), the PFL-GrcA complex has full pyruvate-formate lyase activity both in vitro and in vivo . In an arcA mutant under microaerobic conditions, GrcA contributes 18% of the flux through the pyruvate formate-lyase reaction . The relatively stable glycyl radical of PYRUVFORMLY-CPLX pyruvate formate-lyase (PFL), which is essential for catalysis, is sensitive to OXYGEN-MOLECULE . Destruction of the glycyl radical by oxygen results in cleavage of the 85 kDa polypeptide to 83 kDa and a 3 kDa fragment and consequent inactivation of the enzyme . GrcA is a small (14 kDa) glycyl radical enzyme (GRE) that can restore activity of oxygen-damaged PYRUVFORMLY-CPLX pyruvate formate-lyase (PFL)...

## Biological Role

Catalyzes KETOBUTFORMLY-RXN (reaction.ecocyc.KETOBUTFORMLY-RXN), PYRUVFORMLY-RXN (reaction.ecocyc.PYRUVFORMLY-RXN).

## Annotation

The relatively stable glycyl radical of PYRUVFORMLY-CPLX pyruvate formate-lyase (PFL), which is essential for catalysis, is sensitive to OXYGEN-MOLECULE . Destruction of the glycyl radical by oxygen results in cleavage of the 85 kDa polypeptide to 83 kDa and a 3 kDa fragment and consequent inactivation of the enzyme . GrcA is a small (14 kDa) glycyl radical enzyme (GRE) that can restore activity of oxygen-damaged PYRUVFORMLY-CPLX pyruvate formate-lyase (PFL). GrcA forms a complex with the oxygen-damaged PFL enzyme and displaces the damaged C-terminal glycyl radical domain . After activation by PFLACTENZ-MONOMER (PflA), the PFL-GrcA complex has full pyruvate-formate lyase activity both in vitro and in vivo . In an arcA mutant under microaerobic conditions, GrcA contributes 18% of the flux through the pyruvate formate-lyase reaction .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.KETOBUTFORMLY-RXN|reaction.ecocyc.KETOBUTFORMLY-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PYRUVFORMLY-RXN|reaction.ecocyc.PYRUVFORMLY-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `is_component_of` <-- [[complex.ecocyc.PYRUVFORMLY-CPLX|complex.ecocyc.PYRUVFORMLY-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P09373|protein.P09373]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P68066|protein.P68066]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-9871`

## Notes

protein.P68066|complex.ecocyc.PYRUVFORMLY-CPLX
