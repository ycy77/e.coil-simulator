---
entity_id: "protein.P37769"
entity_type: "protein"
name: "kduD"
source_database: "UniProt"
source_id: "P37769"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kduD ygeC yqeD b2842 JW2810"
---

# kduD

`protein.P37769`

## Static

- Type: `protein`
- Source: `UniProt:P37769`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible reduction of 2,5-diketo-3-deoxygluconate (DKII or 4,6-dihydroxy-2,5-dioxohexanoate) into 2-keto-3-deoxygluconate (KDG or 2-dehydro-3-deoxygluconate) with a concomitant oxidation of NADH (Ref.4). To a lesser extent, can also reduce 5-keto-D-gluconate and oxidize D-gluconate and 1,2-propanediol (PubMed:24509771). Together with KduI, seems to play a role in the catabolism of hexuronates under osmotic stress conditions, substituting for the regular hexuronate degrading enzymes UxaABC and UxuAB whose expression is repressed in these conditions (PubMed:23437267). In vitro, also exhibits NADH-dependent 20-ketosteroid reductase activity against eukaryotic steroid hormone 11-deoxycorticosterone (11-DOC), which is converted into the product 4-pregnen-20,21-diol-3-one. In addition to 11-DOC, five other C21 steroid compounds (11-deoxycortisol, cortisol, corticosterone, cortisone, and 21-hydroxypregnenolone) are reduced by KduD, but steroids lacking the hydroxyl group at C21 position, such as pregnenolone, testosterone propionate, cortisone acetate, or progesterone, cannot be used as substrate (PubMed:24509771). {ECO:0000269|PubMed:23437267, ECO:0000269|PubMed:24509771, ECO:0000269|Ref.4}. KduD is predicted to encode a 2-keto-3-deoxy-D-gluconate dehydrogenase by sequence similarity to the enzyme from Erwinia chrysanthemi...

## Biological Role

Catalyzes 2-dehydro-3-deoxy-D-gluconate:NAD+ 5-oxidoreductase (reaction.R01542), 1.1.1.127-RXN (reaction.ecocyc.1.1.1.127-RXN), RXN-15607 (reaction.ecocyc.RXN-15607), RXN0-7101 (reaction.ecocyc.RXN0-7101).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible reduction of 2,5-diketo-3-deoxygluconate (DKII or 4,6-dihydroxy-2,5-dioxohexanoate) into 2-keto-3-deoxygluconate (KDG or 2-dehydro-3-deoxygluconate) with a concomitant oxidation of NADH (Ref.4). To a lesser extent, can also reduce 5-keto-D-gluconate and oxidize D-gluconate and 1,2-propanediol (PubMed:24509771). Together with KduI, seems to play a role in the catabolism of hexuronates under osmotic stress conditions, substituting for the regular hexuronate degrading enzymes UxaABC and UxuAB whose expression is repressed in these conditions (PubMed:23437267). In vitro, also exhibits NADH-dependent 20-ketosteroid reductase activity against eukaryotic steroid hormone 11-deoxycorticosterone (11-DOC), which is converted into the product 4-pregnen-20,21-diol-3-one. In addition to 11-DOC, five other C21 steroid compounds (11-deoxycortisol, cortisol, corticosterone, cortisone, and 21-hydroxypregnenolone) are reduced by KduD, but steroids lacking the hydroxyl group at C21 position, such as pregnenolone, testosterone propionate, cortisone acetate, or progesterone, cannot be used as substrate (PubMed:24509771). {ECO:0000269|PubMed:23437267, ECO:0000269|PubMed:24509771, ECO:0000269|Ref.4}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R01542|reaction.R01542]] `KEGG` `database` - via EC:1.1.1.127
- `catalyzes` --> [[reaction.ecocyc.1.1.1.127-RXN|reaction.ecocyc.1.1.1.127-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-15607|reaction.ecocyc.RXN-15607]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7101|reaction.ecocyc.RXN0-7101]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2842|gene.b2842]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37769`
- `KEGG:ecj:JW2810;eco:b2842;ecoc:C3026_15605;`
- `GeneID:947323;`
- `GO:GO:0008678; GO:0016616; GO:0019698; GO:0033764; GO:0042840; GO:0047001; GO:0051287; GO:0102635`
- `EC:1.1.1.-; 1.1.1.127`

## Notes

2-dehydro-3-deoxy-D-gluconate 5-dehydrogenase (EC 1.1.1.127) (2-deoxy-D-gluconate 3-dehydrogenase) (2-keto-3-deoxygluconate 5-dehydrogenase) (2-keto-3-deoxygluconate oxidoreductase) (KDG oxidoreductase) (20-ketosteroid reductase) (EC 1.1.1.-)
