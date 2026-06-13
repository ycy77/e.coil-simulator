---
entity_id: "protein.P69380"
entity_type: "protein"
name: "fieF"
source_database: "UniProt"
source_id: "P69380"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01425, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16049012, ECO:0000269|PubMed:19749753}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01425, ECO:0000269|PubMed:16049012, ECO:0000269|PubMed:19749753}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fieF yiiP b3915 JW3886"
---

# fieF

`protein.P69380`

## Static

- Type: `protein`
- Source: `UniProt:P69380`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01425, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16049012, ECO:0000269|PubMed:19749753}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01425, ECO:0000269|PubMed:16049012, ECO:0000269|PubMed:19749753}.

## Enriched Summary

FUNCTION: Divalent metal cation transporter which exports Zn(2+), Cd(2+) and possibly Fe(2+) (PubMed:14960568, PubMed:15549269, PubMed:16049012, PubMed:16790427, PubMed:19749753, PubMed:22529353). May be involved in zinc and iron detoxification by efflux (PubMed:15549269, PubMed:19749753). In vitro, can also bind, but probably not transport, Hg(2+), Co(2+), Ni(2+), Mn(2+), Ca(2+) and Mg(2+) (PubMed:14960568, PubMed:16049012, PubMed:16790427). {ECO:0000269|PubMed:14960568, ECO:0000269|PubMed:15549269, ECO:0000269|PubMed:16049012, ECO:0000269|PubMed:16790427, ECO:0000269|PubMed:19749753, ECO:0000269|PubMed:22529353}. The FieF protein is a member of the cation diffusion facilitator (CDF) family of metal cation transporters . FieF functions as a divalent metal cation transporter which exports Zn2+, Cd2+, and possibly Fe2+ but probably not Hg2+, Co2+, Ni2+, Mn2+, Ca2+ or Mg2+. Metal binding properties of the purified protein identifying zinc and cadmium as substrates have been described . FieF forms dimers in detergent-lipid micelles and in reconstituted membranes . The structure of FieF in complex with zinc has been determined by X-ray crystallography to a resolution of 3.8 Å. The FieF homodimer forms a 'Y'-shaped molecule in perpendicular orientation to the plane of the membrane...

## Biological Role

Component of Zn2+/Fe2+/Cd2+ exporter (complex.ecocyc.CPLX0-7641).

## Annotation

FUNCTION: Divalent metal cation transporter which exports Zn(2+), Cd(2+) and possibly Fe(2+) (PubMed:14960568, PubMed:15549269, PubMed:16049012, PubMed:16790427, PubMed:19749753, PubMed:22529353). May be involved in zinc and iron detoxification by efflux (PubMed:15549269, PubMed:19749753). In vitro, can also bind, but probably not transport, Hg(2+), Co(2+), Ni(2+), Mn(2+), Ca(2+) and Mg(2+) (PubMed:14960568, PubMed:16049012, PubMed:16790427). {ECO:0000269|PubMed:14960568, ECO:0000269|PubMed:15549269, ECO:0000269|PubMed:16049012, ECO:0000269|PubMed:16790427, ECO:0000269|PubMed:19749753, ECO:0000269|PubMed:22529353}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7641|complex.ecocyc.CPLX0-7641]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3915|gene.b3915]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69380`
- `KEGG:ecj:JW3886;eco:b3915;ecoc:C3026_21165;`
- `GeneID:75169355;75204588;948413;`
- `GO:GO:0005886; GO:0006879; GO:0006882; GO:0015086; GO:0015093; GO:0015341; GO:0034755; GO:0042802; GO:0046872; GO:0070574; GO:0071577; GO:0140826`

## Notes

Cation-efflux pump FieF (Ferrous-iron efflux pump FieF)
