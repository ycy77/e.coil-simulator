---
entity_id: "complex.ecocyc.HOMOSERKIN-CPLX"
entity_type: "complex"
name: "homoserine kinase"
source_database: "EcoCyc"
source_id: "HOMOSERKIN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# homoserine kinase

`complex.ecocyc.HOMOSERKIN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:HOMOSERKIN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P00547|protein.P00547]]

## Enriched Summary

Homoserine kinase (ThrB) catalyzes the phosphorylation of homoserine to O-phospho-L-homoserine en route to generating threonine . Though it is a substrate, homoserine can actually cause partial inhibition of the reaction at higher concentrations, with a Ki of ~2 mM . Substrate inhibition by high levels of ATP has also been observed . ThrB has been subject to kinetic and mechanistic analysis . The enzyme appears to have a second, regulatory binding site for L-homoserine . Site-directed mutagenesis has confirmed the role of Arg234 and the His residues H139 and H205 in substrate binding . ThrB is required for growth of pdxB mutants on glucose and 3-hydroxyhomoserine or D-glycolaldehyde . Later, thrB was identified as a multicopy suppressor of the PLP auxotrophy of a pdxB deletion strain. ThrB was found to be part of a serendipitous metabolic pathway that produces an intermediate of the PYRIDOXSYN-PWY pathway, 4-PHOSPHONOOXY-THREONINE, that lies downstream of PdxB . The 4-hydroxy-L-threonine kinase activity of ThrB that is required for this pathway had already been identified in vitro . The pathway diverts 3-phosphohydroxypyruvate from serine biosynthesis . A temperature-sensitive mutation in this gene was identified that showed potential as a growth-switch for genetic engineering . Translation of ThrA and ThrB is coupled...

## Biological Role

Catalyzes HOMOSERKIN-RXN (reaction.ecocyc.HOMOSERKIN-RXN), RXN0-6564 (reaction.ecocyc.RXN0-6564). Bound by Potassium cation (molecule.C00238), Magnesium cation (molecule.C00305).

## Annotation

Homoserine kinase (ThrB) catalyzes the phosphorylation of homoserine to O-phospho-L-homoserine en route to generating threonine . Though it is a substrate, homoserine can actually cause partial inhibition of the reaction at higher concentrations, with a Ki of ~2 mM . Substrate inhibition by high levels of ATP has also been observed . ThrB has been subject to kinetic and mechanistic analysis . The enzyme appears to have a second, regulatory binding site for L-homoserine . Site-directed mutagenesis has confirmed the role of Arg234 and the His residues H139 and H205 in substrate binding . ThrB is required for growth of pdxB mutants on glucose and 3-hydroxyhomoserine or D-glycolaldehyde . Later, thrB was identified as a multicopy suppressor of the PLP auxotrophy of a pdxB deletion strain. ThrB was found to be part of a serendipitous metabolic pathway that produces an intermediate of the PYRIDOXSYN-PWY pathway, 4-PHOSPHONOOXY-THREONINE, that lies downstream of PdxB . The 4-hydroxy-L-threonine kinase activity of ThrB that is required for this pathway had already been identified in vitro . The pathway diverts 3-phosphohydroxypyruvate from serine biosynthesis . A temperature-sensitive mutation in this gene was identified that showed potential as a growth-switch for genetic engineering . Translation of ThrA and ThrB is coupled .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.HOMOSERKIN-RXN|reaction.ecocyc.HOMOSERKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6564|reaction.ecocyc.RXN0-6564]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P00547|protein.P00547]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:HOMOSERKIN-CPLX`
- `QSPROTEOME:QS00049725`

## Notes

2*protein.P00547
