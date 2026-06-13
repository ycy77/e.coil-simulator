---
entity_id: "protein.P0C8J6"
entity_type: "protein"
name: "gatY"
source_database: "UniProt"
source_id: "P0C8J6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gatY yegF b2096 JW5343"
---

# gatY

`protein.P0C8J6`

## Static

- Type: `protein`
- Source: `UniProt:P0C8J6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalytic subunit of the tagatose-1,6-bisphosphate aldolase GatYZ, which catalyzes the reversible aldol condensation of dihydroxyacetone phosphate (DHAP or glycerone-phosphate) with glyceraldehyde 3-phosphate (G3P) to produce tagatose 1,6-bisphosphate (TBP) (PubMed:11976750, PubMed:8955298). Requires GatZ subunit for full activity and stability (PubMed:11976750). Is involved in the catabolism of galactitol (PubMed:11976750, PubMed:8955298). Has a high aldolase activity for TBP and a very low one for fructose 1,6-bisphosphate (FBP) (PubMed:11976750). {ECO:0000269|PubMed:11976750, ECO:0000269|PubMed:8955298}. There are two distinct tagatose-1,6-bisphosphate aldolases in E. coli, the EG12768 kbaY-encoded aldolase 1 and the EG12419 gatY-encoded aldolase 2, both of which participate in galactitol catabolism. They catalyze the reversible aldol condensation of glycerone phosphate (dihydroxyacetone phosphate) with D-glyceraldehyde 3-phosphate to form tagatose 1,6-bisphosphate . The G7128-MONOMER GatZ protein has no catalytic activity, but appears to stabilize GatY, is required for full activity of GatY, and thus may have a chaperone-like function . The gatYZABCDR operon appears to be constitutively expressed due to an IS3E insertion in the gatR repressor . Proteomics studies showed increased levels of GatY in response to low pH and acetate stress...

## Biological Role

Catalyzes TAGAALDOL-RXN (reaction.ecocyc.TAGAALDOL-RXN).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalytic subunit of the tagatose-1,6-bisphosphate aldolase GatYZ, which catalyzes the reversible aldol condensation of dihydroxyacetone phosphate (DHAP or glycerone-phosphate) with glyceraldehyde 3-phosphate (G3P) to produce tagatose 1,6-bisphosphate (TBP) (PubMed:11976750, PubMed:8955298). Requires GatZ subunit for full activity and stability (PubMed:11976750). Is involved in the catabolism of galactitol (PubMed:11976750, PubMed:8955298). Has a high aldolase activity for TBP and a very low one for fructose 1,6-bisphosphate (FBP) (PubMed:11976750). {ECO:0000269|PubMed:11976750, ECO:0000269|PubMed:8955298}.

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TAGAALDOL-RXN|reaction.ecocyc.TAGAALDOL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2096|gene.b2096]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0C8J6`
- `KEGG:ecj:JW5343;eco:b2096;ecoc:C3026_11765;`
- `GeneID:946636;`
- `GO:GO:0005829; GO:0008270; GO:0009025; GO:0019404; GO:1902494; GO:2001059`
- `EC:4.1.2.40`

## Notes

D-tagatose-1,6-bisphosphate aldolase subunit GatY (TBPA) (TagBP aldolase) (EC 4.1.2.40) (D-tagatose-bisphosphate aldolase class II) (Tagatose-bisphosphate aldolase)
