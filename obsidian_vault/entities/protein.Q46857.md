---
entity_id: "protein.Q46857"
entity_type: "protein"
name: "dkgA"
source_database: "UniProt"
source_id: "Q46857"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dkgA yqhE b3012 JW5499"
---

# dkgA

`protein.Q46857`

## Static

- Type: `protein`
- Source: `UniProt:Q46857`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Aldo-keto reductase that significantly contributes to cellular methylglyoxal detoxification by catalyzing the NADPH-dependent conversion of methylglyoxal to acetol (PubMed:16077126, PubMed:16284956). It also exhibits fairly high activity with glyoxal (PubMed:23990306). Shows broad specificity and can use aromatic aldehydes such as 4-nitrobenzaldehyde, 3-nitrobenzaldehyde and benzaldehyde, and phenylglyoxal (PubMed:16077126). Shows beta-keto ester reductase activity toward ethyl acetoacetate and a variety of 2-substituted derivatives (PubMed:11934293). Also catalyzes the reduction of 2,5-diketo-D-gluconic acid (25DKG) to 2-keto-L-gulonic acid (2KLG) and could be involved in ketogluconate metabolism (PubMed:10427017). However, the specific activity of the enzyme toward 2,5-diketo-D-gluconate was reported to be almost 400-fold lower than its activity toward methylglyoxal (PubMed:16077126). Can catalyze in vitro the NADPH-dependent reduction of furfural, a natural product of lignocellulosic decomposition, to the less toxic product, furfuryl alcohol (PubMed:19429550). However, it is unlikely that furfural is a physiological substrate (PubMed:19429550). {ECO:0000269|PubMed:10427017, ECO:0000269|PubMed:11934293, ECO:0000269|PubMed:16077126, ECO:0000269|PubMed:16284956, ECO:0000269|PubMed:19429550, ECO:0000269|PubMed:23990306}...

## Biological Role

Catalyzes 2-dehydro-L-idonate:NADP+ 5-oxidoreductase (reaction.R08878), RXN0-1941 (reaction.ecocyc.RXN0-1941), RXN0-4281 (reaction.ecocyc.RXN0-4281), RXN0-7020 (reaction.ecocyc.RXN0-7020), RXN0-7119 (reaction.ecocyc.RXN0-7119).

## Annotation

FUNCTION: Aldo-keto reductase that significantly contributes to cellular methylglyoxal detoxification by catalyzing the NADPH-dependent conversion of methylglyoxal to acetol (PubMed:16077126, PubMed:16284956). It also exhibits fairly high activity with glyoxal (PubMed:23990306). Shows broad specificity and can use aromatic aldehydes such as 4-nitrobenzaldehyde, 3-nitrobenzaldehyde and benzaldehyde, and phenylglyoxal (PubMed:16077126). Shows beta-keto ester reductase activity toward ethyl acetoacetate and a variety of 2-substituted derivatives (PubMed:11934293). Also catalyzes the reduction of 2,5-diketo-D-gluconic acid (25DKG) to 2-keto-L-gulonic acid (2KLG) and could be involved in ketogluconate metabolism (PubMed:10427017). However, the specific activity of the enzyme toward 2,5-diketo-D-gluconate was reported to be almost 400-fold lower than its activity toward methylglyoxal (PubMed:16077126). Can catalyze in vitro the NADPH-dependent reduction of furfural, a natural product of lignocellulosic decomposition, to the less toxic product, furfuryl alcohol (PubMed:19429550). However, it is unlikely that furfural is a physiological substrate (PubMed:19429550). {ECO:0000269|PubMed:10427017, ECO:0000269|PubMed:11934293, ECO:0000269|PubMed:16077126, ECO:0000269|PubMed:16284956, ECO:0000269|PubMed:19429550, ECO:0000269|PubMed:23990306}.

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R08878|reaction.R08878]] `KEGG` `database` - via EC:1.1.1.346
- `catalyzes` --> [[reaction.ecocyc.RXN0-1941|reaction.ecocyc.RXN0-1941]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-4281|reaction.ecocyc.RXN0-4281]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7020|reaction.ecocyc.RXN0-7020]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7119|reaction.ecocyc.RXN0-7119]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3012|gene.b3012]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46857`
- `KEGG:ecj:JW5499;eco:b3012;ecoc:C3026_16465;`
- `GeneID:75173142;75203590;947495;`
- `GO:GO:0004032; GO:0005829; GO:0008106; GO:0016616; GO:0050580; GO:0051596; GO:1990002`
- `EC:1.1.1.-; 1.1.1.2; 1.1.1.346`

## Notes

Methylglyoxal reductase DkgA (EC 1.1.1.-) (2,5-diketo-D-gluconic acid reductase A) (2,5-DKG reductase A) (2,5-DKGR A) (25DKGR-A) (EC 1.1.1.346) (AKR5C) (Aldo-keto reductase YqhE) (EC 1.1.1.2) (Beta-keto ester reductase)
