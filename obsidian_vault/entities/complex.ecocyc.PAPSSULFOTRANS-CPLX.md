---
entity_id: "complex.ecocyc.PAPSSULFOTRANS-CPLX"
entity_type: "complex"
name: "phosphoadenosine phosphosulfate reductase"
source_database: "EcoCyc"
source_id: "PAPSSULFOTRANS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# phosphoadenosine phosphosulfate reductase

`complex.ecocyc.PAPSSULFOTRANS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PAPSSULFOTRANS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P17854|protein.P17854]]

## Enriched Summary

3'-Phospho-adenylylsulfate reductase (CysH) is involved in the assimilation of sulfate and catalyzes the reduction of 3'-phospho-adenylylsulfate (PAPS) to sulfite and PAP. As a consequence of this and a subsequent reaction, the adenylate removed from the cell at the initiation of the cysteine biosynthetic pathway is returned as AMP. PAPS reductase is composed of two identical subunits of 28 kDa. It has no chromophores and contains a single cysteine per subunit in a highly conserved ECGLH motif, which is identified as the redox-active center of the enzyme . Reduction of sulfate to sulfite by PAPS reductase requires two electrons which are donated by the cysteine residues of the enzyme in a ping-pong mechanism. During the transfer, the cysteines are oxidized and form a disulfide. The oxidized enzyme is inactive and needs to be reduced for the reduction of PAPS to continue. Dimeric oxidized PAPS reductase migrates on SDS-PAGE with an apparent molecular mass (60 kDa) higher than that of the reduced form (30 kDa). The enzyme can be reduced in vitro by the thioredoxins Trx1 and Trx2 and the glutaredoxin Grx1 . The likely in vivo relevant factor is Trx1. The enzyme is also regulated by glutathione: if the intracellular environment is somewhat oxidizing, a mixed disulfide may form between Cys239 of the enzyme and glutathione, rendering the enzyme inactive...

## Biological Role

Catalyzes 1.8.4.8-RXN (reaction.ecocyc.1.8.4.8-RXN).

## Annotation

3'-Phospho-adenylylsulfate reductase (CysH) is involved in the assimilation of sulfate and catalyzes the reduction of 3'-phospho-adenylylsulfate (PAPS) to sulfite and PAP. As a consequence of this and a subsequent reaction, the adenylate removed from the cell at the initiation of the cysteine biosynthetic pathway is returned as AMP. PAPS reductase is composed of two identical subunits of 28 kDa. It has no chromophores and contains a single cysteine per subunit in a highly conserved ECGLH motif, which is identified as the redox-active center of the enzyme . Reduction of sulfate to sulfite by PAPS reductase requires two electrons which are donated by the cysteine residues of the enzyme in a ping-pong mechanism. During the transfer, the cysteines are oxidized and form a disulfide. The oxidized enzyme is inactive and needs to be reduced for the reduction of PAPS to continue. Dimeric oxidized PAPS reductase migrates on SDS-PAGE with an apparent molecular mass (60 kDa) higher than that of the reduced form (30 kDa). The enzyme can be reduced in vitro by the thioredoxins Trx1 and Trx2 and the glutaredoxin Grx1 . The likely in vivo relevant factor is Trx1. The enzyme is also regulated by glutathione: if the intracellular environment is somewhat oxidizing, a mixed disulfide may form between Cys239 of the enzyme and glutathione, rendering the enzyme inactive. This inactivation can be relieved by all glutaredoxins, which can catalyze the reduction of this mixed disulfide . A conserved residue which altered catalytic activity when mutated was identified through site directed mutagenesis studies . The crystal structure of CysH in complex with thioredoxin I has been determined at 3.0 Å resolution . The CysH protein is capable of weak interactions with the HupA protein . Mutational stu

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.1.8.4.8-RXN|reaction.ecocyc.1.8.4.8-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P17854|protein.P17854]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PAPSSULFOTRANS-CPLX`
- `QSPROTEOME:QS00188477`

## Notes

2*protein.P17854
