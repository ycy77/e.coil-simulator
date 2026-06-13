---
entity_id: "protein.P0AC19"
entity_type: "protein"
name: "folX"
source_database: "UniProt"
source_id: "P0AC19"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "folX b2303 JW2300"
---

# folX

`protein.P0AC19`

## Static

- Type: `protein`
- Source: `UniProt:P0AC19`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the epimerization of carbon 2' of the side chain of 7,8-dihydroneopterin triphosphate (H2NTP) to form 7,8-dihydromonapterin triphosphate (H2MTP) (PubMed:9182560, PubMed:9651328). Is required for tetrahydromonapterin biosynthesis, a major pterin in E.coli (PubMed:19897652). {ECO:0000269|PubMed:19897652, ECO:0000269|PubMed:9182560, ECO:0000269|PubMed:9651328}.

## Biological Role

Component of dihydroneopterin triphosphate 2'-epimerase (complex.ecocyc.FOLXTET-CPLX).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Annotation

FUNCTION: Catalyzes the epimerization of carbon 2' of the side chain of 7,8-dihydroneopterin triphosphate (H2NTP) to form 7,8-dihydromonapterin triphosphate (H2MTP) (PubMed:9182560, PubMed:9651328). Is required for tetrahydromonapterin biosynthesis, a major pterin in E.coli (PubMed:19897652). {ECO:0000269|PubMed:19897652, ECO:0000269|PubMed:9182560, ECO:0000269|PubMed:9651328}.

## Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.FOLXTET-CPLX|complex.ecocyc.FOLXTET-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## Incoming Edges (1)

- `encodes` <-- [[gene.b2303|gene.b2303]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC19`
- `KEGG:ecj:JW2300;eco:b2303;ecoc:C3026_12845;`
- `GeneID:93774871;946781;`
- `GO:GO:0004150; GO:0005737; GO:0005829; GO:0006760; GO:0008719; GO:0042559; GO:0042802`
- `EC:5.1.99.7`

## Notes

Dihydroneopterin triphosphate 2'-epimerase (EC 5.1.99.7) (D-erythro-7,8-dihydroneopterin triphosphate epimerase)
