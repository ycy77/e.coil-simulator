---
entity_id: "protein.P0AFF2"
entity_type: "protein"
name: "nupC"
source_database: "UniProt"
source_id: "P0AFF2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:8022285}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nupC cru b2393 JW2389"
---

# nupC

`protein.P0AFF2`

## Static

- Type: `protein`
- Source: `UniProt:P0AFF2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:8022285}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Nucleoside transport protein that can transport adenosine, uridine, thymidine, cytidine and deoxycytidine (PubMed:11466294, PubMed:14668133, PubMed:15678184, PubMed:374403). Shows weak activity with inosine and xanthosine (PubMed:11466294, PubMed:14668133). Transport is driven by a proton motive force (PubMed:14668133, PubMed:374403). Does not transport guanosine, deoxyguanosine, hypoxanthine or uracil (PubMed:14668133, PubMed:374403). Also shows activity with the chemotherapeutic drugs 3'-azido-3'-deoxythymidine (AZT), 2',3'- dideoxycytidine (ddC) and 2'-deoxy-2',2'-difluorocytidine (gemcitabine) (PubMed:14668133). {ECO:0000269|PubMed:11466294, ECO:0000269|PubMed:14668133, ECO:0000269|PubMed:15678184, ECO:0000269|PubMed:374403}. Early studies in E. coli K-12 reported the presence of two different nucleoside transport systems, one of which (cru/nupC) transports pyrimidine and adenine nucleosides and is inhibited by the nucleoside antibiotic showdomycin, and the other (gru/NUPG-MONOMER nupG) which transports all nucleosides and is not affected by showdomycin . NupC mediates proton-dependent uptake of the nucleosides, (deoxy)cytidine, thymidine, uridine and (deoxy)adenosine but does not transport guanosine; it is also able to transport inosine and the nucleoside drugs 3'-azido-3'-deoxythymidine (AZT) and 5'-azacytidine...

## Biological Role

Catalyzes adenosine:proton symport (reaction.ecocyc.TRANS-RXN-108A), cytidine:proton symport (reaction.ecocyc.TRANS-RXN-108B), deoxyadenosine:proton symport (reaction.ecocyc.TRANS-RXN-108C), deoxycytidine:proton symport (reaction.ecocyc.TRANS-RXN-108D), deoxyinosine:proton symport (reaction.ecocyc.TRANS-RXN-108E), deoxyuridine:proton symport (reaction.ecocyc.TRANS-RXN-108F), inosine:proton symport (reaction.ecocyc.TRANS-RXN-108G), thymidine:proton symport (reaction.ecocyc.TRANS-RXN-108H), and 2 more. Transports Adenosine (molecule.C00212), Thymidine (molecule.C00214), Inosine (molecule.C00294), Uridine (molecule.C00299), Cytidine (molecule.C00475), Deoxyuridine (molecule.C00526), Deoxyadenosine (molecule.C00559), Deoxycytidine (molecule.C00881), and 2 more.

## Annotation

FUNCTION: Nucleoside transport protein that can transport adenosine, uridine, thymidine, cytidine and deoxycytidine (PubMed:11466294, PubMed:14668133, PubMed:15678184, PubMed:374403). Shows weak activity with inosine and xanthosine (PubMed:11466294, PubMed:14668133). Transport is driven by a proton motive force (PubMed:14668133, PubMed:374403). Does not transport guanosine, deoxyguanosine, hypoxanthine or uracil (PubMed:14668133, PubMed:374403). Also shows activity with the chemotherapeutic drugs 3'-azido-3'-deoxythymidine (AZT), 2',3'- dideoxycytidine (ddC) and 2'-deoxy-2',2'-difluorocytidine (gemcitabine) (PubMed:14668133). {ECO:0000269|PubMed:11466294, ECO:0000269|PubMed:14668133, ECO:0000269|PubMed:15678184, ECO:0000269|PubMed:374403}.

## Outgoing Edges (20)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-108A|reaction.ecocyc.TRANS-RXN-108A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-108B|reaction.ecocyc.TRANS-RXN-108B]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-108C|reaction.ecocyc.TRANS-RXN-108C]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-108D|reaction.ecocyc.TRANS-RXN-108D]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-108E|reaction.ecocyc.TRANS-RXN-108E]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-108F|reaction.ecocyc.TRANS-RXN-108F]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-108G|reaction.ecocyc.TRANS-RXN-108G]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-108H|reaction.ecocyc.TRANS-RXN-108H]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-108I|reaction.ecocyc.TRANS-RXN-108I]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-476|reaction.ecocyc.TRANS-RXN-476]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00212|molecule.C00212]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00214|molecule.C00214]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00294|molecule.C00294]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00299|molecule.C00299]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00475|molecule.C00475]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00526|molecule.C00526]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00559|molecule.C00559]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00881|molecule.C00881]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C05512|molecule.C05512]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2393|gene.b2393]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFF2`
- `KEGG:ecj:JW2389;eco:b2393;ecoc:C3026_13300;`
- `GeneID:75172511;75202539;946895;`
- `GO:GO:0005886; GO:0015212; GO:0015213; GO:0015506; GO:1901642`

## Notes

Nucleoside permease NupC (Nucleoside-transport system protein NupC)
