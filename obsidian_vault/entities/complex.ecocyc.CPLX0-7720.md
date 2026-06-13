---
entity_id: "complex.ecocyc.CPLX0-7720"
entity_type: "complex"
name: "undecaprenyl-phosphate-α-L-Ara4N flippase"
source_database: "EcoCyc"
source_id: "CPLX0-7720"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "undecaprenyl-phosphate-&alpha"
  - "-L-Ara4N intramembrane lipid transporter"
---

# undecaprenyl-phosphate-α-L-Ara4N flippase

`complex.ecocyc.CPLX0-7720`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7720`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.Q47377|protein.Q47377]], [[protein.P76474|protein.P76474]]

## Enriched Summary

The ArnE/ArnF undecaprenyl-phosphate-α-L-Ara4N flippase is responsible for transporting undecaprenyl-phosphate-α-L-Ara4N from the cytoplasmic face of the inner membrane to the periplasmic face of the inner membrane. ArnE and ArnF are both predicted to be integral membrane proteins with 4 transmembrane helices and belong to the drug/metabolite transporter (DMT) superfamily . ArnE and ArnF may act as a heterodimer . Deletion of arnE or arnF results in restoration of polymyxin sensitivity in a polymyxin-resitant pmrAc strain; mutant strains are defective for transfer of undecaprenyl-phosphate-α-L-Ara4N from the cytoplasmic face of the inner membrane to the periplasmic face and for attachment of L-Ara4N to lipid A . Both ArnE and ArnF are required for polymyxin resistance as expression from a plasmid of one cannot replace a deletion of the other . Expression of the arnBCADTEF operon increased during growth with elevated FeSO4, FeCl3, or ZnSO4 and was dependent upon the BasSR two-component signal transduction system . Reviews: The ArnE/ArnF undecaprenyl-phosphate-α-L-Ara4N flippase is responsible for transporting undecaprenyl-phosphate-α-L-Ara4N from the cytoplasmic face of the inner membrane to the periplasmic face of the inner membrane...

## Biological Role

Catalyzes TRANS-RXN0-276 (reaction.ecocyc.TRANS-RXN0-276).

## Annotation

The ArnE/ArnF undecaprenyl-phosphate-α-L-Ara4N flippase is responsible for transporting undecaprenyl-phosphate-α-L-Ara4N from the cytoplasmic face of the inner membrane to the periplasmic face of the inner membrane. ArnE and ArnF are both predicted to be integral membrane proteins with 4 transmembrane helices and belong to the drug/metabolite transporter (DMT) superfamily . ArnE and ArnF may act as a heterodimer . Deletion of arnE or arnF results in restoration of polymyxin sensitivity in a polymyxin-resitant pmrAc strain; mutant strains are defective for transfer of undecaprenyl-phosphate-α-L-Ara4N from the cytoplasmic face of the inner membrane to the periplasmic face and for attachment of L-Ara4N to lipid A . Both ArnE and ArnF are required for polymyxin resistance as expression from a plasmid of one cannot replace a deletion of the other . Expression of the arnBCADTEF operon increased during growth with elevated FeSO4, FeCl3, or ZnSO4 and was dependent upon the BasSR two-component signal transduction system . Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-276|reaction.ecocyc.TRANS-RXN0-276]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P76474|protein.P76474]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.Q47377|protein.Q47377]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:CPLX0-7720`
- `QSPROTEOME:QS00049437`

## Notes

protein.Q47377|protein.P76474
