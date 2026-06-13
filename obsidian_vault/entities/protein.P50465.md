---
entity_id: "protein.P50465"
entity_type: "protein"
name: "nei"
source_database: "UniProt"
source_id: "P50465"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nei b0714 JW0704"
---

# nei

`protein.P50465`

## Static

- Type: `protein`
- Source: `UniProt:P50465`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in base excision repair of DNA damaged by oxidation or by mutagenic agents. Acts as a DNA glycosylase that recognizes and removes damaged bases. Has a preference for oxidized pyrimidines, such as thymine glycol, 5,6-dihydrouracil and 5,6-dihydrothymine. Acts on DNA bubble and 3'-fork structures, suggesting a role in replication-associated DNA repair. Has AP (apurinic/apyrimidinic) lyase activity and introduces nicks in the DNA strand. Cleaves the DNA backbone by beta-delta elimination to generate a single-strand break at the site of the removed base with both 3'- and 5'-phosphates. {ECO:0000269|PubMed:20031487}. Endo VIII (purified initially from E. coli strain BW435 containing an nth deletion) has both DNA N-glycosylase and class I AP lyase activities; Endo VIII shares substrate specificity with EG10662-MONOMER "Endo III" - the product of nth . nei nth double deletion mutants have a strong mutator phenotype indicating that a significant number of premutagenic pyrimidine lesions are not repaired when cells lack both Endo VIII and Endo III . Purified Endo VIII recognises the oxidation products of cytosine and thymine; purified Endo VIII has 5' deoxyribophosphodiesterase activity...

## Biological Role

Catalyzes DNA-(apurinic or apyrimidinic site) lyase (Fpg type) (reaction.ecocyc.RXN-21250).

## Enriched Pathways

- `eco03410` Base excision repair (KEGG)

## Annotation

FUNCTION: Involved in base excision repair of DNA damaged by oxidation or by mutagenic agents. Acts as a DNA glycosylase that recognizes and removes damaged bases. Has a preference for oxidized pyrimidines, such as thymine glycol, 5,6-dihydrouracil and 5,6-dihydrothymine. Acts on DNA bubble and 3'-fork structures, suggesting a role in replication-associated DNA repair. Has AP (apurinic/apyrimidinic) lyase activity and introduces nicks in the DNA strand. Cleaves the DNA backbone by beta-delta elimination to generate a single-strand break at the site of the removed base with both 3'- and 5'-phosphates. {ECO:0000269|PubMed:20031487}.

## Pathways

- `eco03410` Base excision repair (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-21250|reaction.ecocyc.RXN-21250]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0714|gene.b0714]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P50465`
- `KEGG:ecj:JW0704;eco:b0714;ecoc:C3026_03570;`
- `GeneID:945320;`
- `GO:GO:0000703; GO:0003684; GO:0003906; GO:0006284; GO:0008270; GO:0140078`
- `EC:3.2.2.-; 4.2.99.18`

## Notes

Endonuclease 8 (DNA glycosylase/AP lyase Nei) (EC 3.2.2.-, EC 4.2.99.18) (DNA-(apurinic or apyrimidinic site) lyase Nei) (Endonuclease VIII)
