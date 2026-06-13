---
entity_id: "protein.P52006"
entity_type: "protein"
name: "nudI"
source_database: "UniProt"
source_id: "P52006"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nudI yfaO b2251 JW2245"
---

# nudI

`protein.P52006`

## Static

- Type: `protein`
- Source: `UniProt:P52006`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of nucleoside triphosphates, with a preference for pyrimidine deoxynucleoside triphosphates (dUTP, dTTP and dCTP). {ECO:0000269|PubMed:16766526}. NudI is a member of the Nudix hydrolase superfamily of nucleoside diphosphatases. The preferred substrate of the purified enzyme is dUTP, but it also shows 67 and 58% of activity with dTTP and dCTP, respectively . A recent analysis showed that geranyl diphosphate is a better substrate than dUTP . The enzyme is a monomer in solution . Preliminary crystallographic data for NudI from E. coli K-1 is available . In an effort to engineer novel biosynthetic pathways for 5-carbon alcohols, it was shown that NudI has a low level of isopentenyl pyrophosphate phosphatase activity in vitro, producing the desired intermediate 3-methyl-3-butenol . NudI can also dephosphorylate dimethylallyl pyrophosphate in vitro . Review:

## Biological Role

Catalyzes DCTP-PYROPHOSPHATASE-RXN (reaction.ecocyc.DCTP-PYROPHOSPHATASE-RXN), DUTP-PYROP-RXN (reaction.ecocyc.DUTP-PYROP-RXN), RXN-17104 (reaction.ecocyc.RXN-17104), RXN0-5107 (reaction.ecocyc.RXN0-5107).

## Annotation

FUNCTION: Catalyzes the hydrolysis of nucleoside triphosphates, with a preference for pyrimidine deoxynucleoside triphosphates (dUTP, dTTP and dCTP). {ECO:0000269|PubMed:16766526}.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.DCTP-PYROPHOSPHATASE-RXN|reaction.ecocyc.DCTP-PYROPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.DUTP-PYROP-RXN|reaction.ecocyc.DUTP-PYROP-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17104|reaction.ecocyc.RXN-17104]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5107|reaction.ecocyc.RXN0-5107]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2251|gene.b2251]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52006`
- `KEGG:ecj:JW2245;eco:b2251;ecoc:C3026_12575;`
- `GeneID:946740;`
- `GO:GO:0000287; GO:0004170; GO:0005737; GO:0016818; GO:0036218; GO:0047840`
- `EC:3.6.1.-; 3.6.1.12; 3.6.1.23; 3.6.1.9`

## Notes

Nucleoside triphosphatase NudI (EC 3.6.1.9) (Nucleotide diphosphatase NudI) (Pyrimidine deoxynucleoside triphosphate diphosphatase) (dCTP diphosphatase) (EC 3.6.1.12) (dTTP diphosphatase) (EC 3.6.1.-) (dUTP diphosphatase) (EC 3.6.1.23)
