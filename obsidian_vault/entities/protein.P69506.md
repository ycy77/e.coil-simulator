---
entity_id: "protein.P69506"
entity_type: "protein"
name: "ytfE"
source_database: "UniProt"
source_id: "P69506"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ytfE b4209 JW4167"
---

# ytfE

`protein.P69506`

## Static

- Type: `protein`
- Source: `UniProt:P69506`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Di-iron-containing protein involved in the repair of iron-sulfur clusters damaged by oxidative and nitrosative stress conditions. {ECO:0000269|PubMed:16553864, ECO:0000269|PubMed:17289666, ECO:0000269|PubMed:18357473}. YtfE belongs to a conserved and widely distributed family of hemerythrin-like proteins. Purified YtfE contains a non-heme di-iron center of the histidine-carboxylate type . Based on spectroscopic, mass spectrometric and kinetic approaches, YtfE is considered to belong to a new class of nitrite reductases . YtfE appears to be involved in the repair of iron centers . YtfE is able to donate iron for the assembly of an Fe-S cluster into apo-G7324-MONOMER IscU but only under conditions that degrade its di-iron center . YtfE can also act as a nitric oxide scavenger that catalyzes the reduction of nitric oxide (NO) to nitrous oxide (N2O) . Genetic interaction experiments suggest that YtfE releases NO from nitrosylation-damaged metalloproteins, with subsequent reduction of NO to N2O by the G6457-MONOMER hybrid cluster protein . Similarly, in the absence of EG11415-MONOMER Dps, YtfE increases the intracellular levels of reactive oxygen species . Exposure of YtfE to oxygen leads to dimerization via the formation of intermolecular disulfide bridges between C30 or C31 in the N-terminal domain of the protein...

## Biological Role

Catalyzes RXN-23850 (reaction.ecocyc.RXN-23850).

## Annotation

FUNCTION: Di-iron-containing protein involved in the repair of iron-sulfur clusters damaged by oxidative and nitrosative stress conditions. {ECO:0000269|PubMed:16553864, ECO:0000269|PubMed:17289666, ECO:0000269|PubMed:18357473}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-23850|reaction.ecocyc.RXN-23850]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4209|gene.b4209]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69506`
- `KEGG:ecj:JW4167;eco:b4209;ecoc:C3026_22735;`
- `GeneID:93777612;948724;`
- `GO:GO:0005506; GO:0005829; GO:0006979; GO:0030091; GO:0051409; GO:0098809`

## Notes

Iron-sulfur cluster repair protein YtfE (Regulator of cell morphogenesis and NO signaling) (RCMNS)
