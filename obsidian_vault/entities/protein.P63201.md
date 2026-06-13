---
entity_id: "protein.P63201"
entity_type: "protein"
name: "gadW"
source_database: "UniProt"
source_id: "P63201"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gadW yhiW b3515 JW3483"
---

# gadW

`protein.P63201`

## Static

- Type: `protein`
- Source: `UniProt:P63201`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Depending on the conditions (growth phase and medium), acts as a positive or negative regulator of gadA and gadBC. Repression occurs directly or via the repression of the expression of gadX. Activation occurs directly by the binding of GadW to the gadA and gadBC promoters. {ECO:0000269|PubMed:12446650, ECO:0000269|PubMed:12730179, ECO:0000269|PubMed:14617649}. The transcription factor GadW, for "Glutamic acid decarboxylase," is negatively autoregulated and controls the transcription of the genes involved in the principal acid resistance system, is glutamate dependent (GAD), and is also referred to as the GAD system . In addition, GadW also activates the transcription of the central activator involved in the acid response . The physiological inducer is unknown. Richard et al. proposed that GadW can sense intracellular Na+ concentrations, but the mechanism is not known . The activity of the GadW iModulon decreases in cells evolved on glycerol and lactate as carbon sources . GadW is one of the regulators in the acid resistance system and is encoded by the unusual gadXW operon, which is located in the region called the acid fitness island . This operon encodes two transcriptional regulators, GadX and GadW, both of which are members of the AraC/XylS family of transcriptional regulators...

## Annotation

FUNCTION: Depending on the conditions (growth phase and medium), acts as a positive or negative regulator of gadA and gadBC. Repression occurs directly or via the repression of the expression of gadX. Activation occurs directly by the binding of GadW to the gadA and gadBC promoters. {ECO:0000269|PubMed:12446650, ECO:0000269|PubMed:12730179, ECO:0000269|PubMed:14617649}.

## Outgoing Edges (12)

- `activates` --> [[gene.b1492|gene.b1492]] `RegulonDB` `S` - regulator=GadW; target=gadC; function=-+
- `activates` --> [[gene.b1493|gene.b1493]] `RegulonDB` `S` - regulator=GadW; target=gadB; function=-+
- `activates` --> [[gene.b3508|gene.b3508]] `RegulonDB` `S` - regulator=GadW; target=yhiD; function=-+
- `activates` --> [[gene.b3510|gene.b3510]] `RegulonDB` `S` - regulator=GadW; target=hdeA; function=-+
- `activates` --> [[gene.b3516|gene.b3516]] `RegulonDB` `S` - regulator=GadW; target=gadX; function=-+
- `activates` --> [[gene.b3517|gene.b3517]] `RegulonDB` `S` - regulator=GadW; target=gadA; function=-+
- `represses` --> [[gene.b1492|gene.b1492]] `RegulonDB` `S` - regulator=GadW; target=gadC; function=-+
- `represses` --> [[gene.b1493|gene.b1493]] `RegulonDB` `S` - regulator=GadW; target=gadB; function=-+
- `represses` --> [[gene.b3508|gene.b3508]] `RegulonDB` `S` - regulator=GadW; target=yhiD; function=-+
- `represses` --> [[gene.b3510|gene.b3510]] `RegulonDB` `S` - regulator=GadW; target=hdeA; function=-+
- `represses` --> [[gene.b3516|gene.b3516]] `RegulonDB` `S` - regulator=GadW; target=gadX; function=-+
- `represses` --> [[gene.b3517|gene.b3517]] `RegulonDB` `S` - regulator=GadW; target=gadA; function=-+

## Incoming Edges (1)

- `encodes` <-- [[gene.b3515|gene.b3515]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P63201`
- `KEGG:ecj:JW3483;eco:b3515;ecoc:C3026_19045;`
- `GeneID:948029;`
- `GO:GO:0000976; GO:0003677; GO:0003700; GO:0006351; GO:0006355; GO:0006974`

## Notes

HTH-type transcriptional regulator GadW
