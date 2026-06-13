---
entity_id: "protein.P23849"
entity_type: "protein"
name: "trkG"
source_database: "UniProt"
source_id: "P23849"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2022616}; Multi-pass membrane protein {ECO:0000269|PubMed:2022616}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "trkG b1363 JW1358"
---

# trkG

`protein.P23849`

## Static

- Type: `protein`
- Source: `UniProt:P23849`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2022616}; Multi-pass membrane protein {ECO:0000269|PubMed:2022616}.

## Enriched Summary

FUNCTION: Low-affinity potassium transport system. Interacts with Trk system potassium uptake protein TrkA. Requires TrkE (sapD) for maximal transport activity, low activity is seen in its absence; no further stimulation is seen with SapF (PubMed:11700350). Transport in the absence of SapD is dependent on a high membrane potential and a high cytoplasmic ATP concentration, suggesting this protein may be able to interact with other ATP-binding proteins (PubMed:11700350). Can transport potassium and rubidium (PubMed:7896723). {ECO:0000269|PubMed:11700350, ECO:0000269|PubMed:2022616, ECO:0000269|PubMed:2674131, ECO:0000269|PubMed:7896723}. TrkG is a Na+-dependent potassium ion transporter that makes a minor contribution to K+ uptake; TrkG-mediated uptake contributes to potassium replenishment when Na+ is present in the growth environment . Early studies in E. coli K-12 identified four separate K+ uptake systems: two constitutive systems [TrkA (also called Trk) and TrkD (also called Kup)], a high affinity system (Kdp) and a non-saturable system TrkF (see also . Although initially thought to be a single system TrkA/Trk activity was later shown to result from the activity of two K+ transporters which were named TRKG-MONOMER "TrkG" and TRKH-MONOMER "TrkH"...

## Biological Role

Catalyzes sodium:potassium symport (reaction.ecocyc.TRANS-RXN-188). Transports Potassium cation (molecule.C00238), Sodium cation (molecule.C01330).

## Annotation

FUNCTION: Low-affinity potassium transport system. Interacts with Trk system potassium uptake protein TrkA. Requires TrkE (sapD) for maximal transport activity, low activity is seen in its absence; no further stimulation is seen with SapF (PubMed:11700350). Transport in the absence of SapD is dependent on a high membrane potential and a high cytoplasmic ATP concentration, suggesting this protein may be able to interact with other ATP-binding proteins (PubMed:11700350). Can transport potassium and rubidium (PubMed:7896723). {ECO:0000269|PubMed:11700350, ECO:0000269|PubMed:2022616, ECO:0000269|PubMed:2674131, ECO:0000269|PubMed:7896723}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-188|reaction.ecocyc.TRANS-RXN-188]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1363|gene.b1363]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23849`
- `KEGG:ecj:JW1358;eco:b1363;ecoc:C3026_07970;`
- `GeneID:86859331;86946529;945932;`
- `GO:GO:0005267; GO:0005886; GO:0015079; GO:0015379; GO:0030955; GO:0071805`

## Notes

Trk system potassium uptake protein TrkG
