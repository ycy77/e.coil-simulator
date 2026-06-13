---
entity_id: "complex.ecocyc.CPLX0-10815"
entity_type: "complex"
name: "high-affinity pyruvate receptor"
source_database: "EcoCyc"
source_id: "CPLX0-10815"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-CYTOSOL-GN|CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# high-affinity pyruvate receptor

`complex.ecocyc.CPLX0-10815`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-10815`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-CYTOSOL-GN|CCI-PM-BAC-NEG-GN
- Complex type: `structural`
- Components: [[protein.P0AD14|protein.P0AD14]]

## Enriched Summary

BtsS is the high-affinity pyruvate receptor of the PWY0-1559 which regulates expression of the pyruvate transporter, G7942-MONOMER "BtsT" in response to nutrient limitation . BtsS binds pyruvate with high affinity (Kd = 58.6 µM) and extracellular pyruvate induces btsT expression in a low-nutrient environment . BtsS is an inner membrane protein with six/seven predicted transmembrane domains; the C terminus is located in the cytoplasm; the N-terminus in the periplasm . BtsS is a class I histidine kinase (HK) in which the histidine phosphotransfer domain is directly linked to the catalytic ATP binding domain . Histidine residue 384 located in the transmitter domain is predicted to be the phosphorylation site and replacement of this residue with a glutamine prevents btsT induction . Autokinase and phosphotransfer activities have been demonstrated in vitro; autokinase activity requires Mn2+-ATP instead of Mg2+-ATP and is stimulated in the presence of pyruvate . A strong protein-protein interaction between BtsS and the inner membrane transporters G7942-MONOMER "BtsT" and YHJX-MONOMER "YhjX" has been detected. BtsS is capable of homo-oligomerisation . A btsSR double deletion mutant (ΔyehTU1324) shows no significant phenotype (compared to an isogenic control strain) when assayed using high throughput phenotype microarrays...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN).

## Annotation

BtsS is the high-affinity pyruvate receptor of the PWY0-1559 which regulates expression of the pyruvate transporter, G7942-MONOMER "BtsT" in response to nutrient limitation . BtsS binds pyruvate with high affinity (Kd = 58.6 µM) and extracellular pyruvate induces btsT expression in a low-nutrient environment . BtsS is an inner membrane protein with six/seven predicted transmembrane domains; the C terminus is located in the cytoplasm; the N-terminus in the periplasm . BtsS is a class I histidine kinase (HK) in which the histidine phosphotransfer domain is directly linked to the catalytic ATP binding domain . Histidine residue 384 located in the transmitter domain is predicted to be the phosphorylation site and replacement of this residue with a glutamine prevents btsT induction . Autokinase and phosphotransfer activities have been demonstrated in vitro; autokinase activity requires Mn2+-ATP instead of Mg2+-ATP and is stimulated in the presence of pyruvate . A strong protein-protein interaction between BtsS and the inner membrane transporters G7942-MONOMER "BtsT" and YHJX-MONOMER "YhjX" has been detected. BtsS is capable of homo-oligomerisation . A btsSR double deletion mutant (ΔyehTU1324) shows no significant phenotype (compared to an isogenic control strain) when assayed using high throughput phenotype microarrays . bts: 'brenztraubensaure' (pyruvic acid)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AD14|protein.P0AD14]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-10815`
- `QSPROTEOME:QS00196483`

## Notes

2*protein.P0AD14
