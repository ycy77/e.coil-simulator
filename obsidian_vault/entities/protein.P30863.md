---
entity_id: "protein.P30863"
entity_type: "protein"
name: "dkgB"
source_database: "UniProt"
source_id: "P30863"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dkgB yafB b0207 JW0197"
---

# dkgB

`protein.P30863`

## Static

- Type: `protein`
- Source: `UniProt:P30863`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Aldo-keto reductase that significantly contributes to cellular methylglyoxal detoxification by catalyzing the NADPH-dependent conversion of methylglyoxal to acetol (PubMed:16077126). It also exhibits fairly high activity with glyoxal and probably plays a significant role in detoxification of glyoxal in vivo (PubMed:23990306). Shows broad specificity and can use aromatic aldehydes such as 4-nitrobenzaldehyde, 3-nitrobenzaldehyde and benzaldehyde, and phenylglyoxal (PubMed:16077126). Also catalyzes the reduction of 2,5-diketo-D-gluconic acid (25DKG) to 2-keto-L-gulonic acid (2KLG) and could be involved in ketogluconate metabolism (PubMed:10427017). However, the specific activity of the enzyme toward 2,5-diketo-D-gluconate was reported to be almost 400-fold lower than its activity toward methylglyoxal (PubMed:16077126). {ECO:0000269|PubMed:10427017, ECO:0000269|PubMed:16077126, ECO:0000269|PubMed:23990306}. DkgB is a member of the aldo-keto reductase (AKR) subfamily 3F . DkgB was shown by different authors to have 2,5-diketo-D-gluconate reductase , methylglyoxal reductase and 4-nitrobenzaldehyde reductase activities . dkgB was reported to encode 2,5-diketo-D-gluconate reductase (25DKGR) B, one of two 25DKG reductases in E. coli. The enzyme uses NADPH as the preferred electron donor and was thought to be involved in ketogluconate metabolism...

## Biological Role

Catalyzes 2-dehydro-L-idonate:NADP+ 5-oxidoreductase (reaction.R08878), RXN0-4281 (reaction.ecocyc.RXN0-4281), RXN0-5141 (reaction.ecocyc.RXN0-5141), RXN0-7020 (reaction.ecocyc.RXN0-7020).

## Annotation

FUNCTION: Aldo-keto reductase that significantly contributes to cellular methylglyoxal detoxification by catalyzing the NADPH-dependent conversion of methylglyoxal to acetol (PubMed:16077126). It also exhibits fairly high activity with glyoxal and probably plays a significant role in detoxification of glyoxal in vivo (PubMed:23990306). Shows broad specificity and can use aromatic aldehydes such as 4-nitrobenzaldehyde, 3-nitrobenzaldehyde and benzaldehyde, and phenylglyoxal (PubMed:16077126). Also catalyzes the reduction of 2,5-diketo-D-gluconic acid (25DKG) to 2-keto-L-gulonic acid (2KLG) and could be involved in ketogluconate metabolism (PubMed:10427017). However, the specific activity of the enzyme toward 2,5-diketo-D-gluconate was reported to be almost 400-fold lower than its activity toward methylglyoxal (PubMed:16077126). {ECO:0000269|PubMed:10427017, ECO:0000269|PubMed:16077126, ECO:0000269|PubMed:23990306}.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R08878|reaction.R08878]] `KEGG` `database` - via EC:1.1.1.346
- `catalyzes` --> [[reaction.ecocyc.RXN0-4281|reaction.ecocyc.RXN0-4281]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5141|reaction.ecocyc.RXN0-5141]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7020|reaction.ecocyc.RXN0-7020]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0207|gene.b0207]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30863`
- `KEGG:ecj:JW0197;eco:b0207;ecoc:C3026_00965;`
- `GeneID:75204936;944901;`
- `GO:GO:0005737; GO:0008106; GO:0047681; GO:0051596; GO:1990002`
- `EC:1.1.1.-; 1.1.1.2; 1.1.1.346`

## Notes

Methylglyoxal reductase DkgB (EC 1.1.1.-) (2,5-diketo-D-gluconic acid reductase B) (2,5-DKG reductase B) (2,5-DKGR B) (25DKGR-B) (EC 1.1.1.346) (AKR5D) (Aldo-keto reductase YafB) (EC 1.1.1.2)
