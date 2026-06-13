---
entity_id: "complex.ecocyc.ASPARTASE-CPLX"
entity_type: "complex"
name: "aspartate ammonia-lyase"
source_database: "EcoCyc"
source_id: "ASPARTASE-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# aspartate ammonia-lyase

`complex.ecocyc.ASPARTASE-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ASPARTASE-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AC38|protein.P0AC38]]

## Enriched Summary

Aspartate ammonia-lyase (aspartase, AspA) carries out the reversible conversion of L-aspartate to fumarate and ammonia . AspA is a member of the aspartase/fumarase superfamily that shares structural similarity and catalytic strategy . Most biochemical studies of AspA were done with enzyme isolated from either E. coli B or E. coli W; however, since their amino acid sequences appear to be 100% identical to that of AspA from E. coli K-12, the results of these studies are reported here as well. Both the amination and deamination reactions operate in a pH-dependent manner, gaining a dependence on the presence of a divalent metal ion as pH becomes more basic . Despite generating L-aspartate as its product, the amination of fumarate is activated by L-aspartate by dint of a lowered Km for fumarate . One metal ion binds per subunit, but to an activator site rather than the active site . AspA interacts with the phosphotransfer domain of PROTEIN-NRII NtrB and with the T-loop domain of PROTEIN-PII GlnB . Under nitrogen-limiting conditions, the L-aspartate deamination activity of AspA is stimulated by interaction with GlnB in the presence of ATP and 2-oxoglutarate; the fumarate amination activity of AspA is unaffected . The activity of AspA can be enhanced by carboxy-terminal cleavage . This enhancement has been examined in detail...

## Biological Role

Catalyzes ASPARTASE-RXN (reaction.ecocyc.ASPARTASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Aspartate ammonia-lyase (aspartase, AspA) carries out the reversible conversion of L-aspartate to fumarate and ammonia . AspA is a member of the aspartase/fumarase superfamily that shares structural similarity and catalytic strategy . Most biochemical studies of AspA were done with enzyme isolated from either E. coli B or E. coli W; however, since their amino acid sequences appear to be 100% identical to that of AspA from E. coli K-12, the results of these studies are reported here as well. Both the amination and deamination reactions operate in a pH-dependent manner, gaining a dependence on the presence of a divalent metal ion as pH becomes more basic . Despite generating L-aspartate as its product, the amination of fumarate is activated by L-aspartate by dint of a lowered Km for fumarate . One metal ion binds per subunit, but to an activator site rather than the active site . AspA interacts with the phosphotransfer domain of PROTEIN-NRII NtrB and with the T-loop domain of PROTEIN-PII GlnB . Under nitrogen-limiting conditions, the L-aspartate deamination activity of AspA is stimulated by interaction with GlnB in the presence of ATP and 2-oxoglutarate; the fumarate amination activity of AspA is unaffected . The activity of AspA can be enhanced by carboxy-terminal cleavage . This enhancement has been examined in detail . AspA is a homotetramer that appears to be arranged as a dimer of dimers . Though it has been reported that tetrameric structure is required for activity, other studies show that each subunit contributes separately to enzyme function and that isolated AspA dimers can have enzymatic activity . A crystal structure of AspA to 2.8 Å resolution shows that each AspA comprises three domains. The central domain contains five α helices that contribute to a twenty-

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ASPARTASE-RXN|reaction.ecocyc.ASPARTASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AC38|protein.P0AC38]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:ASPARTASE-CPLX`
- `QSPROTEOME:QS00181539`

## Notes

4*protein.P0AC38
