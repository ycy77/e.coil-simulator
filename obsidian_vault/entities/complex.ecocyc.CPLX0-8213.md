---
entity_id: "complex.ecocyc.CPLX0-8213"
entity_type: "complex"
name: "periplasmic protein-L-methionine sulfoxide reducing system"
source_database: "EcoCyc"
source_id: "CPLX0-8213"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "quinol:protein L-methionine sulfoxide oxidoreductase"
---

# periplasmic protein-L-methionine sulfoxide reducing system

`complex.ecocyc.CPLX0-8213`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8213`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76343|protein.P76343]], [[protein.P76342|protein.P76342]]

## Enriched Summary

MsrP, a periplasmic methionine sulfoxide reductase and MsrQ, an inner membrane flavocytochrome, constitute a protein-L-methionine sulfoxide reducing system that functions to protect periplasmic proteins from oxidative damage in vivo. Unlike cytosolic methionine sulfoxide reductases, which rely on the thioredoxin system for reducing equivalents (see for example EG11433-MONOMER), the MsrPQ system uses electrons derived from the membrane quinone pool to reduce L-methionine sulfoxide residues . MsrQ may also receive electrons from the cytosolic NAD(P)H:flavin reductase FMNREDUCT-MONOMER Fre; in this pathway (which is not depicted here) Fre uses the MsrQ FMN cofactor as a substrate to catalyse reduction of the MsrQ heme in the presence of NADH . The MsrPQ system is induced during aerobic growth in the presence of copper where it functions to protect copper-trafficking proteins, including components of the CusCFBA efflux pump, from methionine oxidation . MsrPQ expression is regulated by the PWY0-1588 HprSR two-component system is in response to hypochlorous acid (HOCl) and related reactive chlorine species . Chlorate contamination in some commercial growth media activates the expression of msrPQ under anaerobic and low oxygen growth conditions...

## Biological Role

Catalyzes RXN-17652 (reaction.ecocyc.RXN-17652), RXN-17663 (reaction.ecocyc.RXN-17663). Bound by Molybdoenzyme molybdenum cofactor (molecule.C18237).

## Annotation

MsrP, a periplasmic methionine sulfoxide reductase and MsrQ, an inner membrane flavocytochrome, constitute a protein-L-methionine sulfoxide reducing system that functions to protect periplasmic proteins from oxidative damage in vivo. Unlike cytosolic methionine sulfoxide reductases, which rely on the thioredoxin system for reducing equivalents (see for example EG11433-MONOMER), the MsrPQ system uses electrons derived from the membrane quinone pool to reduce L-methionine sulfoxide residues . MsrQ may also receive electrons from the cytosolic NAD(P)H:flavin reductase FMNREDUCT-MONOMER Fre; in this pathway (which is not depicted here) Fre uses the MsrQ FMN cofactor as a substrate to catalyse reduction of the MsrQ heme in the presence of NADH . The MsrPQ system is induced during aerobic growth in the presence of copper where it functions to protect copper-trafficking proteins, including components of the CusCFBA efflux pump, from methionine oxidation . MsrPQ expression is regulated by the PWY0-1588 HprSR two-component system is in response to hypochlorous acid (HOCl) and related reactive chlorine species . Chlorate contamination in some commercial growth media activates the expression of msrPQ under anaerobic and low oxygen growth conditions . The formation of an MsrPQ complex has not been directly demonstrated; reports that an MsrP(C102S) mutant associates specifically with MsrQ in the cytoplasmic membrane and suggests that the subunits are likely coupled during catalysis in vivo.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-17652|reaction.ecocyc.RXN-17652]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17663|reaction.ecocyc.RXN-17663]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C18237|molecule.C18237]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P76342|protein.P76342]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P76343|protein.P76343]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-8213`
- `QSPROTEOME:QS00196881`

## Notes

1*protein.P76343|1*protein.P76342
