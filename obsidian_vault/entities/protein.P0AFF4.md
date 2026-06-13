---
entity_id: "protein.P0AFF4"
entity_type: "protein"
name: "nupG"
source_database: "UniProt"
source_id: "P0AFF4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02049, ECO:0000269|PubMed:15513740, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:3311747, ECO:0000269|PubMed:33640454}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02049, ECO:0000269|PubMed:33640454}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nupG b2964 JW2932"
---

# nupG

`protein.P0AFF4`

## Static

- Type: `protein`
- Source: `UniProt:P0AFF4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02049, ECO:0000269|PubMed:15513740, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:3311747, ECO:0000269|PubMed:33640454}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02049, ECO:0000269|PubMed:33640454}.

## Enriched Summary

FUNCTION: Broad-specificity transporter of purine and pyrimidine nucleosides (PubMed:11466294, PubMed:15513740, PubMed:15678184, PubMed:3311747, PubMed:374403). Can transport adenosine, uridine, thymidine, cytidine, deoxycytidine, guanosine and inosine (PubMed:11466294, PubMed:15513740, PubMed:15678184, PubMed:3311747, PubMed:374403). Can also transport xanthosine, but with a very low affinity (PubMed:11466294). Transport is driven by a proton motive force (PubMed:15513740, PubMed:374403). {ECO:0000269|PubMed:11466294, ECO:0000269|PubMed:15513740, ECO:0000269|PubMed:15678184, ECO:0000269|PubMed:3311747, ECO:0000269|PubMed:374403}. Early studies in E. coli K-12 reported the presence of two different nucleoside transport systems, one of which (gru/nupG) transports all nucleosides and is not affected by the nucleoside antibiotic, showdomycin, and the other (cru/NUPC-MONOMER nupC) which transports pyrimidine and adenine nucleosides and is inhibited by showdomycin . NupG is a broad specificity nucleoside transporter; it mediates uptake of all 6 natural purine/pyrimidine nucleosides . NupG mediated nucleoside transport is inhibited by proton ionophores; transport is driven primarily by the electrical component of the proton motive force . Structural motifs important for ligand binding to NupG and NupC have been investigated...

## Biological Role

Catalyzes adenosine:proton symport (reaction.ecocyc.TRANS-RXN-108A), cytidine:proton symport (reaction.ecocyc.TRANS-RXN-108B), deoxyadenosine:proton symport (reaction.ecocyc.TRANS-RXN-108C), deoxycytidine:proton symport (reaction.ecocyc.TRANS-RXN-108D), deoxyinosine:proton symport (reaction.ecocyc.TRANS-RXN-108E), inosine:proton symport (reaction.ecocyc.TRANS-RXN-108G), thymidine:proton symport (reaction.ecocyc.TRANS-RXN-108H), uridine:proton symport (reaction.ecocyc.TRANS-RXN-108I), and 3 more. Transports Deoxyguanosine (molecule.C00330), Guanosine (molecule.C00387), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Broad-specificity transporter of purine and pyrimidine nucleosides (PubMed:11466294, PubMed:15513740, PubMed:15678184, PubMed:3311747, PubMed:374403). Can transport adenosine, uridine, thymidine, cytidine, deoxycytidine, guanosine and inosine (PubMed:11466294, PubMed:15513740, PubMed:15678184, PubMed:3311747, PubMed:374403). Can also transport xanthosine, but with a very low affinity (PubMed:11466294). Transport is driven by a proton motive force (PubMed:15513740, PubMed:374403). {ECO:0000269|PubMed:11466294, ECO:0000269|PubMed:15513740, ECO:0000269|PubMed:15678184, ECO:0000269|PubMed:3311747, ECO:0000269|PubMed:374403}.

## Outgoing Edges (14)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-108A|reaction.ecocyc.TRANS-RXN-108A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-108B|reaction.ecocyc.TRANS-RXN-108B]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-108C|reaction.ecocyc.TRANS-RXN-108C]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-108D|reaction.ecocyc.TRANS-RXN-108D]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-108E|reaction.ecocyc.TRANS-RXN-108E]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-108G|reaction.ecocyc.TRANS-RXN-108G]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-108H|reaction.ecocyc.TRANS-RXN-108H]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-108I|reaction.ecocyc.TRANS-RXN-108I]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-474|reaction.ecocyc.TRANS-RXN-474]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-475|reaction.ecocyc.TRANS-RXN-475]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-476|reaction.ecocyc.TRANS-RXN-476]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00330|molecule.C00330]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00387|molecule.C00387]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2964|gene.b2964]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFF4`
- `KEGG:ecj:JW2932;eco:b2964;ecoc:C3026_16220;`
- `GeneID:93779027;946282;`
- `GO:GO:0005886; GO:0015212; GO:0015213; GO:0015214; GO:0015506; GO:0015860; GO:0015862; GO:0015864; GO:0032238; GO:1901642`

## Notes

Nucleoside permease NupG (Nucleoside-transport system protein NupG)
