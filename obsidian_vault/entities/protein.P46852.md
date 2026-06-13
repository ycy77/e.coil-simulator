---
entity_id: "protein.P46852"
entity_type: "protein"
name: "yhhW"
source_database: "UniProt"
source_id: "P46852"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yhhW b3439 JW3402"
---

# yhhW

`protein.P46852`

## Static

- Type: `protein`
- Source: `UniProt:P46852`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Has quercetin 2,3-dioxygenase activity in vitro. Its physiological role is unknown; however, may provide a mechanism that would avoid inhibition of key cellular proteins, such as DNA gyrase, by quercetin. {ECO:0000269|PubMed:15951572}. YhhW was identified as a Pirin homolog and was shown to have quercetin 2,3-dioxygenase activity, which results in the release of carbon monoxide. Quercetin is a flavonoid, a class of widely occurring compounds synthesized by plants. Possible roles of eukaryotic pirins, including modulation of transcription, DNA replication, or repair, programmed cell death, seed germination and seedling development have been proposed. The physiological role of YhhW in E. coli is unknown. A crystal structure of YhhW has been solved at 2.0 Å resolution. The structure is similar to that of quercetin 2,3-dioxygenase; modelling of potential binding pockets showed that quercetin may be a substrate . Expression of yhhW is induced by exposure to hydroquinone; this induction is abolished in a yhaJ mutant .

## Biological Role

Catalyzes QUERCETIN-23-DIOXYGENASE-RXN (reaction.ecocyc.QUERCETIN-23-DIOXYGENASE-RXN).

## Annotation

FUNCTION: Has quercetin 2,3-dioxygenase activity in vitro. Its physiological role is unknown; however, may provide a mechanism that would avoid inhibition of key cellular proteins, such as DNA gyrase, by quercetin. {ECO:0000269|PubMed:15951572}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.QUERCETIN-23-DIOXYGENASE-RXN|reaction.ecocyc.QUERCETIN-23-DIOXYGENASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3439|gene.b3439]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P46852`
- `KEGG:ecj:JW3402;eco:b3439;ecoc:C3026_18635;`
- `GeneID:93778548;947945;`
- `GO:GO:0008127; GO:0046872`
- `EC:1.13.11.24`

## Notes

Quercetin 2,3-dioxygenase (Quercetinase) (EC 1.13.11.24) (Pirin-like protein YhhW)
