---
entity_id: "protein.P0A6H1"
entity_type: "protein"
name: "clpX"
source_database: "UniProt"
source_id: "P0A6H1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "clpX lopC b0438 JW0428"
---

# clpX

`protein.P0A6H1`

## Static

- Type: `protein`
- Source: `UniProt:P0A6H1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: ATP-dependent specificity component of the Clp protease. Uses cycles of ATP binding and hydrolysis to unfold proteins and translocate them to the ClpP protease. It directs the protease to specific substrates both with and without the help of adapter proteins such as SspB. Participates in the final steps of RseA-sigma-E degradation, liberating sigma-E to induce the extracytoplasmic-stress response. It may bind to the lambda O substrate protein and present it to the ClpP protease in a form that can be recognized and readily hydrolyzed by ClpP. Can perform chaperone functions in the absence of ClpP. {ECO:0000269|PubMed:12941278, ECO:0000269|PubMed:15371343}.

## Biological Role

Component of ClpX ATP-dependent protease specificity component and chaperone (complex.ecocyc.CPLX0-3102), ClpXP (complex.ecocyc.CPLX0-3107), ClpAXP (complex.ecocyc.CPLX0-3108).

## Annotation

FUNCTION: ATP-dependent specificity component of the Clp protease. Uses cycles of ATP binding and hydrolysis to unfold proteins and translocate them to the ClpP protease. It directs the protease to specific substrates both with and without the help of adapter proteins such as SspB. Participates in the final steps of RseA-sigma-E degradation, liberating sigma-E to induce the extracytoplasmic-stress response. It may bind to the lambda O substrate protein and present it to the ClpP protease in a form that can be recognized and readily hydrolyzed by ClpP. Can perform chaperone functions in the absence of ClpP. {ECO:0000269|PubMed:12941278, ECO:0000269|PubMed:15371343}.

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3102|complex.ecocyc.CPLX0-3102]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6
- `is_component_of` --> [[complex.ecocyc.CPLX0-3107|complex.ecocyc.CPLX0-3107]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` --> [[complex.ecocyc.CPLX0-3108|complex.ecocyc.CPLX0-3108]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b0438|gene.b0438]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6H1`
- `KEGG:ecj:JW0428;eco:b0438;ecoc:C3026_02145;`
- `GeneID:86862983;93777016;945083;`
- `GO:GO:0002020; GO:0004176; GO:0005524; GO:0005829; GO:0008270; GO:0009368; GO:0009376; GO:0016887; GO:0042802; GO:0043335; GO:0046983; GO:0051082; GO:0051301; GO:0051603; GO:0097718; GO:0140662`

## Notes

ATP-dependent Clp protease ATP-binding subunit ClpX (ATP-dependent unfoldase ClpX)
