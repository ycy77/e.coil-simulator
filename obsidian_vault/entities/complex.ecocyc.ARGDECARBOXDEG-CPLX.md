---
entity_id: "complex.ecocyc.ARGDECARBOXDEG-CPLX"
entity_type: "complex"
name: "arginine decarboxylase, degradative"
source_database: "EcoCyc"
source_id: "ARGDECARBOXDEG-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# arginine decarboxylase, degradative

`complex.ecocyc.ARGDECARBOXDEG-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ARGDECARBOXDEG-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P28629|protein.P28629]]

## Enriched Summary

Escherichia coli contains two types of arginine decarboxylase. The biosynthetic form is expressed regardless of pH variations and is involved in the synthesis of polyamines. Arginine decarboxylase, degradative is induced in rich medium at a low pH in the presence of excess substrate under anaerobic conditions. It appears to play a role in pH homeostasis by consuming protons and neutralizing the acidic by-products produced during carbohydrate fermentation. The decarboxylase increases the surrounding pH by removing acidic carboxyl groups and releasing CO2 from their substrates . An adiA mutant was defective in arginine-dependent acid resistance . When cells are grown at pH 2.5 with arginine, the internal pH reaches 4.7 which reflects the pH optimum of the arginine decarboxylase . Expression of adiA is positively regulated by AdiY . Escherichia coli contains two types of arginine decarboxylase. The biosynthetic form is expressed regardless of pH variations and is involved in the synthesis of polyamines. Arginine decarboxylase, degradative is induced in rich medium at a low pH in the presence of excess substrate under anaerobic conditions. It appears to play a role in pH homeostasis by consuming protons and neutralizing the acidic by-products produced during carbohydrate fermentation...

## Biological Role

Catalyzes ARGDECARBOX-RXN (reaction.ecocyc.ARGDECARBOX-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

Escherichia coli contains two types of arginine decarboxylase. The biosynthetic form is expressed regardless of pH variations and is involved in the synthesis of polyamines. Arginine decarboxylase, degradative is induced in rich medium at a low pH in the presence of excess substrate under anaerobic conditions. It appears to play a role in pH homeostasis by consuming protons and neutralizing the acidic by-products produced during carbohydrate fermentation. The decarboxylase increases the surrounding pH by removing acidic carboxyl groups and releasing CO2 from their substrates . An adiA mutant was defective in arginine-dependent acid resistance . When cells are grown at pH 2.5 with arginine, the internal pH reaches 4.7 which reflects the pH optimum of the arginine decarboxylase . Expression of adiA is positively regulated by AdiY .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ARGDECARBOX-RXN|reaction.ecocyc.ARGDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P28629|protein.P28629]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## External IDs

- `EcoCyc:ARGDECARBOXDEG-CPLX`

## Notes

10*protein.P28629
