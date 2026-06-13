---
entity_id: "complex.ecocyc.CPLX0-234"
entity_type: "complex"
name: "2-C-methyl-D-erythritol 4-phosphate cytidylyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-234"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 2-C-methyl-D-erythritol 4-phosphate cytidylyltransferase

`complex.ecocyc.CPLX0-234`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-234`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.Q46893|protein.Q46893]]

## Enriched Summary

4-diphosphocytidyl-2C-methyl-D-erythritol synthase (IspD) catalyzes the third step in the methylerythritol phosphate pathway, the CTP-dependent conversion of 2-C-methyl-D-erythritol-4-phosphate to 4-(cytidine 5'-diphospho)-2-C-methyl-erythritol . This is an ordered reaction, with CTP binding required before 2-C-methyl-D-erythritol-4-phosphate can bind . This reaction requires Mn2+ or Mg2+ as a cofactor . IspD is a homodimer . Crystal structures have been determined, both of the apo form of the enzyme and enzyme bound to CTP and Mg2+, and 4-(cytidine 5'-diphospho)-2-C-methyl-erythritol and Mg2+, offering insight into the reaction process . A number of residues have been identified that are critical for enzymatic activity . ispD is an essential gene . Since the enzymes of the methylerythritol pathway are not found in humans, they have attracted much interest for their potential as anti-infective drug targets. Inhibitors for IspD have been studied . Both computational and high-throughput experimental methods have been used to attempt to identify inhibitors of IspD |CITS [22213702][17081012]|. 4-diphosphocytidyl-2C-methyl-D-erythritol synthase (IspD) catalyzes the third step in the methylerythritol phosphate pathway, the CTP-dependent conversion of 2-C-methyl-D-erythritol-4-phosphate to 4-(cytidine 5'-diphospho)-2-C-methyl-erythritol...

## Biological Role

Catalyzes 2.7.7.60-RXN (reaction.ecocyc.2.7.7.60-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

4-diphosphocytidyl-2C-methyl-D-erythritol synthase (IspD) catalyzes the third step in the methylerythritol phosphate pathway, the CTP-dependent conversion of 2-C-methyl-D-erythritol-4-phosphate to 4-(cytidine 5'-diphospho)-2-C-methyl-erythritol . This is an ordered reaction, with CTP binding required before 2-C-methyl-D-erythritol-4-phosphate can bind . This reaction requires Mn2+ or Mg2+ as a cofactor . IspD is a homodimer . Crystal structures have been determined, both of the apo form of the enzyme and enzyme bound to CTP and Mg2+, and 4-(cytidine 5'-diphospho)-2-C-methyl-erythritol and Mg2+, offering insight into the reaction process . A number of residues have been identified that are critical for enzymatic activity . ispD is an essential gene . Since the enzymes of the methylerythritol pathway are not found in humans, they have attracted much interest for their potential as anti-infective drug targets. Inhibitors for IspD have been studied . Both computational and high-throughput experimental methods have been used to attempt to identify inhibitors of IspD |CITS [22213702][17081012]|.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.7.60-RXN|reaction.ecocyc.2.7.7.60-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.Q46893|protein.Q46893]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-234`
- `QSPROTEOME:QS00182013`

## Notes

2*protein.Q46893
