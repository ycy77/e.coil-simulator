---
entity_id: "protein.P39276"
entity_type: "protein"
name: "dtpC"
source_database: "UniProt"
source_id: "P39276"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dtpC yjdL b4130 JW4091"
---

# dtpC

`protein.P39276`

## Static

- Type: `protein`
- Source: `UniProt:P39276`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Proton-dependent permease that transports di- and tripeptides. Shows significantly higher specificity towards dipeptides than tripeptides. Has a preference for dipeptides with a C-terminal Lys residue. Can bind Ala-Lys, Lys-Ala, Ala-Ala. Can also transport alanine and trialanine. {ECO:0000269|PubMed:19703419, ECO:0000269|PubMed:21933132, ECO:0000269|PubMed:22940668, ECO:0000269|PubMed:24440353}. The DtpC protein is a member of the POT (proton-dependent oligopeptide transporter) family of peptide transporters . DtpC transports dialanine, trialanine, alanine and the lysine analogue, aminohexanoic acid in vitro DtpC has a higher specificity towards dipeptides compared to tripeptides and displays a preference for dipeptides with a C-terminal lysine residue . Direct binding of Ala-Lys dipeptides to purified protein has been reported. Binding of the tripeptide Ala-Ala-Lys and the dipeptide Ala-Gln to the purified protein was not detected . Binding of Ala-Lys to a DtpCE388Q variant could not be detected in agreement with the observation that glutamic acid 388 may play a role in ligand binding . A high resolution cryo-EM structure of DtpC provides insight into the basis for ligand preference . DtpC is predicted to contain 14 transmembrane regions with the C-terminus located in the cytoplasm . dtpC: dipeptide tripeptide permease C

## Biological Role

Catalyzes tripeptide:proton symport (reaction.ecocyc.TRANS-RXN0-267), dipeptide:proton symport (reaction.ecocyc.TRANS-RXN0-288). Transports hν (molecule.ecocyc.Light), a tripeptide (molecule.ecocyc.TRIPEPTIDES).

## Annotation

FUNCTION: Proton-dependent permease that transports di- and tripeptides. Shows significantly higher specificity towards dipeptides than tripeptides. Has a preference for dipeptides with a C-terminal Lys residue. Can bind Ala-Lys, Lys-Ala, Ala-Ala. Can also transport alanine and trialanine. {ECO:0000269|PubMed:19703419, ECO:0000269|PubMed:21933132, ECO:0000269|PubMed:22940668, ECO:0000269|PubMed:24440353}.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-267|reaction.ecocyc.TRANS-RXN0-267]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-288|reaction.ecocyc.TRANS-RXN0-288]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.TRIPEPTIDES|molecule.ecocyc.TRIPEPTIDES]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b4130|gene.b4130]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39276`
- `KEGG:ecj:JW4091;eco:b4130;ecoc:C3026_22325;`
- `GeneID:948644;`
- `GO:GO:0005886; GO:0015031; GO:0015078; GO:0015333; GO:0035442; GO:0035443; GO:0042937; GO:0071916; GO:1902600`

## Notes

Dipeptide and tripeptide permease C (Dipeptide/tripeptide:H(+) symporter DtpC)
