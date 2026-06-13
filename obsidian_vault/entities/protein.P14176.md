---
entity_id: "protein.P14176"
entity_type: "protein"
name: "proW"
source_database: "UniProt"
source_id: "P14176"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "proW b2678 JW2653"
---

# proW

`protein.P14176`

## Static

- Type: `protein`
- Source: `UniProt:P14176`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the ProU ABC transporter complex involved in glycine betaine and proline betaine uptake (PubMed:23249124, PubMed:3305496, PubMed:7898450). Probably responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:23249124, ECO:0000269|PubMed:3305496, ECO:0000269|PubMed:7898450, ECO:0000305}. ProW is the predicted integral membrane subunit of an osmoresponsive ABC transport system that imports compounds such as glycine betaine and proline betaine in response to osmotic upshift. ProW is predicted to contain 7 transmembrane regions and an N-terminal domain that protrudes into the periplasm

## Biological Role

Component of glycine betaine ABC transporter (complex.ecocyc.ABC-26-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ProU ABC transporter complex involved in glycine betaine and proline betaine uptake (PubMed:23249124, PubMed:3305496, PubMed:7898450). Probably responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:23249124, ECO:0000269|PubMed:3305496, ECO:0000269|PubMed:7898450, ECO:0000305}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-26-CPLX|complex.ecocyc.ABC-26-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2678|gene.b2678]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P14176`
- `KEGG:ecj:JW2653;eco:b2678;ecoc:C3026_14755;`
- `GeneID:86860771;947145;`
- `GO:GO:0005275; GO:0005886; GO:0006972; GO:0015226; GO:0015871; GO:0016020; GO:0031460; GO:0043190; GO:0071470; GO:0089718; GO:1902603; GO:1903804; GO:1990222`

## Notes

Glycine betaine/proline betaine transport system permease protein ProW
