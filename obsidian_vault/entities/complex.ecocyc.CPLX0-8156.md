---
entity_id: "complex.ecocyc.CPLX0-8156"
entity_type: "complex"
name: "Xaa-Pro dipeptidase"
source_database: "EcoCyc"
source_id: "CPLX0-8156"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# Xaa-Pro dipeptidase

`complex.ecocyc.CPLX0-8156`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8156`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P21165|protein.P21165]]

## Enriched Summary

PepQ, a proline dipeptidase, hydrolyzes dipeptide substrates containing a proline residue at the carboxy-terminal end . A crystal structure of PepQ has been solved at 2 Å resolution. The C-terminal catalytic domain shows a pita-bread fold that is typical for this family of metalloproteases . pepQ mutants are resistant to the dipeptide L-valyl-L-proline . PepQ, a proline dipeptidase, hydrolyzes dipeptide substrates containing a proline residue at the carboxy-terminal end . A crystal structure of PepQ has been solved at 2 Å resolution. The C-terminal catalytic domain shows a pita-bread fold that is typical for this family of metalloproteases . pepQ mutants are resistant to the dipeptide L-valyl-L-proline .

## Biological Role

Catalyzes 3.4.13.9-RXN (reaction.ecocyc.3.4.13.9-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

PepQ, a proline dipeptidase, hydrolyzes dipeptide substrates containing a proline residue at the carboxy-terminal end . A crystal structure of PepQ has been solved at 2 Å resolution. The C-terminal catalytic domain shows a pita-bread fold that is typical for this family of metalloproteases . pepQ mutants are resistant to the dipeptide L-valyl-L-proline .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.4.13.9-RXN|reaction.ecocyc.3.4.13.9-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P21165|protein.P21165]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8156`
- `QSPROTEOME:QS00188921`

## Notes

2*protein.P21165
