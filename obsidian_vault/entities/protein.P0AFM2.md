---
entity_id: "protein.P0AFM2"
entity_type: "protein"
name: "proX"
source_database: "UniProt"
source_id: "P0AFM2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:3305496, ECO:0000269|PubMed:7898450}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "proX proU b2679 JW2654"
---

# proX

`protein.P0AFM2`

## Static

- Type: `protein`
- Source: `UniProt:P0AFM2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:3305496, ECO:0000269|PubMed:7898450}.

## Enriched Summary

FUNCTION: Part of the ProU ABC transporter complex involved in glycine betaine and proline betaine uptake. Binds glycine betaine and proline betaine with high affinity. {ECO:0000269|PubMed:14612446, ECO:0000269|PubMed:23249124, ECO:0000269|PubMed:3305496, ECO:0000269|PubMed:7898450}. ProX is the periplasmic binding protein of an osmoresponsive ABC transport system that imports compounds such as glycine betaine and proline betaine in response to osmotic upshift. Purified ProX consists of two globular domains connected through a hinge region; a ligand binding site is located in a cleft between the two domains and three tryptophan residues are directly implicated in binding quaternary ammonium groups .

## Biological Role

Component of glycine betaine ABC transporter (complex.ecocyc.ABC-26-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ProU ABC transporter complex involved in glycine betaine and proline betaine uptake. Binds glycine betaine and proline betaine with high affinity. {ECO:0000269|PubMed:14612446, ECO:0000269|PubMed:23249124, ECO:0000269|PubMed:3305496, ECO:0000269|PubMed:7898450}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-26-CPLX|complex.ecocyc.ABC-26-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2679|gene.b2679]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFM2`
- `KEGG:ecj:JW2654;eco:b2679;ecoc:C3026_14760;`
- `GeneID:86860772;947165;`
- `GO:GO:0006972; GO:0016020; GO:0022857; GO:0030288; GO:0031460; GO:0050997; GO:0071470; GO:0089718; GO:1903804; GO:1990222`

## Notes

Glycine betaine/proline betaine-binding periplasmic protein (GBBP)
