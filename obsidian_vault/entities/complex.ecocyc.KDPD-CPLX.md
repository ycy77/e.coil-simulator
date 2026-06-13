---
entity_id: "complex.ecocyc.KDPD-CPLX"
entity_type: "complex"
name: "serine histidine kinase KdpD"
source_database: "EcoCyc"
source_id: "KDPD-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# serine histidine kinase KdpD

`complex.ecocyc.KDPD-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:KDPD-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCO-PM-BAC-NEG
- Complex type: `regulatory`
- Components: [[protein.P21865|protein.P21865]]

## Enriched Summary

KdpD is the tandem serine histidine kinase of the PWY0-1495 "KdpDE two-component system" which contributes to K+ homeostasis through control of the high-affinity ATPASE-1-CPLX (KdpFABC); KdpD acts as both a two-component sensor histidine kinase/phosphatase to regulate kdpFABC transcription and as an atypical serine kinase to control KdpFABC activity post-translationally. KdpD is the sensor member of a sensor-effector pair with KdpE . KdpD has autokinase, phosphotransferase and protein phosphatase activity: in the presence of ATP, purified, reconstituted KdpD autophosphorylates at the conserved His-673 residue and subsequently transfers the phosphate to its cognate response regulator - the KdpE transcription factor ; KdpD is able to dephosphorylate phospho-KdpE in vitro . The rate of dephosphorylation increases in the presence of ATP or nonhydrolyzable ATP analogs but is not affected by other nucleotides . KdpD kinase activity in reconstituted proteoliposomes is influenced by phospholipid composition . KdpD has atypical serine kinase activity; KdpD directly mediates KdpBS162 phosphorylation with subsequent KdpFABC inhibition; mutating the Walker A motif in the N-terminal 'KdpD domain' abolishes KdpBS162 phosphorylation in vitro . The nature of the primary stimulus perceived by KdpD has been widely investigated (see reviews by )...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN), RXN-24864 (reaction.ecocyc.RXN-24864).

## Annotation

KdpD is the tandem serine histidine kinase of the PWY0-1495 "KdpDE two-component system" which contributes to K+ homeostasis through control of the high-affinity ATPASE-1-CPLX (KdpFABC); KdpD acts as both a two-component sensor histidine kinase/phosphatase to regulate kdpFABC transcription and as an atypical serine kinase to control KdpFABC activity post-translationally. KdpD is the sensor member of a sensor-effector pair with KdpE . KdpD has autokinase, phosphotransferase and protein phosphatase activity: in the presence of ATP, purified, reconstituted KdpD autophosphorylates at the conserved His-673 residue and subsequently transfers the phosphate to its cognate response regulator - the KdpE transcription factor ; KdpD is able to dephosphorylate phospho-KdpE in vitro . The rate of dephosphorylation increases in the presence of ATP or nonhydrolyzable ATP analogs but is not affected by other nucleotides . KdpD kinase activity in reconstituted proteoliposomes is influenced by phospholipid composition . KdpD has atypical serine kinase activity; KdpD directly mediates KdpBS162 phosphorylation with subsequent KdpFABC inhibition; mutating the Walker A motif in the N-terminal 'KdpD domain' abolishes KdpBS162 phosphorylation in vitro . The nature of the primary stimulus perceived by KdpD has been widely investigated (see reviews by ). Early work indicating that the Kdp system responds to turgor pressure (the difference in pressure across the inner membrane) and suggesting that KdpD is a mechanical transducer which undergoes conformational change in response to membrane pressure or stretch has been disputed . Other studies have focused on intracellular and extracellular K+ concentration, intracellular ionic strength and ATP levels as defining stimuli ; it has also been suggeste

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-24864|reaction.ecocyc.RXN-24864]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P21865|protein.P21865]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:KDPD-CPLX`
- `QSPROTEOME:QS00049728`
- `PDB:6LGQ`
- `PDB:4Y2F`
- `PDB:4QPR`

## Notes

2*protein.P21865
