---
entity_id: "protein.Q47679"
entity_type: "protein"
name: "yafV"
source_database: "UniProt"
source_id: "Q47679"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yafV b0219 JW5019"
---

# yafV

`protein.Q47679`

## Static

- Type: `protein`
- Source: `UniProt:Q47679`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Hydrolyzes alpha-ketoglutaramate (a-KGM) to alpha-ketoglutarate (alpha-KG) and ammonia, has weak activity on L-glutamine, almost no activity on deaminated glutathione (dGSH) and none on glutathione (By similarity). May function as a metabolite repair enzyme (By similarity). {ECO:0000250|UniProtKB:A0A140NDS5}. YafV is an ω-amidase that may function as a metabolite repair enzyme. α-ketoglutaramate (α-KGM) is the product of a potential side reaction of glutamine aminotransferases. The purified recombinant YafV expressed from an ASKA clone showed high activity toward α-KGM .

## Biological Role

Catalyzes 2-oxoglutaramate amidohydrolase (reaction.R00269), 2-oxosuccinamate amidohydrolase (reaction.R00348), RXN-13072 (reaction.ecocyc.RXN-13072).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Hydrolyzes alpha-ketoglutaramate (a-KGM) to alpha-ketoglutarate (alpha-KG) and ammonia, has weak activity on L-glutamine, almost no activity on deaminated glutathione (dGSH) and none on glutathione (By similarity). May function as a metabolite repair enzyme (By similarity). {ECO:0000250|UniProtKB:A0A140NDS5}.

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00269|reaction.R00269]] `KEGG` `database` - via EC:3.5.1.3
- `catalyzes` --> [[reaction.R00348|reaction.R00348]] `KEGG` `database` - via EC:3.5.1.3
- `catalyzes` --> [[reaction.ecocyc.RXN-13072|reaction.ecocyc.RXN-13072]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0219|gene.b0219]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q47679`
- `KEGG:ecj:JW5019;eco:b0219;ecoc:C3026_01035;`
- `GeneID:946585;`
- `GO:GO:0050152; GO:0106008`
- `EC:3.5.1.3`

## Notes

Omega-amidase YafV (EC 3.5.1.3)
