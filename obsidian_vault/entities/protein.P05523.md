---
entity_id: "protein.P05523"
entity_type: "protein"
name: "mutM"
source_database: "UniProt"
source_id: "P05523"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mutM fpg b3635 JW3610"
---

# mutM

`protein.P05523`

## Static

- Type: `protein`
- Source: `UniProt:P05523`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in base excision repair of DNA damaged by oxidation or by mutagenic agents. Acts as a DNA glycosylase that recognizes and removes damaged bases. Has a preference for oxidized purines, such as 7,8-dihydro-8-oxoguanine (8-oxoG) and its derivatives such as guanidinohydantoin:C and spiroiminodihydantoin:C, however it also acts on thymine glycol:G, 5,6-dihydrouracil:G and 5-hydroxyuracil:G. Has AP (apurinic/apyrimidinic) lyase activity and introduces nicks in the DNA strand. Cleaves the DNA backbone by beta-delta elimination to generate a single-strand break at the site of the removed base with both 3'- and 5'-phosphates. Cleaves ssDNA containing an AP site. {ECO:0000269|PubMed:1689309, ECO:0000269|PubMed:20031487}. MutM (also known as Fpg or formamidopyrimidine glycosylase) is a bifunctional DNA glycosylase which cleaves the N-glycosidic bond of redox-damaged purines and incises the phosphodiester backbone to yield single strand breaks with 3' and 5'-phosphoryl ends; the reaction proceeds via formation of an enzyme-substrate Schiff base intermediate with subsequent β,δ-elimination reactions (see )...

## Biological Role

Catalyzes 3.2.2.23-RXN (reaction.ecocyc.3.2.2.23-RXN), RXN-18435 (reaction.ecocyc.RXN-18435), RXN-21266 (reaction.ecocyc.RXN-21266), RXN-21279 (reaction.ecocyc.RXN-21279).

## Enriched Pathways

- `eco03410` Base excision repair (KEGG)

## Annotation

FUNCTION: Involved in base excision repair of DNA damaged by oxidation or by mutagenic agents. Acts as a DNA glycosylase that recognizes and removes damaged bases. Has a preference for oxidized purines, such as 7,8-dihydro-8-oxoguanine (8-oxoG) and its derivatives such as guanidinohydantoin:C and spiroiminodihydantoin:C, however it also acts on thymine glycol:G, 5,6-dihydrouracil:G and 5-hydroxyuracil:G. Has AP (apurinic/apyrimidinic) lyase activity and introduces nicks in the DNA strand. Cleaves the DNA backbone by beta-delta elimination to generate a single-strand break at the site of the removed base with both 3'- and 5'-phosphates. Cleaves ssDNA containing an AP site. {ECO:0000269|PubMed:1689309, ECO:0000269|PubMed:20031487}.

## Pathways

- `eco03410` Base excision repair (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.3.2.2.23-RXN|reaction.ecocyc.3.2.2.23-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-18435|reaction.ecocyc.RXN-18435]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-21266|reaction.ecocyc.RXN-21266]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-21279|reaction.ecocyc.RXN-21279]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3635|gene.b3635]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P05523`
- `KEGG:ecj:JW3610;eco:b3635;ecoc:C3026_19700;`
- `GeneID:75202204;946765;`
- `GO:GO:0000703; GO:0003684; GO:0003906; GO:0004519; GO:0005737; GO:0006284; GO:0006974; GO:0008270; GO:0008534; GO:0019104; GO:0034039; GO:0046872; GO:0140078`
- `EC:3.2.2.23; 4.2.99.18`

## Notes

Formamidopyrimidine-DNA glycosylase (Fapy-DNA glycosylase) (EC 3.2.2.23) (DNA-(apurinic or apyrimidinic site) lyase MutM) (AP lyase MutM) (EC 4.2.99.18)
