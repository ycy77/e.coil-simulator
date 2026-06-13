---
entity_id: "protein.P28629"
entity_type: "protein"
name: "adiA"
source_database: "UniProt"
source_id: "P28629"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "adiA adi b4117 JW5731"
---

# adiA

`protein.P28629`

## Static

- Type: `protein`
- Source: `UniProt:P28629`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Component of the acid-resistance (AR) system allowing enteric pathogens to survive the acidic environment in the stomach (Probable). ADC can be found in two forms: biodegradative (this enzyme) and biosynthetic (speA). The biodegradative form plays a role in regulating pH by consuming proteins. Converts arginine imported by AdiC to agmatine which is then exported by AdiC (Probable). {ECO:0000305|PubMed:12867448, ECO:0000305|PubMed:19298070}.

## Biological Role

Catalyzes L-arginine carboxy-lyase (agmatine-forming) (reaction.R00566). Component of arginine decarboxylase, degradative (complex.ecocyc.ARGDECARBOXDEG-CPLX).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Component of the acid-resistance (AR) system allowing enteric pathogens to survive the acidic environment in the stomach (Probable). ADC can be found in two forms: biodegradative (this enzyme) and biosynthetic (speA). The biodegradative form plays a role in regulating pH by consuming proteins. Converts arginine imported by AdiC to agmatine which is then exported by AdiC (Probable). {ECO:0000305|PubMed:12867448, ECO:0000305|PubMed:19298070}.

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00566|reaction.R00566]] `KEGG` `database` - via EC:4.1.1.19
- `is_component_of` --> [[complex.ecocyc.ARGDECARBOXDEG-CPLX|complex.ecocyc.ARGDECARBOXDEG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## Incoming Edges (1)

- `encodes` <-- [[gene.b4117|gene.b4117]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P28629`
- `KEGG:ecj:JW5731;eco:b4117;`
- `GeneID:948638;`
- `GO:GO:0005829; GO:0006527; GO:0008792; GO:0030170; GO:0051454`
- `EC:4.1.1.19`

## Notes

Biodegradative arginine decarboxylase (ADC) (EC 4.1.1.19)
