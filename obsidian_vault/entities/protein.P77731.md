---
entity_id: "protein.P77731"
entity_type: "protein"
name: "allA"
source_database: "UniProt"
source_id: "P77731"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "allA glxA2 ybbT b0505 JW0493"
---

# allA

`protein.P77731`

## Static

- Type: `protein`
- Source: `UniProt:P77731`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the catabolism of the allantoin degradation intermediate (S)-ureidoglycolate, generating urea and glyoxylate. Involved in the anaerobic utilization of allantoin as sole nitrogen source. Reinforces the induction of genes involved in the degradation of allantoin and glyoxylate by producing glyoxylate. {ECO:0000255|HAMAP-Rule:MF_00616, ECO:0000269|PubMed:10601204, ECO:0000269|PubMed:24107613}. Ureidoglycolate lyase catalyzes the conversion of ureidoglycolate to glyoxylate and urea . E. coli is able to utilize allantoin as a sole source of nitrogen under anaerobic conditions, but can not utilize it as a sole source of carbon. An allA mutant is not impaired in the utilization of allantoin . Ureidoglycolate lyase activity is slightly induced by growth on allantoin as the sole source of nitrogen . Transcription of allA is induced by growth on glyoxylate .

## Biological Role

Catalyzes (S)-ureidoglycolate urea-lyase (glyoxylate-forming) (reaction.R00776), UREIDOGLYCOLATE-LYASE-RXN (reaction.ecocyc.UREIDOGLYCOLATE-LYASE-RXN). Bound by Nickel(2+) (molecule.C19609).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the catabolism of the allantoin degradation intermediate (S)-ureidoglycolate, generating urea and glyoxylate. Involved in the anaerobic utilization of allantoin as sole nitrogen source. Reinforces the induction of genes involved in the degradation of allantoin and glyoxylate by producing glyoxylate. {ECO:0000255|HAMAP-Rule:MF_00616, ECO:0000269|PubMed:10601204, ECO:0000269|PubMed:24107613}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00776|reaction.R00776]] `KEGG` `database` - via EC:4.3.2.3
- `catalyzes` --> [[reaction.ecocyc.UREIDOGLYCOLATE-LYASE-RXN|reaction.ecocyc.UREIDOGLYCOLATE-LYASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0505|gene.b0505]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77731`
- `KEGG:ecj:JW0493;eco:b0505;ecoc:C3026_02480;`
- `GeneID:945141;`
- `GO:GO:0000256; GO:0004848; GO:0006145; GO:0050385`
- `EC:4.3.2.3`

## Notes

Ureidoglycolate lyase (EC 4.3.2.3) (Ureidoglycolatase) (Ureidoglycolate hydrolase)
