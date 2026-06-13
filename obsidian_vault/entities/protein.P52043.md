---
entity_id: "protein.P52043"
entity_type: "protein"
name: "scpC"
source_database: "UniProt"
source_id: "P52043"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "scpC ygfH b2920 JW2887"
---

# scpC

`protein.P52043`

## Static

- Type: `protein`
- Source: `UniProt:P52043`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the transfer of coenzyme A from propionyl-CoA to succinate (PubMed:10769117). Could be part of a pathway that converts succinate to propionate (PubMed:10769117). {ECO:0000269|PubMed:10769117}. The scpC-encoded enzyme is a CoA transferase. This reaction is suggested to be part of a pathway of succinate decarboxylation whose metabolic function is unknown . Deletion of scpC increases heterologous production of 6-deoxyerythronolide B (6dEB), the macrolactone precursor of erythromycin .

## Biological Role

Catalyzes RXN0-268 (reaction.ecocyc.RXN0-268).

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of coenzyme A from propionyl-CoA to succinate (PubMed:10769117). Could be part of a pathway that converts succinate to propionate (PubMed:10769117). {ECO:0000269|PubMed:10769117}.

## Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-268|reaction.ecocyc.RXN0-268]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2920|gene.b2920]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52043`
- `KEGG:ecj:JW2887;eco:b2920;ecoc:C3026_16000;`
- `GeneID:947402;`
- `GO:GO:0003986; GO:0006083; GO:0006084; GO:0008775; GO:0043821`
- `EC:2.8.3.27`

## Notes

Propanoyl-CoA:succinate CoA transferase (EC 2.8.3.27) (Propionyl CoA:succinate CoA transferase)
