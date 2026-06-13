---
entity_id: "complex.ecocyc.ORNCARBAMTRANSFERF-CPLX"
entity_type: "complex"
name: "ornithine carbamoyltransferase"
source_database: "EcoCyc"
source_id: "ORNCARBAMTRANSFERF-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "OTCase-2"
---

# ornithine carbamoyltransferase

`complex.ecocyc.ORNCARBAMTRANSFERF-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ORNCARBAMTRANSFERF-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P06960|protein.P06960]]

## Enriched Summary

E. coli K-12 contains two structural genes, argF and argI, encoding ornithine carbamoyltransferase, both of which catalyze the sixth step of arginine biosynthesis. The active enzyme molecule is a trimer, and the products of the two genes become associated in a family of four isoenzymes, namely FFF, FFI, FII, and III. As compared to argI, argF might be the product of a relatively recent event of duplication or transposition in E. coli K-12 . Ornithine carbamoyltransferase catalyzes the synthesis of L-citrulline by transfer of the carbamoyl group from carbamoyl phosphate to L-ornithine. Zn2+ is a homotropic effector and an allosteric cofactor of ornithine transcarbamoylase . Arg57 of the enzyme is essential for the tight binding to carbamoyl phosphate and the productive binding to L-ornithine for efficient catalysis . A carbamoyl phosphate-induced isomerization of ornithine transcarbamoylase causes substrate binding to be ordered. It leads to a random substrate-binding pattern if Arg57 in the active site of the enzyme is replaced by a glycine . The enzyme follows an ordered Bi Bi mechanism with carbamoyl phosphate being the first substrate bound and L-citrulline being the first product released . Substrate binding order of this enzyme is dictated by the protonation state of Arg57...

## Biological Role

Catalyzes ORNCARBAMTRANSFER-RXN (reaction.ecocyc.ORNCARBAMTRANSFER-RXN).

## Annotation

E. coli K-12 contains two structural genes, argF and argI, encoding ornithine carbamoyltransferase, both of which catalyze the sixth step of arginine biosynthesis. The active enzyme molecule is a trimer, and the products of the two genes become associated in a family of four isoenzymes, namely FFF, FFI, FII, and III. As compared to argI, argF might be the product of a relatively recent event of duplication or transposition in E. coli K-12 . Ornithine carbamoyltransferase catalyzes the synthesis of L-citrulline by transfer of the carbamoyl group from carbamoyl phosphate to L-ornithine. Zn2+ is a homotropic effector and an allosteric cofactor of ornithine transcarbamoylase . Arg57 of the enzyme is essential for the tight binding to carbamoyl phosphate and the productive binding to L-ornithine for efficient catalysis . A carbamoyl phosphate-induced isomerization of ornithine transcarbamoylase causes substrate binding to be ordered. It leads to a random substrate-binding pattern if Arg57 in the active site of the enzyme is replaced by a glycine . The enzyme follows an ordered Bi Bi mechanism with carbamoyl phosphate being the first substrate bound and L-citrulline being the first product released . Substrate binding order of this enzyme is dictated by the protonation state of Arg57. The positive charge at Arg57 enhances the rate of carbamoyl phosphate binding, augments the turnover rate and controls the substrate binding order of carbamoylation. Carbamoyl phosphate-induced conformational change is the rate-limiting step of the enzymic reaction in the forward direction . The hydrogen-bonding interactions of carbamoyl phosphate to the enzyme reduce the rate of thermal decomposition of carbamoyl phosphate by a factor of >5,000 by preventing the C-O bond breakage . The crystal

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ORNCARBAMTRANSFER-RXN|reaction.ecocyc.ORNCARBAMTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P06960|protein.P06960]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:ORNCARBAMTRANSFERF-CPLX`
- `QSPROTEOME:QS00178321`

## Notes

3*protein.P06960
