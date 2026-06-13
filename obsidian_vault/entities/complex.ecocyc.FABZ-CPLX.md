---
entity_id: "complex.ecocyc.FABZ-CPLX"
entity_type: "complex"
name: "3-hydroxy-acyl-[acyl-carrier-protein] dehydratase"
source_database: "EcoCyc"
source_id: "FABZ-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "(3R)-hydroxymyristoyl-ACP dehydratase"
  - "(3R)-hydroxymyristoyl-(acyl-carrier-protein) dehydratase"
---

# 3-hydroxy-acyl-[acyl-carrier-protein] dehydratase

`complex.ecocyc.FABZ-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:FABZ-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6Q6|protein.P0A6Q6]]

## Enriched Summary

There are two β-hydroxyacyl-ACP dehydratases in E. coli, coded for by the EG10273 and EG11284 genes. They both function in the dissociated or type II fatty acid synthase systems. The FabZ enzyme has a very broad substrate specificity. It catalyzes the dehydration of short chain β-hydroxyacyl-ACPs and long chain saturated and unsaturated β-hydroxyacyl-ACPs. While the FabA enzyme is most active on intermediate chain lengths, the two dehydratases do possess broad overlapping substrate specificities. It is thought that the FabZ enzyme is the primary dehydratase involved in the unsaturated branch of the fatty acid synthesis pathway . Certain mutations in fabZ have been found as suppressor mutations; its sabA1 allele changes the suppression of the OmpF315 phenotype by asmB1, and increased fabZ expression suppresses OmpF315 itself . The sfhC21 allele of fabZ allows survival of ftsH null mutants . The enzyme is also involved in the elongation of 3-Ketoglutaryl-ACP-methyl-ester "3-ketoglutaryl-[acp]-methyl-ester" to Pimeloyl-ACP-methyl-esters "pimeloyl-[acp]-methyl-ester", part of the biotin biosynthesis pathway . Gel electrophoresis data suggested that the FabZ protein undergoes oligomerization, although the precise subunit structure was not determined...

## Biological Role

Catalyzes 3-HYDROXYDECANOYL-ACP-DEHYDR-RXN (reaction.ecocyc.3-HYDROXYDECANOYL-ACP-DEHYDR-RXN), (3R)-3-hydroxybutanoyl-[acyl-carrier-protein] hydratase (reaction.ecocyc.4.2.1.58-RXN), 4.2.1.59-RXN (reaction.ecocyc.4.2.1.59-RXN), 4.2.1.61-RXN (reaction.ecocyc.4.2.1.61-RXN), RXN-10656 (reaction.ecocyc.RXN-10656), RXN-10660 (reaction.ecocyc.RXN-10660), RXN-11477 (reaction.ecocyc.RXN-11477), RXN-11481 (reaction.ecocyc.RXN-11481), and 6 more.

## Annotation

There are two β-hydroxyacyl-ACP dehydratases in E. coli, coded for by the EG10273 and EG11284 genes. They both function in the dissociated or type II fatty acid synthase systems. The FabZ enzyme has a very broad substrate specificity. It catalyzes the dehydration of short chain β-hydroxyacyl-ACPs and long chain saturated and unsaturated β-hydroxyacyl-ACPs. While the FabA enzyme is most active on intermediate chain lengths, the two dehydratases do possess broad overlapping substrate specificities. It is thought that the FabZ enzyme is the primary dehydratase involved in the unsaturated branch of the fatty acid synthesis pathway . Certain mutations in fabZ have been found as suppressor mutations; its sabA1 allele changes the suppression of the OmpF315 phenotype by asmB1, and increased fabZ expression suppresses OmpF315 itself . The sfhC21 allele of fabZ allows survival of ftsH null mutants . The enzyme is also involved in the elongation of 3-Ketoglutaryl-ACP-methyl-ester "3-ketoglutaryl-[acp]-methyl-ester" to Pimeloyl-ACP-methyl-esters "pimeloyl-[acp]-methyl-ester", part of the biotin biosynthesis pathway . Gel electrophoresis data suggested that the FabZ protein undergoes oligomerization, although the precise subunit structure was not determined . However, a later paper describing the crystal structure of Pseudomonas aeruginosa FabZ also included the determination of the subunit structure of E. coli His-tagged FabZ. The native apparent molecular mass of the E. coli enzyme determined by gel filtration chromatography was 112 kDa and the subunit apparent molecular mass determined by SDS-PAGE was 19 kDa, suggesting a hexamer ( see Fig. 3). A steady state kinetic analysis of an in vitro reconstituted fatty acid biosynthesis system was performed in which increased concentratio

## Outgoing Edges (14)

- `catalyzes` --> [[reaction.ecocyc.3-HYDROXYDECANOYL-ACP-DEHYDR-RXN|reaction.ecocyc.3-HYDROXYDECANOYL-ACP-DEHYDR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.4.2.1.58-RXN|reaction.ecocyc.4.2.1.58-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.4.2.1.59-RXN|reaction.ecocyc.4.2.1.59-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.4.2.1.61-RXN|reaction.ecocyc.4.2.1.61-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-10656|reaction.ecocyc.RXN-10656]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-10660|reaction.ecocyc.RXN-10660]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-11477|reaction.ecocyc.RXN-11477]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-11481|reaction.ecocyc.RXN-11481]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9520|reaction.ecocyc.RXN-9520]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9533|reaction.ecocyc.RXN-9533]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9537|reaction.ecocyc.RXN-9537]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9557|reaction.ecocyc.RXN-9557]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9655|reaction.ecocyc.RXN-9655]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-2144|reaction.ecocyc.RXN0-2144]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A6Q6|protein.P0A6Q6]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:FABZ-CPLX`
- `QSPROTEOME:QS00183131`

## Notes

6*protein.P0A6Q6
