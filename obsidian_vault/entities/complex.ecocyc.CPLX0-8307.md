---
entity_id: "complex.ecocyc.CPLX0-8307"
entity_type: "complex"
name: "sensor histidine kinase DcuS"
source_database: "EcoCyc"
source_id: "CPLX0-8307"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# sensor histidine kinase DcuS

`complex.ecocyc.CPLX0-8307`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8307`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AEC8|protein.P0AEC8]]

## Enriched Summary

DcuS is the sensor histidine kinase of the DcuSR two component system which controls the expression of genes relating to the utilization of exogenous C4 dicarboxylates. dcuS is required for the anaerobic, fumarate dependent induction of dcuB (encoding a dicarboxylate transporter) and frdA (the first gene in the operon encoding fumarate reductase) and is also involved in the aerobic, succinate dependent induction of dctA . DcuS senses external substrate . C4-dicarboxylates (fumarate and succinate) stimulate autophosphorylation of DcuS in vitro; the phosphate group is then rapidly transferred to the DcuR transcriptional activator . Under anaerobic conditions, fumarate, L-malate, maleate, L and D-tartrate, succinate, aspartate, mesaconate, the non–C4-dicarboxylate citrate, and 3-nitropropionate are all effectors of DcuS (as measured by expression of a dcuB-lacZ reporter gene fusion) . DcuS requires the transport protein DCTA-MONOMER "DctA" (under aerobic conditions) or DCUB-MONOMER "DcuB" (under anaerobic conditions) for normal function; deletion of DctA or DcuB results in constitutive expression of DcuSR regulated genes in the absence of C4-dicarboxylates . DcuS interacts physically with DctA in vivo ; DcuS interacts physically with DcuB in vivo; the complexes are present in both the absence and presence of fumarate...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN).

## Annotation

DcuS is the sensor histidine kinase of the DcuSR two component system which controls the expression of genes relating to the utilization of exogenous C4 dicarboxylates. dcuS is required for the anaerobic, fumarate dependent induction of dcuB (encoding a dicarboxylate transporter) and frdA (the first gene in the operon encoding fumarate reductase) and is also involved in the aerobic, succinate dependent induction of dctA . DcuS senses external substrate . C4-dicarboxylates (fumarate and succinate) stimulate autophosphorylation of DcuS in vitro; the phosphate group is then rapidly transferred to the DcuR transcriptional activator . Under anaerobic conditions, fumarate, L-malate, maleate, L and D-tartrate, succinate, aspartate, mesaconate, the non–C4-dicarboxylate citrate, and 3-nitropropionate are all effectors of DcuS (as measured by expression of a dcuB-lacZ reporter gene fusion) . DcuS requires the transport protein DCTA-MONOMER "DctA" (under aerobic conditions) or DCUB-MONOMER "DcuB" (under anaerobic conditions) for normal function; deletion of DctA or DcuB results in constitutive expression of DcuSR regulated genes in the absence of C4-dicarboxylates . DcuS interacts physically with DctA in vivo ; DcuS interacts physically with DcuB in vivo; the complexes are present in both the absence and presence of fumarate . Shifting DcuS from the constitutive "on" state (as measured by expression of dcuB-lacZ) to the fumarate responsive state requires the presence of DctA (under aerobic conditions) or DcuB (under anerobic condtions) but not transport by DctA/DcuB . Citrate can induce DcuS dependent reporter gene expression under aerobic growth but it is not a substrate for DctA-mediated transport ; citrate, maleate, L- and meso-tartrate and 3-nitropropionate can induce DcuS dep

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AEC8|protein.P0AEC8]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8307`
- `QSPROTEOME:QS00196215`

## Notes

2*protein.P0AEC8
