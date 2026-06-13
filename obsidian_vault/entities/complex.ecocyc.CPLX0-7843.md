---
entity_id: "complex.ecocyc.CPLX0-7843"
entity_type: "complex"
name: "formate channel FocA"
source_database: "EcoCyc"
source_id: "CPLX0-7843"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# formate channel FocA

`complex.ecocyc.CPLX0-7843`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7843`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AC23|protein.P0AC23]]

## Enriched Summary

FocA is a pH dependent, bidirectional formate transporter with an important role in regulating intracellular formate levels during anaerobic respiration and mixed acid fermentation. Formate, produced by the action of the glycyl-radical enzyme PYRUVFORMLY-CPLX "pyruvate:formate lyase" (PflB) is exported from the cytoplasm where, in the presence of terminal electron acceptors, it is a substrate of the periplasmic formate dehydrogenases. In the absence of terminal electron acceptors it is reimported to the cytoplasm for use by the FHLMULTI-CPLX "formate:hydrogen lyase complex" (reviewed in ). Analysis of formate levels in fermenting E. coli cultures indicate that initially, formate is exported out of the cell in order to prevent acidification of the cytoplasm. focA knock-out mutants grown in this manner are associated with increased intracellular levels of formate and decreased excretion of formate. However, if the pH of the culture medium drops below about 6.8, formate is transported back into the cell by FocA (see also and ). FocA is required for the import of the toxic formate analogue, hypophosphite . FocA and FOCB-MONOMER FocB are implicated in the maintenance of ion gradients during fermentation . The FocA compex (purified from E...

## Biological Role

Catalyzes TRANS-RXN-1 (reaction.ecocyc.TRANS-RXN-1), TRANS-RXN-381 (reaction.ecocyc.TRANS-RXN-381).

## Annotation

FocA is a pH dependent, bidirectional formate transporter with an important role in regulating intracellular formate levels during anaerobic respiration and mixed acid fermentation. Formate, produced by the action of the glycyl-radical enzyme PYRUVFORMLY-CPLX "pyruvate:formate lyase" (PflB) is exported from the cytoplasm where, in the presence of terminal electron acceptors, it is a substrate of the periplasmic formate dehydrogenases. In the absence of terminal electron acceptors it is reimported to the cytoplasm for use by the FHLMULTI-CPLX "formate:hydrogen lyase complex" (reviewed in ). Analysis of formate levels in fermenting E. coli cultures indicate that initially, formate is exported out of the cell in order to prevent acidification of the cytoplasm. focA knock-out mutants grown in this manner are associated with increased intracellular levels of formate and decreased excretion of formate. However, if the pH of the culture medium drops below about 6.8, formate is transported back into the cell by FocA (see also and ). FocA is required for the import of the toxic formate analogue, hypophosphite . FocA and FOCB-MONOMER FocB are implicated in the maintenance of ion gradients during fermentation . The FocA compex (purified from E. coli O157:H7) is a symmetric pentamer forming a single central pore believed to be occupied by lipid molecules, plus 5 axial pores (one per protomer) that may be the site of transport (see also ). Each protomer contains six transmembrane helices; both the amino and carboxy termini of FocA protomers are located on the cytoplasmic side of the inner membrane . The energetics of formate transport are unclear although structural evidence suggests that FocA functions as a channel rather than a transporter . The FocA complex must undergo some sort

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-1|reaction.ecocyc.TRANS-RXN-1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-381|reaction.ecocyc.TRANS-RXN-381]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AC23|protein.P0AC23]] `EcoCyc` `database` - EcoCyc component coefficient=5 | EcoCyc protcplxs.col coefficient=5 | EcoCyc transporter component coefficient=5

## External IDs

- `EcoCyc:CPLX0-7843`
- `QSPROTEOME:QS00155811`

## Notes

5*protein.P0AC23
