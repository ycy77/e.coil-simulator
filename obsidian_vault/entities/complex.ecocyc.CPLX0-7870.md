---
entity_id: "complex.ecocyc.CPLX0-7870"
entity_type: "complex"
name: "sensor histidine kinase AtoS"
source_database: "EcoCyc"
source_id: "CPLX0-7870"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "AtoS"
---

# sensor histidine kinase AtoS

`complex.ecocyc.CPLX0-7870`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7870`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `regulatory`
- Components: [[protein.Q06067|protein.Q06067]]

## Enriched Summary

AtoS is the sensor histidine kinase of the AtoS/AtoC two-component signal transduction pathway which is best characterised by its induction of the ato operon (atoDAEB) for metabolism of short chain fatty acids in response to the presence of acetoacetate. AtoS is a homo-dimeric transmembrane protein consisting of an amino-terminal periplasmic sensing domain coupled to a carboxy-terminal cytoplasmic kinase domain |CITS [16153782][18534200]|. AtoS autophosphorylates on a conserved histidine residue (His-398) by a trans-phosphorylation mechanism in which one subunit of the homodimer binds ATP and phosphorylates the other subunit . AtoS tranfers a phosphoryl group to the cytoplasmic response regulator AtoC which controls transcriptional expression of the operon (atoDAEB) involved in short-chain fatty acid catabolism |CITS [2883171][15200682][16153782]|. AtoS is the sensor histidine kinase of the AtoS/AtoC two-component signal transduction pathway which is best characterised by its induction of the ato operon (atoDAEB) for metabolism of short chain fatty acids in response to the presence of acetoacetate. AtoS is a homo-dimeric transmembrane protein consisting of an amino-terminal periplasmic sensing domain coupled to a carboxy-terminal cytoplasmic kinase domain |CITS [16153782][18534200]|...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN).

## Annotation

AtoS is the sensor histidine kinase of the AtoS/AtoC two-component signal transduction pathway which is best characterised by its induction of the ato operon (atoDAEB) for metabolism of short chain fatty acids in response to the presence of acetoacetate. AtoS is a homo-dimeric transmembrane protein consisting of an amino-terminal periplasmic sensing domain coupled to a carboxy-terminal cytoplasmic kinase domain |CITS [16153782][18534200]|. AtoS autophosphorylates on a conserved histidine residue (His-398) by a trans-phosphorylation mechanism in which one subunit of the homodimer binds ATP and phosphorylates the other subunit . AtoS tranfers a phosphoryl group to the cytoplasmic response regulator AtoC which controls transcriptional expression of the operon (atoDAEB) involved in short-chain fatty acid catabolism |CITS [2883171][15200682][16153782]|.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.Q06067|protein.Q06067]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7870`
- `QSPROTEOME:QS00049671`

## Notes

2*protein.Q06067
