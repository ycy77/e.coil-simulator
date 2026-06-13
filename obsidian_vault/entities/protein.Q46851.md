---
entity_id: "protein.Q46851"
entity_type: "protein"
name: "gpr"
source_database: "UniProt"
source_id: "Q46851"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gpr mgrA yghZ b3001 JW2970"
---

# gpr

`protein.Q46851`

## Static

- Type: `protein`
- Source: `UniProt:Q46851`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Aldo-keto reductase that catalyzes the stereospecific, NADPH-dependent reduction of L-glyceraldehyde 3-phosphate (L-GAP) to L-glycerol 3-phosphate (L-G3P) (PubMed:18620424). The physiological role of Gpr is the detoxification of L-GAP, which may be formed via non-enzymatic and/or enzymatic racemization of D-GAP (PubMed:18620424). Also contributes to cellular methylglyoxal detoxification by catalyzing the NADPH-dependent conversion of methylglyoxal to acetol (PubMed:12583903, PubMed:16077126). However, the catalytic efficiency of methylglyoxal reductase activity is more than 2 orders of magnitude lower than the L-GAP reductase activity (PubMed:18620424). In addition, exhibits activity with glyoxal and probably plays a significant role in detoxification of glyoxal in vivo (PubMed:23990306). Shows broad specificity and can use aromatic aldehydes such as 4-nitrobenzaldehyde and benzaldehyde, D,L-glyceraldehyde, phenylglyoxal, isatin and the model substrate 4-nitrobenzaldehyde (PubMed:12583903, PubMed:16077126). {ECO:0000269|PubMed:12583903, ECO:0000269|PubMed:16077126, ECO:0000269|PubMed:18620424, ECO:0000269|PubMed:23990306}. YghZ is an L-glyceraldehyde 3-phosphate (L-GAP) reductase ; the enzyme is also able to detoxify methylglyoxal at a low rate . YghZ defines the AKR14 (aldo-keto reductase 14) protein family . L-GAP is not a natural metabolite and is toxic to E...

## Biological Role

Catalyzes RXN0-4281 (reaction.ecocyc.RXN0-4281), RXN0-5410 (reaction.ecocyc.RXN0-5410).

## Annotation

FUNCTION: Aldo-keto reductase that catalyzes the stereospecific, NADPH-dependent reduction of L-glyceraldehyde 3-phosphate (L-GAP) to L-glycerol 3-phosphate (L-G3P) (PubMed:18620424). The physiological role of Gpr is the detoxification of L-GAP, which may be formed via non-enzymatic and/or enzymatic racemization of D-GAP (PubMed:18620424). Also contributes to cellular methylglyoxal detoxification by catalyzing the NADPH-dependent conversion of methylglyoxal to acetol (PubMed:12583903, PubMed:16077126). However, the catalytic efficiency of methylglyoxal reductase activity is more than 2 orders of magnitude lower than the L-GAP reductase activity (PubMed:18620424). In addition, exhibits activity with glyoxal and probably plays a significant role in detoxification of glyoxal in vivo (PubMed:23990306). Shows broad specificity and can use aromatic aldehydes such as 4-nitrobenzaldehyde and benzaldehyde, D,L-glyceraldehyde, phenylglyoxal, isatin and the model substrate 4-nitrobenzaldehyde (PubMed:12583903, PubMed:16077126). {ECO:0000269|PubMed:12583903, ECO:0000269|PubMed:16077126, ECO:0000269|PubMed:18620424, ECO:0000269|PubMed:23990306}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-4281|reaction.ecocyc.RXN0-4281]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5410|reaction.ecocyc.RXN0-5410]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3001|gene.b3001]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46851`
- `KEGG:ecj:JW2970;eco:b3001;ecoc:C3026_16410;`
- `GeneID:947480;`
- `GO:GO:0006974; GO:0008106; GO:0016616; GO:0051596; GO:1990002`
- `EC:1.1.1.-; 1.1.1.2`

## Notes

L-glyceraldehyde 3-phosphate reductase (L-GAP reductase) (EC 1.1.1.-) (AKR14A1) (Aldo-keto reductase YqhE) (EC 1.1.1.2) (Methylglyoxal reductase Gpr) (EC 1.1.1.-)
