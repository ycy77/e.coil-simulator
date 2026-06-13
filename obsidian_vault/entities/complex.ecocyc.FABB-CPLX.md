---
entity_id: "complex.ecocyc.FABB-CPLX"
entity_type: "complex"
name: "3-oxoacyl-[acyl carrier protein] synthase 1"
source_database: "EcoCyc"
source_id: "FABB-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "KASI"
---

# 3-oxoacyl-[acyl carrier protein] synthase 1

`complex.ecocyc.FABB-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:FABB-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A953|protein.P0A953]]

## Enriched Summary

There are three β-ketoacyl-[acyl carrier protein] synthases (KAS) in E. coli: KASI (FabB), 3-OXOACYL-ACP-SYNTHII-CPLX KASII and CPLX0-252 KASIII, encoded by fabB, EG12606 fabF and EG10277 fabH, respectively. All three are genetically and biochemically distinct. KASIII is involved in the initiation of fatty acid biosynthesis, while KASI and KASII are involved in the type II fatty acid elongation cycle. KAS enzymes use a common catalytic mechanism. The Claisen-type condensation reaction follows a two-step ping-pong process. First, the acyl cargo is transferred from the phosphopantetheinyl arm of the donor acyl-[acyl carrier protein] (acyl-ACP) to the active site cysteine of the KAS enzyme, forming a covalent bond. The donor holo-ACP is then replaced by the acceptor malonyl-ACP, and the acyl group is transferred from KAS to the malonyl group of the acceptor in a decarboxylating Claisen-type condensation reaction. Because the KAS enzyme interacts sequentially with two distinct ACPs, this reaction mechanism requires that the enzyme enforces temporal and structural discrimination between the donor and acceptor acyl-ACPs. Crystal structures of KAS in several catalytic states and analysis of mutants has suggested that two conserved gating loops within the active site provide substrate specificity and cooperative relationships between the two FabB monomers...

## Biological Role

Catalyzes 2.3.1.41-RXN (reaction.ecocyc.2.3.1.41-RXN), 3-OXOACYL-ACP-SYNTH-BASE-RXN (reaction.ecocyc.3-OXOACYL-ACP-SYNTH-BASE-RXN), 3-OXOACYL-ACP-SYNTH-RXN (reaction.ecocyc.3-OXOACYL-ACP-SYNTH-RXN), MALONYL-ACPDECARBOX-RXN (reaction.ecocyc.MALONYL-ACPDECARBOX-RXN), RXN-10654 (reaction.ecocyc.RXN-10654), RXN-10658 (reaction.ecocyc.RXN-10658), RXN-11479 (reaction.ecocyc.RXN-11479), 3-oxo-hexanoyl-[acyl-carrier protein] synthase (reaction.ecocyc.RXN-9516), and 6 more.

## Annotation

There are three β-ketoacyl-[acyl carrier protein] synthases (KAS) in E. coli: KASI (FabB), 3-OXOACYL-ACP-SYNTHII-CPLX KASII and CPLX0-252 KASIII, encoded by fabB, EG12606 fabF and EG10277 fabH, respectively. All three are genetically and biochemically distinct. KASIII is involved in the initiation of fatty acid biosynthesis, while KASI and KASII are involved in the type II fatty acid elongation cycle. KAS enzymes use a common catalytic mechanism. The Claisen-type condensation reaction follows a two-step ping-pong process. First, the acyl cargo is transferred from the phosphopantetheinyl arm of the donor acyl-[acyl carrier protein] (acyl-ACP) to the active site cysteine of the KAS enzyme, forming a covalent bond. The donor holo-ACP is then replaced by the acceptor malonyl-ACP, and the acyl group is transferred from KAS to the malonyl group of the acceptor in a decarboxylating Claisen-type condensation reaction. Because the KAS enzyme interacts sequentially with two distinct ACPs, this reaction mechanism requires that the enzyme enforces temporal and structural discrimination between the donor and acceptor acyl-ACPs. Crystal structures of KAS in several catalytic states and analysis of mutants has suggested that two conserved gating loops within the active site provide substrate specificity and cooperative relationships between the two FabB monomers . FabB differs from FabF in that it requires ACP as the acyl donor , and FabB alone is required for the elongation of short-chain unsaturated acyl-ACP. FabB can catalyze all the condensation reactions of long chain fatty acid synthesis except the elongation of pamitoleoyl-ACP, but has reduced activity towards substrates longer than 12 C atoms, whereas FabF efficiently catalyzes the elongation of saturated C14 and unsaturated C

## Outgoing Edges (14)

- `catalyzes` --> [[reaction.ecocyc.2.3.1.41-RXN|reaction.ecocyc.2.3.1.41-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.3-OXOACYL-ACP-SYNTH-BASE-RXN|reaction.ecocyc.3-OXOACYL-ACP-SYNTH-BASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.3-OXOACYL-ACP-SYNTH-RXN|reaction.ecocyc.3-OXOACYL-ACP-SYNTH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.MALONYL-ACPDECARBOX-RXN|reaction.ecocyc.MALONYL-ACPDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-10654|reaction.ecocyc.RXN-10654]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-10658|reaction.ecocyc.RXN-10658]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-11479|reaction.ecocyc.RXN-11479]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9516|reaction.ecocyc.RXN-9516]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9523|reaction.ecocyc.RXN-9523]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9527|reaction.ecocyc.RXN-9527]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9531|reaction.ecocyc.RXN-9531]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9535|reaction.ecocyc.RXN-9535]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9539|reaction.ecocyc.RXN-9539]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-2141|reaction.ecocyc.RXN0-2141]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A953|protein.P0A953]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:FABB-CPLX`
- `QSPROTEOME:QS00199067`

## Notes

2*protein.P0A953
