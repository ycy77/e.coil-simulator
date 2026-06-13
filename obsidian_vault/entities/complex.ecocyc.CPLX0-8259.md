---
entity_id: "complex.ecocyc.CPLX0-8259"
entity_type: "complex"
name: "6-hydroxyaminopurine reductase"
source_database: "EcoCyc"
source_id: "CPLX0-8259"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 6-hydroxyaminopurine reductase

`complex.ecocyc.CPLX0-8259`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8259`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P32157|protein.P32157]]

## Enriched Summary

YiiM belongs to the sulfite oxidase family of molybdenum cofactor enzymes and catalyzes the reduction of N-hydroxylated compounds such as 6-hydroxyaminopurine . Early experiments showed that YiiM functions in the molybdenum cofactor-dependent pathway for detoxification of N-hydroxylated base analogs . The FMNREDUCT-MONOMER Fre flavin reductase is hypothesized to be the electron donor for YiiM (Kozmin et al., unpublished; noted in ). YiiM contains an N-terminal MOSC (MoCo sulfurase C-terminal) domain and a C-terminal helical domain . Crystal structures of YiiM have been solved at 2.3, 2.5, and 2.85 Å resolution . YiiM is not involved in biosynthesis of the molybdenum cofactor . The cofactor used by the enzyme appears to be the GMP-free CPD-15870 rather than CPD-582 . A yiiM mutant shows increased sensitivity to the mutagenic effects of 2-amino-6-N-hydroxylaminopurine (AHAP) and hydroxylamine . Using an electrochemical method that includes an electrode coated with purified EG11870-MONOMER, an array of N-hydroxylated compounds were tested at a range of pH values. Little to no reductive activity was found for amine-oxides or sulfoxides, but hydroxylamines, amidoximes, N-hydroxypurines and N-hydroxyureas were preferred at a pH optimum of 7.1 with pKa values of 6.2 and 8.1 , very similar to another Mo-dependent enzyme, G6487-MONOMER YcbX...

## Biological Role

Catalyzes RXN0-7398 (reaction.ecocyc.RXN0-7398). Bound by Molybdoenzyme molybdenum cofactor (molecule.C18237).

## Annotation

YiiM belongs to the sulfite oxidase family of molybdenum cofactor enzymes and catalyzes the reduction of N-hydroxylated compounds such as 6-hydroxyaminopurine . Early experiments showed that YiiM functions in the molybdenum cofactor-dependent pathway for detoxification of N-hydroxylated base analogs . The FMNREDUCT-MONOMER Fre flavin reductase is hypothesized to be the electron donor for YiiM (Kozmin et al., unpublished; noted in ). YiiM contains an N-terminal MOSC (MoCo sulfurase C-terminal) domain and a C-terminal helical domain . Crystal structures of YiiM have been solved at 2.3, 2.5, and 2.85 Å resolution . YiiM is not involved in biosynthesis of the molybdenum cofactor . The cofactor used by the enzyme appears to be the GMP-free CPD-15870 rather than CPD-582 . A yiiM mutant shows increased sensitivity to the mutagenic effects of 2-amino-6-N-hydroxylaminopurine (AHAP) and hydroxylamine . Using an electrochemical method that includes an electrode coated with purified EG11870-MONOMER, an array of N-hydroxylated compounds were tested at a range of pH values. Little to no reductive activity was found for amine-oxides or sulfoxides, but hydroxylamines, amidoximes, N-hydroxypurines and N-hydroxyureas were preferred at a pH optimum of 7.1 with pKa values of 6.2 and 8.1 , very similar to another Mo-dependent enzyme, G6487-MONOMER YcbX .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7398|reaction.ecocyc.RXN0-7398]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C18237|molecule.C18237]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P32157|protein.P32157]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8259`
- `QSPROTEOME:QS00191677`

## Notes

2*protein.P32157
