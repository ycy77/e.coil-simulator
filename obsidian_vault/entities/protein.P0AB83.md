---
entity_id: "protein.P0AB83"
entity_type: "protein"
name: "nth"
source_database: "UniProt"
source_id: "P0AB83"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nth b1633 JW1625"
---

# nth

`protein.P0AB83`

## Static

- Type: `protein`
- Source: `UniProt:P0AB83`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: DNA repair enzyme that has both DNA N-glycosylase activity and AP-lyase activity. The DNA N-glycosylase activity releases various damaged pyrimidines from DNA by cleaving the N-glycosidic bond, leaving an AP (apurinic/apyrimidinic) site. The AP-lyase activity cleaves the phosphodiester bond 3' to the AP site by a beta-elimination, leaving a 3'-terminal unsaturated sugar and a product with a terminal 5'-phosphate. {ECO:0000255|HAMAP-Rule:MF_00942, ECO:0000269|PubMed:2449657, ECO:0000269|PubMed:2669955, ECO:0000269|PubMed:6371006}. Endonuclease III (Endo III or Nth) is a combined DNA glycosylase and apurinic/apyrimidinic (AP) lyase; Endo III cleaves the N-glycosidic bond of damaged pyrimidines to create AP sites and incises the phosphodiester backbone 3' to the abasic site to yield single strand breaks with 3'-unsaturated aldehydic and deoxyribonucleoside 5'-phosphoryl ends. The AP lyase activity of Endo III generates blocked 3' termini that are then processed by one of two AP endonucleases (EG11073-MONOMER "Exonuclease III" and EG10651-MONOMER "Endonuclease IV") to generate the 3' OH ends that are required for DNA polymerase repair synthesis (see ). Endonuclease III recognizes pyrimidine residues damaged by ring saturation, ring fragmentation or ring contraction...

## Biological Role

Catalyzes RXN-20478 (reaction.ecocyc.RXN-20478), RXN-21261 (reaction.ecocyc.RXN-21261), RXN0-2601 (reaction.ecocyc.RXN0-2601). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Enriched Pathways

- `eco03410` Base excision repair (KEGG)

## Annotation

FUNCTION: DNA repair enzyme that has both DNA N-glycosylase activity and AP-lyase activity. The DNA N-glycosylase activity releases various damaged pyrimidines from DNA by cleaving the N-glycosidic bond, leaving an AP (apurinic/apyrimidinic) site. The AP-lyase activity cleaves the phosphodiester bond 3' to the AP site by a beta-elimination, leaving a 3'-terminal unsaturated sugar and a product with a terminal 5'-phosphate. {ECO:0000255|HAMAP-Rule:MF_00942, ECO:0000269|PubMed:2449657, ECO:0000269|PubMed:2669955, ECO:0000269|PubMed:6371006}.

## Pathways

- `eco03410` Base excision repair (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-20478|reaction.ecocyc.RXN-20478]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-21261|reaction.ecocyc.RXN-21261]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-2601|reaction.ecocyc.RXN0-2601]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1633|gene.b1633]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB83`
- `KEGG:ecj:JW1625;eco:b1633;ecoc:C3026_09380;`
- `GeneID:86859603;93775785;947122;`
- `GO:GO:0000703; GO:0003677; GO:0003906; GO:0004844; GO:0006285; GO:0019104; GO:0034644; GO:0046872; GO:0051539; GO:0097510; GO:0140078`
- `EC:4.2.99.18`

## Notes

Endonuclease III (EC 4.2.99.18) (DNA-(apurinic or apyrimidinic site) lyase)
