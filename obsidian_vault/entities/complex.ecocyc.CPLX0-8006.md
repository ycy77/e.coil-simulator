---
entity_id: "complex.ecocyc.CPLX0-8006"
entity_type: "complex"
name: "enoyl-[acyl-carrier-protein] reductase"
source_database: "EcoCyc"
source_id: "CPLX0-8006"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "enoyl-ACP reductase"
---

# enoyl-[acyl-carrier-protein] reductase

`complex.ecocyc.CPLX0-8006`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8006`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AEK4|protein.P0AEK4]]

## Enriched Summary

The FabI protein is an enoyl-acyl carrier protein reductase (enoyl-ACP reductase) that catalyzes an essential step in fatty acid biosynthesis, the reduction of the 2,3-double bond in the elongating fatty acid moiety . Enoyl-ACP reductase is inhibited by acyl-ACP, probably through product inhibition, thus regulating fatty acid synthesis at a significant point . More recent experiments with exogenous fatty acids found no evidence that FabI is directly inhibited by long-chain acyl-CoA in vivo despite previous in vitro experiments that used nonphysiological substrates (enoyl-acyl-CoA instead of enoyl-acyl-ACP). Instead, exogenous long-chain fatty acids lead to fatty acid synthesis inhibition due to acyl-CoA competition with acyl-ACP substrates, leading to acyl-ACP accumulation and feedback inhibition of PWY-4381 at ACETYL-COA-CARBOXYLTRANSFER-CPLX . FabI is the only enoyl-acyl carrier protein reductase in E. coli and is essential for growth . The enzyme is also involved in the elongation of 3-Ketoglutaryl-ACP-methyl-ester "3-ketoglutaryl-[acp]-methyl-ester" to Pimeloyl-ACP-methyl-esters "pimeloyl-[acp]-methyl-ester", part of the biotin biosynthesis pathway . The fabI gene (previously referred to as envM or qmeA) was identified, temperature-sensitive mutants were isolated, and its protein product was purified and characterized...

## Biological Role

Catalyzes 1.3.1.9-RXN (reaction.ecocyc.1.3.1.9-RXN), ENOYL-ACP-REDUCT-NADH-RXN (reaction.ecocyc.ENOYL-ACP-REDUCT-NADH-RXN), 2,3,4-saturated fatty acyl-[acp] dehydrogenase (reaction.ecocyc.ENOYL-ACP-REDUCT-NADPH-RXN), RXN-10657 (reaction.ecocyc.RXN-10657), RXN-10661 (reaction.ecocyc.RXN-10661), RXN-11478 (reaction.ecocyc.RXN-11478), RXN-11482 (reaction.ecocyc.RXN-11482), RXN-9558 (reaction.ecocyc.RXN-9558), and 8 more.

## Annotation

The FabI protein is an enoyl-acyl carrier protein reductase (enoyl-ACP reductase) that catalyzes an essential step in fatty acid biosynthesis, the reduction of the 2,3-double bond in the elongating fatty acid moiety . Enoyl-ACP reductase is inhibited by acyl-ACP, probably through product inhibition, thus regulating fatty acid synthesis at a significant point . More recent experiments with exogenous fatty acids found no evidence that FabI is directly inhibited by long-chain acyl-CoA in vivo despite previous in vitro experiments that used nonphysiological substrates (enoyl-acyl-CoA instead of enoyl-acyl-ACP). Instead, exogenous long-chain fatty acids lead to fatty acid synthesis inhibition due to acyl-CoA competition with acyl-ACP substrates, leading to acyl-ACP accumulation and feedback inhibition of PWY-4381 at ACETYL-COA-CARBOXYLTRANSFER-CPLX . FabI is the only enoyl-acyl carrier protein reductase in E. coli and is essential for growth . The enzyme is also involved in the elongation of 3-Ketoglutaryl-ACP-methyl-ester "3-ketoglutaryl-[acp]-methyl-ester" to Pimeloyl-ACP-methyl-esters "pimeloyl-[acp]-methyl-ester", part of the biotin biosynthesis pathway . The fabI gene (previously referred to as envM or qmeA) was identified, temperature-sensitive mutants were isolated, and its protein product was purified and characterized . Early work described two activities for enoyl-ACP reductase, one NADH-dependent and one NADPH-dependent, that catalyze the reduction of enoyl derivatives of carbon chain length from 4 to 16 . The latter activity was B-specific with respect to NADPH . However, it was later shown that both activities reside in FabI . The activity with NADH was over 17-fold higher than with NADPH , thus the designation of the E. coli enzyme as EC 1.3.1.9. The FabI prote

## Outgoing Edges (16)

- `catalyzes` --> [[reaction.ecocyc.1.3.1.9-RXN|reaction.ecocyc.1.3.1.9-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ENOYL-ACP-REDUCT-NADH-RXN|reaction.ecocyc.ENOYL-ACP-REDUCT-NADH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ENOYL-ACP-REDUCT-NADPH-RXN|reaction.ecocyc.ENOYL-ACP-REDUCT-NADPH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-10657|reaction.ecocyc.RXN-10657]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-10661|reaction.ecocyc.RXN-10661]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-11478|reaction.ecocyc.RXN-11478]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-11482|reaction.ecocyc.RXN-11482]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9558|reaction.ecocyc.RXN-9558]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9657|reaction.ecocyc.RXN-9657]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9658|reaction.ecocyc.RXN-9658]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9659|reaction.ecocyc.RXN-9659]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9660|reaction.ecocyc.RXN-9660]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9661|reaction.ecocyc.RXN-9661]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9662|reaction.ecocyc.RXN-9662]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9663|reaction.ecocyc.RXN-9663]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-2145|reaction.ecocyc.RXN0-2145]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AEK4|protein.P0AEK4]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-8006`
- `QSPROTEOME:QS00182745`

## Notes

4*protein.P0AEK4
