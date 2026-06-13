---
entity_id: "protein.P31552"
entity_type: "protein"
name: "caiC"
source_database: "UniProt"
source_id: "P31552"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "caiC yaaM b0037 JW0036"
---

# caiC

`protein.P31552`

## Static

- Type: `protein`
- Source: `UniProt:P31552`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the transfer of CoA to carnitine, generating the initial carnitinyl-CoA needed for the CaiB reaction cycle. Also has activity toward crotonobetaine and gamma-butyrobetaine. {ECO:0000255|HAMAP-Rule:MF_01524, ECO:0000269|PubMed:18266698}. Carnitine-CoA ligase (CaiC) catalyzes the transfer of CoA to carnitine. CaiC was initially predicted to have CoA ligase activity by . In vitro, the enzyme can utilize both L- and D-carnitine as well as crotonobetaine and γ-butyrobetaine as substrates. CaiC also exhibits a CoA-transferase-like activity in vitro, which can not substitute for CaiB activity in vivo .

## Biological Role

Catalyzes LCARNCOALIG-RXN (reaction.ecocyc.LCARNCOALIG-RXN).

## Annotation

FUNCTION: Catalyzes the transfer of CoA to carnitine, generating the initial carnitinyl-CoA needed for the CaiB reaction cycle. Also has activity toward crotonobetaine and gamma-butyrobetaine. {ECO:0000255|HAMAP-Rule:MF_01524, ECO:0000269|PubMed:18266698}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.LCARNCOALIG-RXN|reaction.ecocyc.LCARNCOALIG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0037|gene.b0037]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31552`
- `KEGG:ecj:JW0036;eco:b0037;ecoc:C3026_00195;`
- `GeneID:944886;`
- `GO:GO:0009437; GO:0016878; GO:0051108; GO:0051109`
- `EC:6.2.1.48`

## Notes

Crotonobetaine/carnitine--CoA ligase (EC 6.2.1.48) (Betaine:CoA ligase)
