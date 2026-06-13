---
entity_id: "protein.P0AFX4"
entity_type: "protein"
name: "rsd"
source_database: "UniProt"
source_id: "P0AFX4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01181}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rsd b3995 JW3959"
---

# rsd

`protein.P0AFX4`

## Static

- Type: `protein`
- Source: `UniProt:P0AFX4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01181}.

## Enriched Summary

FUNCTION: Binds RpoD and negatively regulates RpoD-mediated transcription activation by preventing the interaction between the primary sigma factor RpoD with the catalytic core of the RNA polymerase and with promoter DNA. May be involved in replacement of the RNA polymerase sigma subunit from RpoD to RpoS during the transition from exponential growth to the stationary phase. {ECO:0000255|HAMAP-Rule:MF_01181, ECO:0000269|PubMed:10368152, ECO:0000269|PubMed:9560209}. Rsd exerts its effect via its ability to specifically interact with a number of proteins, including RPOD-MONOMER σ70 , SPOT-MONOMER SpoT and dephosphorylated PTSH-MONOMER HPr . Rsd was first identified as an anti-σ factor. It binds specifically to the major σ factor RPOD-MONOMER σ70 with a stoichiometry of 1:1 . Rsd sequesters σ70, making RNAP core enzyme accessible for σS and possibly other σ factors in stationary phase . The dephosphorylated form of PTSH-MONOMER HPr is able to form a tight 1:1 complex with Rsd and thereby inhibit its interaction with σ70, linking Rsd anti-σ factor activity to nutrient availability . Rsd interacts directly with the TGS domain of SPOT-MONOMER SpoT and stimulates its (p)ppGpp hydrolase activity; it does not interact with RelA. The stimulatory effect of Rsd on SpoT (p)ppGpp hydrolase activity is negated by the presence of dephosphorylated...

## Annotation

FUNCTION: Binds RpoD and negatively regulates RpoD-mediated transcription activation by preventing the interaction between the primary sigma factor RpoD with the catalytic core of the RNA polymerase and with promoter DNA. May be involved in replacement of the RNA polymerase sigma subunit from RpoD to RpoS during the transition from exponential growth to the stationary phase. {ECO:0000255|HAMAP-Rule:MF_01181, ECO:0000269|PubMed:10368152, ECO:0000269|PubMed:9560209}.

## Outgoing Edges (2)

- `activates` --> [[reaction.ecocyc.PPGPPSYN-RXN|reaction.ecocyc.PPGPPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.RXN0-6427|reaction.ecocyc.RXN0-6427]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `encodes` <-- [[gene.b3995|gene.b3995]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFX4`
- `KEGG:ecj:JW3959;eco:b3995;ecoc:C3026_21580;`
- `GeneID:75169441;75205513;948496;`
- `GO:GO:0001000; GO:0005737; GO:0015968; GO:0016989; GO:0030813; GO:0045892; GO:1903865`

## Notes

Regulator of sigma D
