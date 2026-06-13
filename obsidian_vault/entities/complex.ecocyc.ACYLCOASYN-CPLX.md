---
entity_id: "complex.ecocyc.ACYLCOASYN-CPLX"
entity_type: "complex"
name: "long-chain-fatty-acid—CoA ligase"
source_database: "EcoCyc"
source_id: "ACYLCOASYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# long-chain-fatty-acid—CoA ligase

`complex.ecocyc.ACYLCOASYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ACYLCOASYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P69451|protein.P69451]]

## Enriched Summary

Long chain fatty acid CoA-ligase, also known as acyl-CoA synthetase or synthase, plays a pivotal role in the transport and activation of exogenous fatty acids prior to their subsequent degradation or incorporation into phospholipids. This is the rate limiting step of β-oxidation in E. coli . The enzyme catalyzes the esterification of fatty acids into metabolically active CoA thioesters concomitant with transport. The reaction proceeds by a two-step mechanism. Early experiments with partially purified enzyme suggested the presence of two enzymes with different preferences for substrate chain length (the other enzyme is likely the EG12357-MONOMER "medium-chain fatty acid:CoA ligase FadK"). FadD has broad chain length specificity with maximal activities associated with fatty acids ranging in length between C-12 and C-18 . Later experiments have shown that the enzyme has a broader substrate range than initially assumed. It is able to esterify not only even carbon number fatty acids (C6, C8, C12, C14 and C16), but also odd carbon number fatty acids (C9, C11 and C13). In addition, it can accept some phenylpropanoate derivatives such as CPD-674 and 3-PHENYLPROPIONATE . The enzyme was reported to be partially membrane-associated . It was later suggested that FadD specifically associates with the inner membrane in response to the presence of long chain fatty acids...

## Biological Role

Catalyzes RXN-19960 (reaction.ecocyc.RXN-19960), RXN0-7238 (reaction.ecocyc.RXN0-7238), RXN0-7239 (reaction.ecocyc.RXN0-7239), RXN0-7248 (reaction.ecocyc.RXN0-7248), TRANS-RXN0-623 (reaction.ecocyc.TRANS-RXN0-623). Bound by Magnesium cation (molecule.C00305).

## Annotation

Long chain fatty acid CoA-ligase, also known as acyl-CoA synthetase or synthase, plays a pivotal role in the transport and activation of exogenous fatty acids prior to their subsequent degradation or incorporation into phospholipids. This is the rate limiting step of β-oxidation in E. coli . The enzyme catalyzes the esterification of fatty acids into metabolically active CoA thioesters concomitant with transport. The reaction proceeds by a two-step mechanism. Early experiments with partially purified enzyme suggested the presence of two enzymes with different preferences for substrate chain length (the other enzyme is likely the EG12357-MONOMER "medium-chain fatty acid:CoA ligase FadK"). FadD has broad chain length specificity with maximal activities associated with fatty acids ranging in length between C-12 and C-18 . Later experiments have shown that the enzyme has a broader substrate range than initially assumed. It is able to esterify not only even carbon number fatty acids (C6, C8, C12, C14 and C16), but also odd carbon number fatty acids (C9, C11 and C13). In addition, it can accept some phenylpropanoate derivatives such as CPD-674 and 3-PHENYLPROPIONATE . The enzyme was reported to be partially membrane-associated . It was later suggested that FadD specifically associates with the inner membrane in response to the presence of long chain fatty acids . Long chain fatty acid uptake into inner membrane vesicles is dependent on the level of FadD in the vesicles . Import of labeled oleate is abolished in fadD null strains . Specific mutations in fadD that abolish or reduce the formation of fatty acyl-CoA likewise abolish or reduce the import of exogenous long chain fatty acids . FadD is implicated in a transenvelope lipid signaling pathway that detects phospholipid acc

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.RXN-19960|reaction.ecocyc.RXN-19960]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7238|reaction.ecocyc.RXN0-7238]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7239|reaction.ecocyc.RXN0-7239]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7248|reaction.ecocyc.RXN0-7248]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-623|reaction.ecocyc.TRANS-RXN0-623]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P69451|protein.P69451]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ACYLCOASYN-CPLX`
- `QSPROTEOME:QS00049345`

## Notes

2*protein.P69451
