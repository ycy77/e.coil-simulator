---
entity_id: "complex.ecocyc.3-ISOPROPYLMALISOM-CPLX"
entity_type: "complex"
name: "3-isopropylmalate dehydratase"
source_database: "EcoCyc"
source_id: "3-ISOPROPYLMALISOM-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "isopropylmalate isomerase"
  - "&alpha"
  - "-isopropylmalate isomerase"
  - "-IPM isomerase"
  - "IPMI"
  - "3-isopropylmalate isomerase"
  - "3-carboxy-3-hydroxy-isocaproate isomerase"
---

# 3-isopropylmalate dehydratase

`complex.ecocyc.3-ISOPROPYLMALISOM-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:3-ISOPROPYLMALISOM-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6A6|protein.P0A6A6]], [[protein.P30126|protein.P30126]]

## Enriched Summary

Isopropylmalate (IPM) isomerase catalyzes the second step in leucine biosynthesis, converting 2-isopropylmalate to 3-isopropylmalate. LeuC and LeuD are both required for the activity of IPM isomerase . Based on the IPM isomerase in Salmonella typhimurium and cross-species complementation studies with the Salmonella and S. cerevisiae enzymes, E. coli IPM isomerase is likely to be a protein complex consisting of a 1:1 pairing of the of leuC and leuD gene products . Expression of leuCD (but not leuC alone) can complement leucine auxotrophy caused by a LEU1 mutation in S. cerevisiae . The failure of an E. coli mutant that lacks both peroxidase and catalase activities to grow in minimal medium under aerobic conditions is at least partly due to damage to the solvent-accessible [4Fe-4S] cluster of IPM isomerase, resulting in its inactivation . Copper also damages the [4Fe-4S] cluster of IPM isomerase . In vivo, IPM isomerase in H2O2-stressed cells appears to have lost its [Fe-S] cluster; this damage can be repaired by the Suf system . Isopropylmalate (IPM) isomerase catalyzes the second step in leucine biosynthesis, converting 2-isopropylmalate to 3-isopropylmalate. LeuC and LeuD are both required for the activity of IPM isomerase . Based on the IPM isomerase in Salmonella typhimurium and cross-species complementation studies with the Salmonella and S. cerevisiae enzymes, E...

## Biological Role

Catalyzes RXN-13163 (reaction.ecocyc.RXN-13163). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

Isopropylmalate (IPM) isomerase catalyzes the second step in leucine biosynthesis, converting 2-isopropylmalate to 3-isopropylmalate. LeuC and LeuD are both required for the activity of IPM isomerase . Based on the IPM isomerase in Salmonella typhimurium and cross-species complementation studies with the Salmonella and S. cerevisiae enzymes, E. coli IPM isomerase is likely to be a protein complex consisting of a 1:1 pairing of the of leuC and leuD gene products . Expression of leuCD (but not leuC alone) can complement leucine auxotrophy caused by a LEU1 mutation in S. cerevisiae . The failure of an E. coli mutant that lacks both peroxidase and catalase activities to grow in minimal medium under aerobic conditions is at least partly due to damage to the solvent-accessible [4Fe-4S] cluster of IPM isomerase, resulting in its inactivation . Copper also damages the [4Fe-4S] cluster of IPM isomerase . In vivo, IPM isomerase in H2O2-stressed cells appears to have lost its [Fe-S] cluster; this damage can be repaired by the Suf system .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-13163|reaction.ecocyc.RXN-13163]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A6A6|protein.P0A6A6]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P30126|protein.P30126]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:3-ISOPROPYLMALISOM-CPLX`
- `QSPROTEOME:QS00049536`

## Notes

1*protein.P0A6A6|1*protein.P30126
