---
entity_id: "complex.ecocyc.FABA-CPLX"
entity_type: "complex"
name: "β-hydroxyacyl-acyl carrier protein dehydratase/isomerase"
source_database: "EcoCyc"
source_id: "FABA-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "3-hydroxydecanoyl-[acp] dehydrase"
  - "3-hydroxyacyl-[acyl-carrier-protein] dehydratase FabA"
  - "&beta"
  - "-hydroxyacyl-ACP dehydratase/isomerase"
---

# β-hydroxyacyl-acyl carrier protein dehydratase/isomerase

`complex.ecocyc.FABA-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:FABA-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A6Q3|protein.P0A6Q3]]

## Enriched Summary

FabA is a dehydratase/isomerase that plays a specific and essential role in the synthesis of unsaturated fatty acids. It functions at the branch point between saturated and unsaturated fatty acid biosynthesis by introducing cis unsaturation (see pathway PWY0-862). It is responsible for shunting an intermediate in the biosynthetic pathway for saturated fatty acids, Trans-D2-decenoyl-ACPs, into unsaturated products (see below). In contrast to FabA, a second dehydratase encoded by EG11284 lacks isomerase activity and plays a general role in both saturated and unsaturated fatty acid biosynthesis . The bifunctional FabA catalyzes the dehydration of Beta-hydroxydecanoyl-ACPs to Trans-D2-decenoyl-ACPs (E-(2)-decenoyl-[acp]) and its isomeriaztion to Cis-delta-3-decenoyl-ACPs (Z-(3)-decenoyl-[acp]). During this reaction, enzyme-bound Trans-D2-decenoyl-ACPs is isomerized to Cis-delta-3-decenoyl-ACPs and the cis double bond is preserved during the subsequent rounds of elongation that ultimately produce the unsaturated fatty acids palmitoleate and cis-vaccenate (see pathways PWY-6282 and PWY-5973). Trans-D2-decenoyl-ACPs can also be released from the enzyme and utilized in the synthesis of saturated fatty acids (see pathway PWY-5971)...

## Biological Role

Catalyzes 3-HYDROXYDECANOYL-ACP-DEHYDR-RXN (reaction.ecocyc.3-HYDROXYDECANOYL-ACP-DEHYDR-RXN), 5.3.3.14-RXN (reaction.ecocyc.5.3.3.14-RXN), RXN-9655 (reaction.ecocyc.RXN-9655).

## Annotation

FabA is a dehydratase/isomerase that plays a specific and essential role in the synthesis of unsaturated fatty acids. It functions at the branch point between saturated and unsaturated fatty acid biosynthesis by introducing cis unsaturation (see pathway PWY0-862). It is responsible for shunting an intermediate in the biosynthetic pathway for saturated fatty acids, Trans-D2-decenoyl-ACPs, into unsaturated products (see below). In contrast to FabA, a second dehydratase encoded by EG11284 lacks isomerase activity and plays a general role in both saturated and unsaturated fatty acid biosynthesis . The bifunctional FabA catalyzes the dehydration of Beta-hydroxydecanoyl-ACPs to Trans-D2-decenoyl-ACPs (E-(2)-decenoyl-[acp]) and its isomeriaztion to Cis-delta-3-decenoyl-ACPs (Z-(3)-decenoyl-[acp]). During this reaction, enzyme-bound Trans-D2-decenoyl-ACPs is isomerized to Cis-delta-3-decenoyl-ACPs and the cis double bond is preserved during the subsequent rounds of elongation that ultimately produce the unsaturated fatty acids palmitoleate and cis-vaccenate (see pathways PWY-6282 and PWY-5973). Trans-D2-decenoyl-ACPs can also be released from the enzyme and utilized in the synthesis of saturated fatty acids (see pathway PWY-5971). The dehydratase activity of FabA catalyzes the dehydration of saturated β-hydroxyacyl-[acp] substrates and is most active on substrates of intermediate chain length. It prefers substrates with C10 aliphatic chains in vitro and does not use unsaturated substrates . Using a combination of structural, quantitative and computational analyses, the chain length-specific interactions between FabA and AcpP were evaluated, demonstrating how FabA maintains a control step favoring C10 substrates over C8 and C6 substrates bound to AcpP . A temperature-sensitive m

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.3-HYDROXYDECANOYL-ACP-DEHYDR-RXN|reaction.ecocyc.3-HYDROXYDECANOYL-ACP-DEHYDR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.5.3.3.14-RXN|reaction.ecocyc.5.3.3.14-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9655|reaction.ecocyc.RXN-9655]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A6Q3|protein.P0A6Q3]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:FABA-CPLX`
- `QSPROTEOME:QS00196921`

## Notes

2*protein.P0A6Q3
