---
entity_id: "complex.ecocyc.CPLX0-8791"
entity_type: "complex"
name: "L-alanine exporter"
source_database: "EcoCyc"
source_id: "CPLX0-8791"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# L-alanine exporter

`complex.ecocyc.CPLX0-8791`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8791`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P64550|protein.P64550]]

## Enriched Summary

alaE encodes an inducible L-alanine exporter which contributes to the maintenance of L-alanine homeostasis. Disruption of alaE in an L-alanine non-metabolizing strain results in the significant accumulation of intra-cellular alanine and this phenotype can be relieved by over-expression of alaE from a plasmid . This strain also has higher susceptibility to L-alanine and to the dipeptide L-alanyl-L-alanine (L-Ala-L-Ala) and significant growth inhibition in media containing L-Ala-L-Ala . Inverted membrane vesicles prepared from L-alanine non-metabolizing, AlaE-producing cells accumulate L-alanine in an energy-dependent manner; accumulation decreases in the presence of the uncoupling agent, carbonyl cyanide m-chlorophenylhydrazone (CCCP) but not in the presence of the ATPase inhibitor, dicyclohexylcarbodiimide . L-serine and D-serine are inhibitors of L-alanine transport in vitro as is D-alanine although earlier studies suggested that AlaE exhibits stereospecificity for L-alanine . AlaE can function as a D-alanine exporter; the physiological relevance of this function remains unclear . AlaE has 4 transmembrane helices with the N and C-termini located in the cytoplasm; AlaE forms homo-oligomers in vitro and the protein may function as a homodimer in vivo . The expression of alaE in an L-alanine non-metabolizing strain is induced in the presence of L-ala-L-ala...

## Biological Role

Catalyzes alanine:proton antiport (reaction.ecocyc.TRANS-RXN0-469). Transports L-Alanine (molecule.C00041), hν (molecule.ecocyc.Light).

## Annotation

alaE encodes an inducible L-alanine exporter which contributes to the maintenance of L-alanine homeostasis. Disruption of alaE in an L-alanine non-metabolizing strain results in the significant accumulation of intra-cellular alanine and this phenotype can be relieved by over-expression of alaE from a plasmid . This strain also has higher susceptibility to L-alanine and to the dipeptide L-alanyl-L-alanine (L-Ala-L-Ala) and significant growth inhibition in media containing L-Ala-L-Ala . Inverted membrane vesicles prepared from L-alanine non-metabolizing, AlaE-producing cells accumulate L-alanine in an energy-dependent manner; accumulation decreases in the presence of the uncoupling agent, carbonyl cyanide m-chlorophenylhydrazone (CCCP) but not in the presence of the ATPase inhibitor, dicyclohexylcarbodiimide . L-serine and D-serine are inhibitors of L-alanine transport in vitro as is D-alanine although earlier studies suggested that AlaE exhibits stereospecificity for L-alanine . AlaE can function as a D-alanine exporter; the physiological relevance of this function remains unclear . AlaE has 4 transmembrane helices with the N and C-termini located in the cytoplasm; AlaE forms homo-oligomers in vitro and the protein may function as a homodimer in vivo . The expression of alaE in an L-alanine non-metabolizing strain is induced in the presence of L-ala-L-ala . alaE expression, in the K-12 strain MG1655, is induced by the transcriptional regulator Lrp, in response to increased levels of intracellular L-alanine; expression is also upregulated by L-leucine however leucine is not a substrate of the AlaE exporter . AlaE-mediated export of L-alanine avoids the toxic accumulation of L-alanine that would otherwise occur under peptide-rich growth conditions . alaE: alanine export

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-469|reaction.ecocyc.TRANS-RXN0-469]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P64550|protein.P64550]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX0-8791`
- `QSPROTEOME:QS00196509`

## Notes

2*protein.P64550
