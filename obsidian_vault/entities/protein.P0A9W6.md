---
entity_id: "protein.P0A9W6"
entity_type: "protein"
name: "ibaG"
source_database: "UniProt"
source_id: "P0A9W6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ibaG yrbA b3190 JW3157"
---

# ibaG

`protein.P0A9W6`

## Static

- Type: `protein`
- Source: `UniProt:P0A9W6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in cell resistance against acid stress. {ECO:0000269|PubMed:22534295}. When IbaG is co-expressed with Grx4, it can form a [2Fe-2S] cluster-bridged Grx4-IbaG heterodimer, within which it destabilizes the interaction of Grx4 with the iron-sulfur cluster. Within the Grx4-IbaG complex, His63 of IbaG is involved in coordinating the [2Fe-2S] cluster. In the absence of Grx4, IbaG appears to be unable to bind an Fe-S cluster. Heterodimerization with Grx4 is independent of the [2Fe-2S] cluster . IbaG may play a role in the assembly or stability of NADH-DHI-CPLX . Expression of ibaG is increased by acid stress. An ibaG deletion mutant is slightly more sensitive to acid stress than wild type . IbaG: "influenced by acid gene"

## Biological Role

Component of Grx4-IbaG complex (complex.ecocyc.CPLX0-8239).

## Annotation

FUNCTION: Involved in cell resistance against acid stress. {ECO:0000269|PubMed:22534295}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8239|complex.ecocyc.CPLX0-8239]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3190|gene.b3190]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9W6`
- `KEGG:ecj:JW3157;eco:b3190;ecoc:C3026_17365;`
- `GeneID:93778791;947958;`
- `GO:GO:0005829; GO:0006879; GO:0016226; GO:0045454; GO:0051537; GO:0097533; GO:1990229`

## Notes

Acid stress protein IbaG
