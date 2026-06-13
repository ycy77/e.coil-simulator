---
entity_id: "complex.ecocyc.CPLX0-7950"
entity_type: "complex"
name: "2-hydroxy-6-oxononatrienedioate hydrolase"
source_database: "EcoCyc"
source_id: "CPLX0-7950"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 2-hydroxy-6-oxononatrienedioate hydrolase

`complex.ecocyc.CPLX0-7950`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7950`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77044|protein.P77044]]

## Enriched Summary

2-hydroxy-6-oxononatrienedioate hydrolase (MhpC) catalyzes the hydrolysis of the ring fission product in the meta-cleavage pathway for the catabolism of 3-(3-hydroxyphenyl)propionate . The catalytic mechanism has been investigated. The first catalytic step appears to be a reversible keto-enol tautomerization, followed by a base-catalyzed attack of water forming a gem-diol intermediate . Analysis of site-directed mutant enzymes suggests that Ser110 activates the nucleophilic water molecule . Arg188 has a catalytic role in ketonization of the dienol substrate; Phe173 and Trp264 appear to be involved in substrate binding, while Asn109 is positioning the active site loop containing Ser110 . Esterase, thioesterase, and hydroxamate formation activities of the wild type and various mutant enzymes has been measured . A crystal structure of MhpC has been solved at 2.1 Å resolution . An mhpC mutant does not grow with m-hydroxyphenylpropionate (MHP) or 3-phenylpropionate as the sole source of carbon . 2-hydroxy-6-oxononatrienedioate hydrolase (MhpC) catalyzes the hydrolysis of the ring fission product in the meta-cleavage pathway for the catabolism of 3-(3-hydroxyphenyl)propionate . The catalytic mechanism has been investigated. The first catalytic step appears to be a reversible keto-enol tautomerization, followed by a base-catalyzed attack of water forming a gem-diol intermediate...

## Biological Role

Catalyzes MHPCHYDROL-RXN (reaction.ecocyc.MHPCHYDROL-RXN), RXN-12070 (reaction.ecocyc.RXN-12070).

## Annotation

2-hydroxy-6-oxononatrienedioate hydrolase (MhpC) catalyzes the hydrolysis of the ring fission product in the meta-cleavage pathway for the catabolism of 3-(3-hydroxyphenyl)propionate . The catalytic mechanism has been investigated. The first catalytic step appears to be a reversible keto-enol tautomerization, followed by a base-catalyzed attack of water forming a gem-diol intermediate . Analysis of site-directed mutant enzymes suggests that Ser110 activates the nucleophilic water molecule . Arg188 has a catalytic role in ketonization of the dienol substrate; Phe173 and Trp264 appear to be involved in substrate binding, while Asn109 is positioning the active site loop containing Ser110 . Esterase, thioesterase, and hydroxamate formation activities of the wild type and various mutant enzymes has been measured . A crystal structure of MhpC has been solved at 2.1 Å resolution . An mhpC mutant does not grow with m-hydroxyphenylpropionate (MHP) or 3-phenylpropionate as the sole source of carbon .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.MHPCHYDROL-RXN|reaction.ecocyc.MHPCHYDROL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-12070|reaction.ecocyc.RXN-12070]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P77044|protein.P77044]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7950`
- `QSPROTEOME:QS00182749`

## Notes

2*protein.P77044
