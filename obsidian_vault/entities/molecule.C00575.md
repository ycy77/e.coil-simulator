---
entity_id: "molecule.C00575"
entity_type: "small_molecule"
name: "3',5'-Cyclic AMP"
source_database: "KEGG"
source_id: "C00575"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3',5'-Cyclic AMP"
  - "Cyclic adenylic acid"
  - "Cyclic AMP"
  - "Adenosine 3',5'-phosphate"
  - "Adenosine 3',5'-cyclic phosphate"
  - "cAMP"
---

# 3',5'-Cyclic AMP

`molecule.C00575`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00575`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3',5'-Cyclic AMP; Cyclic adenylic acid; Cyclic AMP; Adenosine 3',5'-phosphate; Adenosine 3',5'-cyclic phosphate; cAMP EcoCyc common name: cyclic-AMP. cAMP is a second messenger used for intracellular signal transduction in many different organisms. In eukaryotes it acts in the activation of protein kinases, in the regulation of ion channels and other proteins, and by conveying to cells the effects of hormones that cannot pass through the plasma membrane. In bacteria cAMP is an indicator for the presence of glucose. A side-effect of glucose transport into the cell results in inhibition of EC-4.6.1.1, and as a result, an inverse correlation between the concentrations of glucose and cAMP. It forms a complex with the transcription factor cAMP receptor protein (CRP), which activates the regulator to bind to DNA, resulting in increased expression of a large number of genes as a response to glucose starvation.

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

KEGG compound: 3',5'-Cyclic AMP; Cyclic adenylic acid; Cyclic AMP; Adenosine 3',5'-phosphate; Adenosine 3',5'-cyclic phosphate; cAMP

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (9)

- `is_component_of` --> [[complex.ecocyc.CPLX0-226|complex.ecocyc.CPLX0-226]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R00089|reaction.R00089]] `KEGG` `database` - C00002 <=> C00575 + C00013
- `is_product_of` --> [[reaction.ecocyc.ADENYLATECYC-RXN|reaction.ecocyc.ADENYLATECYC-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-564|reaction.ecocyc.TRANS-RXN0-564]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00191|reaction.R00191]] `KEGG` `database` - C00575 + C00001 <=> C00020
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-269|reaction.ecocyc.RXN0-269]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5038|reaction.ecocyc.RXN0-5038]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-564|reaction.ecocyc.TRANS-RXN0-564]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.MALIC-NADP-RXN|reaction.ecocyc.MALIC-NADP-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00575`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
