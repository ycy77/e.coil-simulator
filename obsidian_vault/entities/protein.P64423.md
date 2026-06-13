---
entity_id: "protein.P64423"
entity_type: "protein"
name: "zntB"
source_database: "UniProt"
source_id: "P64423"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01565, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:29101379}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01565, ECO:0000269|PubMed:29101379}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "zntB ydaN b1342 JW1336"
---

# zntB

`protein.P64423`

## Static

- Type: `protein`
- Source: `UniProt:P64423`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01565, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:29101379}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01565, ECO:0000269|PubMed:29101379}.

## Enriched Summary

FUNCTION: Zinc transporter (PubMed:29101379). Acts as a Zn(2+):proton symporter, which likely mediates zinc ion uptake (PubMed:29101379). Purified ZntB reconstituted in liposomes also binds and transports Cd(2+), Ni(2+) and Co(2+) (PubMed:29101379). {ECO:0000269|PubMed:29101379}. ZntB is a zinc ion transporter; initial investigations conducted concurrently in E. coli and Salmonella enterica serovar Typhimurium implicated ZntB (formerly YdaN) in zinc efflux while later work characterized it as a Zn2+:proton symporter likely mediating zinc ion uptake. An E. coli strain (GR480) which lacks the 5 known Zn2+ transporters ZntA, ZitB, ZupT, ZnuABC and FieF, but retains ZntB (YdaN), exhibits a greater Zn2+ efflux rate than a strain (RS1220) which lacks all 6 transporters suggesting that ZntB is able to facilitate Zn2+ efflux; expression of the cloned homologous gene from Salmonella enterica increases the rate of Zn2+ efflux in E.coli strain RS1220 . Deletion of zntB in Salmonella enterica increases sensitivity to Zn2+ . ZntB consists of a large N-terminal cytoplasmic domain and two transmembrane helices joined by a periplasmic loop; ZntB forms a symmetrical pentamer with a central transmembrane pore...

## Biological Role

Catalyzes Zn2+:proton symport (reaction.ecocyc.TRANS-RXN-346). Transports Zinc cation (molecule.C00038), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Zinc transporter (PubMed:29101379). Acts as a Zn(2+):proton symporter, which likely mediates zinc ion uptake (PubMed:29101379). Purified ZntB reconstituted in liposomes also binds and transports Cd(2+), Ni(2+) and Co(2+) (PubMed:29101379). {ECO:0000269|PubMed:29101379}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-346|reaction.ecocyc.TRANS-RXN-346]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1342|gene.b1342]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P64423`
- `KEGG:ecj:JW1336;eco:b1342;ecoc:C3026_07860;`
- `GeneID:93775479;945910;`
- `GO:GO:0000287; GO:0005385; GO:0005886; GO:0015087; GO:0015095; GO:0015295; GO:0022883; GO:0050897; GO:0071577; GO:0071578`

## Notes

Zinc transport protein ZntB
