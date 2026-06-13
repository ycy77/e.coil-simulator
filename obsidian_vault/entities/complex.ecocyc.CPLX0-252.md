---
entity_id: "complex.ecocyc.CPLX0-252"
entity_type: "complex"
name: "3-oxoacyl-[acyl carrier protein] synthase 3"
source_database: "EcoCyc"
source_id: "CPLX0-252"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "KASIII"
---

# 3-oxoacyl-[acyl carrier protein] synthase 3

`complex.ecocyc.CPLX0-252`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-252`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6R0|protein.P0A6R0]]

## Enriched Summary

There are three β-ketoacyl-[acyl carrier protein] synthases (KAS) in E. coli: FABB-CPLX KASI, 3-OXOACYL-ACP-SYNTHII-CPLX KASII and KASIII (FabH), encoded by EG10274 fabB, EG12606 fabF and fabH, respectively. All three are genetically and biochemically distinct. KASIII is involved in the initiation of fatty acid biosynthesis, while KASI and KASII are involved in the type II fatty acid elongation cycle. KAS enzymes use a common catalytic mechanism. The Claisen-type condensation reaction follows a two-step ping-pong process. First, the acyl cargo is transferred from the phosphopantetheinyl arm of the donor acyl-[acyl carrier protein] (acyl-ACP) to the active site cysteine of the KAS enzyme, forming a covalent bond. The donor holo-ACP is then replaced by the acceptor malonyl-ACP, and the acyl group is transferred from KAS to the malonyl group of the acceptor in a decarboxylating Claisen-type condensation reaction. Because the KAS enzyme interacts sequentially with two distinct ACPs, this reaction mechanism requires that the enzyme enforces temporal and structural discrimination between the donor and acceptor acyl-ACPs. Crystal structures of KAS in several catalytic states and analysis of mutants has now suggested that two conserved gating loops within the active site provide substrate specificity . FabH is a key enzyme in the initiation of fatty acids biosynthesis...

## Biological Role

Catalyzes 2.3.1.180-RXN (reaction.ecocyc.2.3.1.180-RXN), ACP-S-ACETYLTRANSFER-RXN (reaction.ecocyc.ACP-S-ACETYLTRANSFER-RXN).

## Annotation

There are three β-ketoacyl-[acyl carrier protein] synthases (KAS) in E. coli: FABB-CPLX KASI, 3-OXOACYL-ACP-SYNTHII-CPLX KASII and KASIII (FabH), encoded by EG10274 fabB, EG12606 fabF and fabH, respectively. All three are genetically and biochemically distinct. KASIII is involved in the initiation of fatty acid biosynthesis, while KASI and KASII are involved in the type II fatty acid elongation cycle. KAS enzymes use a common catalytic mechanism. The Claisen-type condensation reaction follows a two-step ping-pong process. First, the acyl cargo is transferred from the phosphopantetheinyl arm of the donor acyl-[acyl carrier protein] (acyl-ACP) to the active site cysteine of the KAS enzyme, forming a covalent bond. The donor holo-ACP is then replaced by the acceptor malonyl-ACP, and the acyl group is transferred from KAS to the malonyl group of the acceptor in a decarboxylating Claisen-type condensation reaction. Because the KAS enzyme interacts sequentially with two distinct ACPs, this reaction mechanism requires that the enzyme enforces temporal and structural discrimination between the donor and acceptor acyl-ACPs. Crystal structures of KAS in several catalytic states and analysis of mutants has now suggested that two conserved gating loops within the active site provide substrate specificity . FabH is a key enzyme in the initiation of fatty acids biosynthesis. It selectively catalyzes the formation of acetoacetyl-ACP and specifically uses CoA thioesters rather than acyl-ACP as the primer. The enzyme is not active with oxa/aza(dethia)CoA analogues of acetyl-CoA . The enzyme's products tend to be shorter than the products of KASI and II, which are involved primarily in elongation reactions. Unlike the other two enzymes, KASIII cannot participate in the terminal elongatio

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.2.3.1.180-RXN|reaction.ecocyc.2.3.1.180-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ACP-S-ACETYLTRANSFER-RXN|reaction.ecocyc.ACP-S-ACETYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A6R0|protein.P0A6R0]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-252`
- `QSPROTEOME:QS00157333`

## Notes

2*protein.P0A6R0
