---
entity_id: "protein.P15081"
entity_type: "protein"
name: "gutM"
source_database: "UniProt"
source_id: "P15081"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gutM srlM b2706 JW2675"
---

# gutM

`protein.P15081`

## Static

- Type: `protein`
- Source: `UniProt:P15081`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Positive regulator for glucitol operon expression. The "glucitol regulator," GutM, is a DNA-binding transcription factor that regulates an operon (gut) involved in transport and utilization of glucitol . This regulator is located in the unusual gut operon, which contains two glucitol-specific transcription factors, GutR and GutM, that regulate this operon negatively and positively, respectively; both regulators control transcription of glucitol PTS permease . Expression of gutM is increased in the presence of glucitol and in the absence of glucose. Although GutM binding does not depend on the presence of glucitol, this compound appears to be necessary for derepressing gutM, perhaps by interacting with GutR . To activate transcription, GutM recognizes DNA-binding sites, but no consensus sequence has been identified. When this protein activates genes involved in glucitol transport and utilization, it appears to bind to their regulatory regions without a coeffector . In addition, Yamada et al. suggested that the regulators GutM and GutR have contrary effects; in the absence of glucitol, GutR represses transcription of the gut operon, and in the presence of glucitol, GutR interacts with this carbohydrate to dissociate from DNA, causing increases of GutM in sufficient amounts to increase transcription of the gut operon...

## Annotation

FUNCTION: Positive regulator for glucitol operon expression.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b2706|gene.b2706]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15081`
- `KEGG:ecj:JW2675;eco:b2706;ecoc:C3026_14895;`
- `GeneID:93779305;948938;`
- `GO:GO:0003677; GO:0006355; GO:0009401`

## Notes

Glucitol operon activator protein
