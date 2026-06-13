---
entity_id: "complex.ecocyc.CPLX0-8168"
entity_type: "complex"
name: "bifunctional sensor histidine kinase PhoQ"
source_database: "EcoCyc"
source_id: "CPLX0-8168"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# bifunctional sensor histidine kinase PhoQ

`complex.ecocyc.CPLX0-8168`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8168`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P23837|protein.P23837]]

## Enriched Summary

PhoQ is the bifunctional sensor histidine kinase of the PhoQP two-component signal transduction system. PhoQ has both sensor kinase activity - autophosphorylation and phosphotransfer to the PhoP transcription factor - and phospho-PhoP phosphatase activity. phoQ encodes a predicted inner membrane protein with two transmembrane regions; PhoQ is 86% identical to the (extensively characterized) PhoQ protein from Salmonella typhimurium . PhoQ is considered to be a prototypical homodimeric histidine kinase containing a periplasmic sensor domain, a transmembrane 4 helix bundle, a cytoplasmic HAMP domain and a kinase domain; Asn202 in transmembrane helix 2 is functionally important - mutagenesis suggests a stringent requirement for hydrophilicity despite being located in the membrane . The PhoQ sensor domain is implicated in binding divalent cations (Mg2+, Ca2+, Mn2+, Ba2+) in vitro; mutagenesis of a proposed cation binding site disrupts Mg2+ binding in vitro and impairs the PhoP mediated response to Mg2+ limitation in vivo supporting a model whereby Mg2+ binding stabilises PhoQ in a signaling-inactive conformation . A mutant PhoQ protein lacking the N-terminal sensor domain is competent for autophosphorylation and phosphotransfer but is unable to fully activate a PhoP dependent reporter gene in response to Mg2+ limitation...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN).

## Annotation

PhoQ is the bifunctional sensor histidine kinase of the PhoQP two-component signal transduction system. PhoQ has both sensor kinase activity - autophosphorylation and phosphotransfer to the PhoP transcription factor - and phospho-PhoP phosphatase activity. phoQ encodes a predicted inner membrane protein with two transmembrane regions; PhoQ is 86% identical to the (extensively characterized) PhoQ protein from Salmonella typhimurium . PhoQ is considered to be a prototypical homodimeric histidine kinase containing a periplasmic sensor domain, a transmembrane 4 helix bundle, a cytoplasmic HAMP domain and a kinase domain; Asn202 in transmembrane helix 2 is functionally important - mutagenesis suggests a stringent requirement for hydrophilicity despite being located in the membrane . The PhoQ sensor domain is implicated in binding divalent cations (Mg2+, Ca2+, Mn2+, Ba2+) in vitro; mutagenesis of a proposed cation binding site disrupts Mg2+ binding in vitro and impairs the PhoP mediated response to Mg2+ limitation in vivo supporting a model whereby Mg2+ binding stabilises PhoQ in a signaling-inactive conformation . A mutant PhoQ protein lacking the N-terminal sensor domain is competent for autophosphorylation and phosphotransfer but is unable to fully activate a PhoP dependent reporter gene in response to Mg2+ limitation . Purified PhoQ is active as an autokinase in buffer containing 0.01mM Mg2+ but activity is significantly decreased in the presence of 10mM Mg2+; the phosphotransfer activity of purified phosphorylated PhoQ is also significantly repressed in the presence of 10mM Mg2+ PhoQ exists as a phosphatase when Mg2+ is non-limiting; when Mg2+ decreases, the sensor kinase activity of PhoQ increases leading to phosphorylation and activation of the PhoP transcription regul

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P23837|protein.P23837]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8168`
- `QSPROTEOME:QS00196211`

## Notes

2*protein.P23837
