---
entity_id: "complex.ecocyc.GLNL-CPLX"
entity_type: "complex"
name: "protein histidine kinase NtrB"
source_database: "EcoCyc"
source_id: "GLNL-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "nitrogen regulator II"
  - "NRII"
  - "GlnL"
---

# protein histidine kinase NtrB

`complex.ecocyc.GLNL-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLNL-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AFB5|protein.P0AFB5]]

## Enriched Summary

NtrB (also known as nitrogen regulator II or NRII), encoded by glnL, is the histidine kinase of the NtrB-NtrC (or NRII-NRI) two-component system which functions as part of a complex regulatory network that controls nitrogen assimilation (reviewed in ). Purified NtrB autophosphorylates in the presence of ATP and transfers a phosphate to its cognate response regulator NtrC (nitrogen regulator I or NRI); NtrB catalysed phosphorylation of NtrC converts the latter to an active form which promotes transcription of the glnALG operon from the glnAp2 promoter . NtrC-phosphate has an 'autophosphatase activity'; dephosphorylation of NtrC-phosphate is stimulated in the presence of NtrB, ATP and protein PROTEIN-PII "PII-1" in vitro; the mechanism of dephosphorylation remains unclear and may not be a reversal of the phosphotransfer reaction (see also ). NtrB binds the key signal transduction protein PII-1 and this interaction regulates the NtrB-NtrC phosphorylation cycle (see PROTEIN-PII "PII-1" for further details); a second PII protein, PII2-CPLX PII-2, encoded by glnK is also implicated in regulation of the NtrB-NtrC cycle. NtrB forms a homodimer ; the NtrB monomer consists of a small N-terminal domain which contains a PAS motif, a central dimerization domain, and a C-terminal domain which contains ATP and PII binding sites (see also )...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN).

## Annotation

NtrB (also known as nitrogen regulator II or NRII), encoded by glnL, is the histidine kinase of the NtrB-NtrC (or NRII-NRI) two-component system which functions as part of a complex regulatory network that controls nitrogen assimilation (reviewed in ). Purified NtrB autophosphorylates in the presence of ATP and transfers a phosphate to its cognate response regulator NtrC (nitrogen regulator I or NRI); NtrB catalysed phosphorylation of NtrC converts the latter to an active form which promotes transcription of the glnALG operon from the glnAp2 promoter . NtrC-phosphate has an 'autophosphatase activity'; dephosphorylation of NtrC-phosphate is stimulated in the presence of NtrB, ATP and protein PROTEIN-PII "PII-1" in vitro; the mechanism of dephosphorylation remains unclear and may not be a reversal of the phosphotransfer reaction (see also ). NtrB binds the key signal transduction protein PII-1 and this interaction regulates the NtrB-NtrC phosphorylation cycle (see PROTEIN-PII "PII-1" for further details); a second PII protein, PII2-CPLX PII-2, encoded by glnK is also implicated in regulation of the NtrB-NtrC cycle. NtrB forms a homodimer ; the NtrB monomer consists of a small N-terminal domain which contains a PAS motif, a central dimerization domain, and a C-terminal domain which contains ATP and PII binding sites (see also ). NtrB autophosphorylates on a conserved histidine residue (His-139) by a transphosphorylation mechanism in which one subunit of the homodimer binds ATP and phosphorylates the other subunit . Early studies characterised glnL / glnR / ntrB mutants which show altered regulation of enzymes that are subject to nitrogen control ('Ntr enzymes') (and see ). Deletion of glnL is epistatic with respect to the phenotypes resulting from glnB and glnD mutations;

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AFB5|protein.P0AFB5]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GLNL-CPLX`
- `QSPROTEOME:QS00049715`

## Notes

2*protein.P0AFB5
