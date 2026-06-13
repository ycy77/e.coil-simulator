---
entity_id: "protein.P52600"
entity_type: "protein"
name: "emrY"
source_database: "UniProt"
source_id: "P52600"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "emrY b2367 JW2364"
---

# emrY

`protein.P52600`

## Static

- Type: `protein`
- Source: `UniProt:P52600`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Part of the tripartite efflux system EmrYK-TolC, which confers resistance to various drugs. {ECO:0000250}. EmrY is the inner membrane subunit of a putative tripartite efflux pump complex. EmrY is a member of the Drug:H+ Antiporter-2 (14 Spanner) (DHA2) Family within the Major Facilitator Superfamily (MFS) . EmrY has 63.3 % sequence identity with the efflux pump protein EMRB-MONOMER "EmrB" . emrY was identified in a screen for genes that reduce the lethal effects of stress; an emrY insertion mutant is more sensitive than wild type to mitomycin C and other stresses such as UV irradiation . emrY is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function .

## Biological Role

Component of tripartite efflux pump EmrKY-TolC (complex.ecocyc.CPLX0-2161).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of the tripartite efflux system EmrYK-TolC, which confers resistance to various drugs. {ECO:0000250}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2161|complex.ecocyc.CPLX0-2161]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2367|gene.b2367]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52600`
- `KEGG:ecj:JW2364;eco:b2367;ecoc:C3026_13165;`
- `GeneID:93774762;946835;`
- `GO:GO:0005886; GO:0006974; GO:0015721; GO:0022857; GO:0046677; GO:0055085; GO:0098567; GO:0140330; GO:1990281; GO:1990961`

## Notes

Probable multidrug resistance protein EmrY
