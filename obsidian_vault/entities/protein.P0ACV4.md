---
entity_id: "protein.P0ACV4"
entity_type: "protein"
name: "lapA"
source_database: "UniProt"
source_id: "P0ACV4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01948, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:24722986}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01948}. Note=Copurifies with LptE/LptD, LptBFGC, LptA, DnaK/DnaJ and LPS. {ECO:0000269|PubMed:24722986}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lapA yciS b1279 JW1271"
---

# lapA

`protein.P0ACV4`

## Static

- Type: `protein`
- Source: `UniProt:P0ACV4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01948, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:24722986}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01948}. Note=Copurifies with LptE/LptD, LptBFGC, LptA, DnaK/DnaJ and LPS. {ECO:0000269|PubMed:24722986}.

## Enriched Summary

FUNCTION: Involved in the assembly of lipopolysaccharide (LPS). {ECO:0000255|HAMAP-Rule:MF_01948, ECO:0000269|PubMed:24722986}. lapA is generally not essential. ΔlapA strains do not grow on MacConkey agar at 43°C. LapA copurifies with LapB, DnaK, DnaJ and with the LPS transport system proteins (LptE/D, LptBFGC, LptA). Purified LapA contains lipopolysaccharide (LPS) . lapAB transcription is subject to heat shock induction via an RpoH-regulated promoter located upstream of lapA . LapA is an inner membrane protein with two predicted transmembrane domains. The C terminus is located in the cytoplasm . LapA was identified in a phylogenetic screen that found proteins containing domains that only occur in organisms that also contain a EG10204-MONOMER Dam methyltransferase . LapA: lipopolysaccharide assembly protein A

## Annotation

FUNCTION: Involved in the assembly of lipopolysaccharide (LPS). {ECO:0000255|HAMAP-Rule:MF_01948, ECO:0000269|PubMed:24722986}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1279|gene.b1279]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACV4`
- `KEGG:ecj:JW1271;eco:b1279;ecoc:C3026_07510;`
- `GeneID:75203392;944936;`
- `GO:GO:0005886; GO:0008653`

## Notes

Lipopolysaccharide assembly protein A
