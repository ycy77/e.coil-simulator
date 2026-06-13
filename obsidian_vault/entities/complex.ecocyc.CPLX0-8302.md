---
entity_id: "complex.ecocyc.CPLX0-8302"
entity_type: "complex"
name: "sensor histidine kinase BarA"
source_database: "EcoCyc"
source_id: "CPLX0-8302"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# sensor histidine kinase BarA

`complex.ecocyc.CPLX0-8302`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8302`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AEC5|protein.P0AEC5]]

## Enriched Summary

BarA is the sensor histidine kinase of the EG11367 BarA/EG11140 UvrY two-component signal transduction system which plays a role in central carbon metabolism via its regulation of the small non-coding RNAs CSRC-RNA "CsrC and CSRB-RNA "CsrB". BarA senses and responds to the presence of the protonated form of short-chain carboxylic acids such as FORMATE "formic acid" and ACET "acetic acid", which accumulate at the late exponential phase of growth on acetogenic substrates such as glucose. Upon sensing of these products, BarA autophosphorylates, followed by transphosphorylation of the cognate response regulator UvrY, which activates transcription of the CsrB and CsrC noncoding regulatory RNAs. These RNAs bind to the RNA-binding protein CPLX0-7956 CsrA, preventing it from interacting with its mRNA targets. BarA is an inner membrane sensor kinase that is predicted to contain two transmembrane segments linked by a periplasmic bridge, plus a tripartite cytoplasmic domain consisting of a primary transmitter domain with a conserved histidine residue (His-302), a central receiver domain with a conserved aspartate residue (Asp-718) and a C-terminal phosphotransfer or Hpt domain containing the second conserved histidine residue (His-861) . BarA senses the presence of formic acid and acetic acids via its sensing domain, which is located within the periplasmic bridge...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN).

## Annotation

BarA is the sensor histidine kinase of the EG11367 BarA/EG11140 UvrY two-component signal transduction system which plays a role in central carbon metabolism via its regulation of the small non-coding RNAs CSRC-RNA "CsrC and CSRB-RNA "CsrB". BarA senses and responds to the presence of the protonated form of short-chain carboxylic acids such as FORMATE "formic acid" and ACET "acetic acid", which accumulate at the late exponential phase of growth on acetogenic substrates such as glucose. Upon sensing of these products, BarA autophosphorylates, followed by transphosphorylation of the cognate response regulator UvrY, which activates transcription of the CsrB and CsrC noncoding regulatory RNAs. These RNAs bind to the RNA-binding protein CPLX0-7956 CsrA, preventing it from interacting with its mRNA targets. BarA is an inner membrane sensor kinase that is predicted to contain two transmembrane segments linked by a periplasmic bridge, plus a tripartite cytoplasmic domain consisting of a primary transmitter domain with a conserved histidine residue (His-302), a central receiver domain with a conserved aspartate residue (Asp-718) and a C-terminal phosphotransfer or Hpt domain containing the second conserved histidine residue (His-861) . BarA senses the presence of formic acid and acetic acids via its sensing domain, which is located within the periplasmic bridge . Upon activation, BarA catalyses phosphorylation of its cognate response regulator UvrY, via a His→Asp→His→Asp phosphorelay. While BarA is activated during the late exponential growth phase, it is repressed during the stationary phase, when it is recruited by the CPLX0-1321 "HflKC complex" to the poles of the cells and its kinase activity is silenced. This repression does not occur during exponential growth since EG10435

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AEC5|protein.P0AEC5]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8302`
- `QSPROTEOME:QS00196189`

## Notes

2*protein.P0AEC5
