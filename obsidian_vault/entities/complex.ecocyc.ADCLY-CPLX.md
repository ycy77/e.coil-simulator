---
entity_id: "complex.ecocyc.ADCLY-CPLX"
entity_type: "complex"
name: "aminodeoxychorismate lyase"
source_database: "EcoCyc"
source_id: "ADCLY-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# aminodeoxychorismate lyase

`complex.ecocyc.ADCLY-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ADCLY-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P28305|protein.P28305]]

## Enriched Summary

Aminodeoxychorismate lyase (PabC) catalyzes the conversion of 4-amino-4-deoxychorismate to produce 4-aminobenzoate (p-aminobenzoate) in the PWY-6612 tetrahydrofolate biosynthesis pathway . Aminodeoxychorismate lyase belongs to the fold-type IV family of α,β-lyases. Its crystal structure has been determined at 2.2 Å resolution, and a reaction mechanism was proposed . The reaction involves the elimination of pyruvate from 4-amino-4-deoxychorismate with concomitant aromatization of the cyclohexadiene ring. The role of the pyridoxal 5'-phosphate cofactor has been studied . A pabC insertion mutant was reported to require 4-aminobenzoate for growth on minimal medium . Aminodeoxychorismate lyase (PabC) catalyzes the conversion of 4-amino-4-deoxychorismate to produce 4-aminobenzoate (p-aminobenzoate) in the PWY-6612 tetrahydrofolate biosynthesis pathway . Aminodeoxychorismate lyase belongs to the fold-type IV family of α,β-lyases. Its crystal structure has been determined at 2.2 Å resolution, and a reaction mechanism was proposed . The reaction involves the elimination of pyruvate from 4-amino-4-deoxychorismate with concomitant aromatization of the cyclohexadiene ring. The role of the pyridoxal 5'-phosphate cofactor has been studied . A pabC insertion mutant was reported to require 4-aminobenzoate for growth on minimal medium .

## Biological Role

Catalyzes ADCLY-RXN (reaction.ecocyc.ADCLY-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

Aminodeoxychorismate lyase (PabC) catalyzes the conversion of 4-amino-4-deoxychorismate to produce 4-aminobenzoate (p-aminobenzoate) in the PWY-6612 tetrahydrofolate biosynthesis pathway . Aminodeoxychorismate lyase belongs to the fold-type IV family of α,β-lyases. Its crystal structure has been determined at 2.2 Å resolution, and a reaction mechanism was proposed . The reaction involves the elimination of pyruvate from 4-amino-4-deoxychorismate with concomitant aromatization of the cyclohexadiene ring. The role of the pyridoxal 5'-phosphate cofactor has been studied . A pabC insertion mutant was reported to require 4-aminobenzoate for growth on minimal medium .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ADCLY-RXN|reaction.ecocyc.ADCLY-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P28305|protein.P28305]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ADCLY-CPLX`
- `QSPROTEOME:QS00180869`

## Notes

2*protein.P28305
