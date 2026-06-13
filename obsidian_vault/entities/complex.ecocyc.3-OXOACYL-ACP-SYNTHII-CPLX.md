---
entity_id: "complex.ecocyc.3-OXOACYL-ACP-SYNTHII-CPLX"
entity_type: "complex"
name: "3-oxoacyl-[acyl carrier protein] synthase 2"
source_database: "EcoCyc"
source_id: "3-OXOACYL-ACP-SYNTHII-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "KASII"
---

# 3-oxoacyl-[acyl carrier protein] synthase 2

`complex.ecocyc.3-OXOACYL-ACP-SYNTHII-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:3-OXOACYL-ACP-SYNTHII-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AAI5|protein.P0AAI5]]

## Enriched Summary

There are three β-ketoacyl-[acyl carrier protein] synthases (KAS) in E. coli: FABB-CPLX KASI, KASII (FabF) and CPLX0-252 KASIII, encoded by EG10274 fabB, fabF and EG10277 fabH, respectively. All three are genetically and biochemically distinct. KASIII is involved in the initiation of fatty acid biosynthesis, while KASI and KASII are involved in the type II fatty acid elongation cycle. KAS enzymes use a common catalytic mechanism. The Claisen-type condensation reaction follows a two-step ping-pong process. First, the acyl cargo is transferred from the phosphopantetheinyl arm of the donor acyl-[acyl carrier protein] (acyl-ACP) to the active site cysteine of the KAS enzyme, forming a covalent bond. The donor holo-ACP is then replaced by the acceptor malonyl-ACP, and the acyl group is transferred from KAS to the malonyl group of the acceptor in a decarboxylating Claisen-type condensation reaction. Because the KAS enzyme interacts sequentially with two distinct ACPs, this reaction mechanism requires that the enzyme enforces temporal and structural discrimination between the donor and acceptor acyl-ACPs. Crystal structures of KAS in several catalytic states and analysis of mutants has now suggested that two conserved gating loops within the active site provide substrate specificity . FabF differs from FabB in that it can utilize CoA-linked acyl chains as the acyl donor...

## Biological Role

Catalyzes 2.3.1.179-RXN (reaction.ecocyc.2.3.1.179-RXN), 3-OXOACYL-ACP-SYNTH-BASE-RXN (reaction.ecocyc.3-OXOACYL-ACP-SYNTH-BASE-RXN), 3-OXOACYL-ACP-SYNTH-RXN (reaction.ecocyc.3-OXOACYL-ACP-SYNTH-RXN), RXN-11479 (reaction.ecocyc.RXN-11479).

## Annotation

There are three β-ketoacyl-[acyl carrier protein] synthases (KAS) in E. coli: FABB-CPLX KASI, KASII (FabF) and CPLX0-252 KASIII, encoded by EG10274 fabB, fabF and EG10277 fabH, respectively. All three are genetically and biochemically distinct. KASIII is involved in the initiation of fatty acid biosynthesis, while KASI and KASII are involved in the type II fatty acid elongation cycle. KAS enzymes use a common catalytic mechanism. The Claisen-type condensation reaction follows a two-step ping-pong process. First, the acyl cargo is transferred from the phosphopantetheinyl arm of the donor acyl-[acyl carrier protein] (acyl-ACP) to the active site cysteine of the KAS enzyme, forming a covalent bond. The donor holo-ACP is then replaced by the acceptor malonyl-ACP, and the acyl group is transferred from KAS to the malonyl group of the acceptor in a decarboxylating Claisen-type condensation reaction. Because the KAS enzyme interacts sequentially with two distinct ACPs, this reaction mechanism requires that the enzyme enforces temporal and structural discrimination between the donor and acceptor acyl-ACPs. Crystal structures of KAS in several catalytic states and analysis of mutants has now suggested that two conserved gating loops within the active site provide substrate specificity . FabF differs from FabB in that it can utilize CoA-linked acyl chains as the acyl donor . FabF is the only enzyme that can efficiently catalyze the conversion of Palmitoleoyl-ACPs palmitoleoyl-ACP to 3-oxo-cis-vaccenoyl-ACPs 3-keto-cis-vaccenoyl-ACP and is more active at low temperatures (relative to the overall rate of fatty acid synthesis) than at high temperatures. It thus plays a major role in the thermal regulation of fatty acid composition of the membrane phospholipids of E. coli . CPD-9245

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.2.3.1.179-RXN|reaction.ecocyc.2.3.1.179-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.3-OXOACYL-ACP-SYNTH-BASE-RXN|reaction.ecocyc.3-OXOACYL-ACP-SYNTH-BASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.3-OXOACYL-ACP-SYNTH-RXN|reaction.ecocyc.3-OXOACYL-ACP-SYNTH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-11479|reaction.ecocyc.RXN-11479]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AAI5|protein.P0AAI5]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:3-OXOACYL-ACP-SYNTHII-CPLX`
- `QSPROTEOME:QS00196195`

## Notes

2*protein.P0AAI5
