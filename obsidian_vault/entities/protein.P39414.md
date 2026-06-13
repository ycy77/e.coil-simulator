---
entity_id: "protein.P39414"
entity_type: "protein"
name: "ttdT"
source_database: "UniProt"
source_id: "P39414"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ttdT ygjC ygjE b3063 JW3035"
---

# ttdT

`protein.P39414`

## Static

- Type: `protein`
- Source: `UniProt:P39414`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Catalyzes the uptake of tartrate in exchange for intracellular succinate. Essential for anaerobic L-tartrate fermentation. {ECO:0000269|PubMed:17172328}. TtdT is a putative tartrate/succinate antiporter belonging to the DASS family of di- and tri-carboxylic acid transporters. ttdT is located in a probable operon with the ttdAB genes encoding L-tartrate dehydratase. In an analogous manner to CitT , under anaerobic conditions TtdT allows the uptake of L-tartrate in exchange for succinate, the end product of tartrate fermentation. In strains lacking anaerobic C4-dicarboxylate antiporters and CitT, TtdT is required for tartrate fermentation as tartrate uptake in ttdT mutants is normal, but tartrate/succinate antiport does not occur . Tartrate is taken up in ttdT mutants by some other mechanism, possibly YeaV or YfaV . ttdABT transcription is controlled by YgiP, a LysR-type transcriptional regulator; tartrate-dependent induction of the ttdABT operon requires YgiP .

## Biological Role

Catalyzes L-tartrate:succinate antiport (reaction.ecocyc.TRANS-RXN-127). Transports Succinate (molecule.C00042), (R,R)-Tartaric acid (molecule.C00898).

## Annotation

FUNCTION: Catalyzes the uptake of tartrate in exchange for intracellular succinate. Essential for anaerobic L-tartrate fermentation. {ECO:0000269|PubMed:17172328}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-127|reaction.ecocyc.TRANS-RXN-127]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00898|molecule.C00898]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3063|gene.b3063]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39414`
- `KEGG:ecj:JW3035;eco:b3063;ecoc:C3026_16735;`
- `GeneID:947576;`
- `GO:GO:0005886; GO:0015516; GO:0015745`

## Notes

L-tartrate/succinate antiporter (Tartrate carrier) (Tartrate transporter)
