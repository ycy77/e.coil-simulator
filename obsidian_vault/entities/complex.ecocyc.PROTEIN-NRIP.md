---
entity_id: "complex.ecocyc.PROTEIN-NRIP"
entity_type: "complex"
name: "DNA-binding transcriptional dual regulator NtrC-phosphorylated"
source_database: "EcoCyc"
source_id: "PROTEIN-NRIP"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-CYTOSOL-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "NtrC-P<sup>asp54</sup>"
  - "NRI"
  - "NtrC response regulator - phosphorylated"
---

# DNA-binding transcriptional dual regulator NtrC-phosphorylated

`complex.ecocyc.PROTEIN-NRIP`

## Static

- Type: `complex`
- Source: `EcoCyc:PROTEIN-NRIP`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-CYTOSOL-GN
- Complex type: `regulatory`
- Components: [[complex.ecocyc.CPLX0-8566|complex.ecocyc.CPLX0-8566]]

## Enriched Summary

Under nitrogen (N)-limiting conditions, the NtrC transcriptional dual regulator regulates genes involved in the assimilation of nitrogen and in the minimization of the slow growth caused by the N-limited condition . Through a cascade of events NtrC appears to regulate as much as 2% of the genome, and many of these genes encode transport systems for nitrogen-containing compounds . NtrC is also involved in the formation of ciprofloxacin-tolerant persister cells under N starvation growth conditions . In an indirect way, NtrC positively regulates genes involved in the synthesis of inorganic polyphosphate (polyP) . NtrC belongs to the two-component system NtrB/NtrC and is a member of the σ54-dependent activator family, whose homologues are widely distributed in bacteria . Both genes glnG, encoding the response regulator (NtrC, also called NRI), and glnL, encoding the sensor kinase (NtrB, also called NRII), are organized in the operon glnALG. glnA encodes a glutamine synthetase. In rich media, the transcription of glnALG is activated from the glnAp1 promoter by σ70 and under limiting ammonium is activated from the glnAp2 promoter by σ54 . NtrB functions as a membrane-associated protein kinase that in response to limitation of N and carbon-limited growth is autophosphorylated. After that, NtrB transfers its phosphate group to NtrC to activate this transcriptional regulator...

## Annotation

Under nitrogen (N)-limiting conditions, the NtrC transcriptional dual regulator regulates genes involved in the assimilation of nitrogen and in the minimization of the slow growth caused by the N-limited condition . Through a cascade of events NtrC appears to regulate as much as 2% of the genome, and many of these genes encode transport systems for nitrogen-containing compounds . NtrC is also involved in the formation of ciprofloxacin-tolerant persister cells under N starvation growth conditions . In an indirect way, NtrC positively regulates genes involved in the synthesis of inorganic polyphosphate (polyP) . NtrC belongs to the two-component system NtrB/NtrC and is a member of the σ54-dependent activator family, whose homologues are widely distributed in bacteria . Both genes glnG, encoding the response regulator (NtrC, also called NRI), and glnL, encoding the sensor kinase (NtrB, also called NRII), are organized in the operon glnALG. glnA encodes a glutamine synthetase. In rich media, the transcription of glnALG is activated from the glnAp1 promoter by σ70 and under limiting ammonium is activated from the glnAp2 promoter by σ54 . NtrB functions as a membrane-associated protein kinase that in response to limitation of N and carbon-limited growth is autophosphorylated. After that, NtrB transfers its phosphate group to NtrC to activate this transcriptional regulator . NtrB is also able to dephosphorylate to NtrC . On the other hand, NtrC is sometimes autophosphorylated with small-molecule phospho donors . In the presence of N, the GlnB protein (also called PII) or the GlnK protein binds to NtrB to activate its phosphatase activity. The NtrB-GlnB/GlnK complex dephosphorylates to NtrC or inhibits NtrC autophosphorylation, inactivating it . Under N deficiency, GlnB and Gln

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-8566|complex.ecocyc.CPLX0-8566]] `EcoCyc` `database` - EcoCyc component coefficient=3
- `is_component_of` <-- [[protein.P0AFB8|protein.P0AFB8]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:PROTEIN-NRIP`
- `QSPROTEOME:QS00183139`

## Notes

3*complex.ecocyc.CPLX0-8566
