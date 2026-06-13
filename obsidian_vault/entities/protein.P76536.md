---
entity_id: "protein.P76536"
entity_type: "protein"
name: "yfeX"
source_database: "UniProt"
source_id: "P76536"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:19564607}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yfeX b2431 JW2424"
---

# yfeX

`protein.P76536`

## Static

- Type: `protein`
- Source: `UniProt:P76536`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:19564607}.

## Enriched Summary

FUNCTION: Has both general peroxidase activity and dye-decolorizing activity. Can catalyze the oxidation of both protoporphyrinogen IX and coproporphyrinogen III to their corresponding porphyrins. Also efficiently decolorizes the dyes alizarin red and Cibacron blue F3GA. {ECO:0000269|PubMed:22068980}. YfeX belongs to the family of dye-decolorizing (DyP-type) peroxidases and is able to oxidize both protoporphyrinogen IX and coproporphyrinogen III to their corresponding porphyrins . A crystal structure of heme-bound YfeX from E. coli O157:H7 str. Sakai has been solved at 2.09 Å resolution. Site-directed mutagenesis of the predicted active site residues D143 And R232 indicate that their importance for catalysis is dependent on the substrate . The sequences of the E. coli O157:H7 str. Sakai and K-12 MG1655 proteins are 99% identical. Additional mutants in predicted active site residues were tested for heme binding ability . The authors of were unable to reproduce dechelation of iron from protoheme or mesoheme, disputing the results of , described below: Due to the lack of an outer membrane receptor for heme, E. coli K-12 is unable to utilize heme as a source of iron . However, expression of the heme receptor protein HasR from Serratia marcescens enables utilization of heme as a source of iron...

## Biological Role

Catalyzes PROTOHEMEFERROCHELAT-RXN (reaction.ecocyc.PROTOHEMEFERROCHELAT-RXN), RXN-11813 (reaction.ecocyc.RXN-11813), RXN0-7325 (reaction.ecocyc.RXN0-7325). Bound by a heme (molecule.ecocyc.Hemes).

## Annotation

FUNCTION: Has both general peroxidase activity and dye-decolorizing activity. Can catalyze the oxidation of both protoporphyrinogen IX and coproporphyrinogen III to their corresponding porphyrins. Also efficiently decolorizes the dyes alizarin red and Cibacron blue F3GA. {ECO:0000269|PubMed:22068980}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.PROTOHEMEFERROCHELAT-RXN|reaction.ecocyc.PROTOHEMEFERROCHELAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-11813|reaction.ecocyc.RXN-11813]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7325|reaction.ecocyc.RXN0-7325]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.Hemes|molecule.ecocyc.Hemes]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2431|gene.b2431]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76536`
- `KEGG:ecj:JW2424;eco:b2431;ecoc:C3026_13505;`
- `GeneID:946913;`
- `GO:GO:0004601; GO:0005737; GO:0005829; GO:0020037; GO:0046872`
- `EC:1.11.1.-`

## Notes

Dye-decolorizing peroxidase YfeX (EC 1.11.1.-) (Porphyrinogen oxidase)
