---
entity_id: "protein.P41407"
entity_type: "protein"
name: "azoR"
source_database: "UniProt"
source_id: "P41407"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "azoR acpD b1412 JW1409"
---

# azoR

`protein.P41407`

## Static

- Type: `protein`
- Source: `UniProt:P41407`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Quinone reductase that provides resistance to thiol-specific stress caused by electrophilic quinones. Can reduce several benzo-, naphtho-, and anthraquinone compounds. {ECO:0000269|PubMed:19666717}.; FUNCTION: Also exhibits azoreductase activity (PubMed:11583992, PubMed:18337254). Catalyzes the reductive cleavage of the azo bond in aromatic azo compounds to the corresponding amines (PubMed:11583992, PubMed:18337254). Can reduce ethyl red, methyl red and p-methyl red, but is not able to convert sulfonated azo dyes (PubMed:11583992, PubMed:18337254, PubMed:23795903). The stoichiometry implies that 2 cycles of the ping-pong mechanism are required for the cleavage of the azo bond (PubMed:11583992). Can also act as a nitroreductase and is able to reduce nitro compounds such as 7-nitrocoumarin-3-carboxylic acid (7NCCA) (PubMed:23795903). {ECO:0000269|PubMed:11583992, ECO:0000269|PubMed:18337254, ECO:0000269|PubMed:23795903}. AzoR is an NADH:quinone oxidoreductase with a role in protection against thiol-specific stress. Purified AzoR is active on a variety of electrophilic quinones . Purified AzoR also has azoreductase activity ; it is the major azoreductase under aerobic conditions . Compounds containing azo bonds (N=N) have environmental and clinical significance and thus proteins with azoreductase activity are subjects of experimental interest...

## Biological Role

Catalyzes N,N-dimethyl-1,4-phenylenediamine,anthranilate:NAD+ oxidoreductase (reaction.R12035). Component of FMN dependent NADH:quinone oxidoreductase (complex.ecocyc.CPLX0-7693).

## Annotation

FUNCTION: Quinone reductase that provides resistance to thiol-specific stress caused by electrophilic quinones. Can reduce several benzo-, naphtho-, and anthraquinone compounds. {ECO:0000269|PubMed:19666717}.; FUNCTION: Also exhibits azoreductase activity (PubMed:11583992, PubMed:18337254). Catalyzes the reductive cleavage of the azo bond in aromatic azo compounds to the corresponding amines (PubMed:11583992, PubMed:18337254). Can reduce ethyl red, methyl red and p-methyl red, but is not able to convert sulfonated azo dyes (PubMed:11583992, PubMed:18337254, PubMed:23795903). The stoichiometry implies that 2 cycles of the ping-pong mechanism are required for the cleavage of the azo bond (PubMed:11583992). Can also act as a nitroreductase and is able to reduce nitro compounds such as 7-nitrocoumarin-3-carboxylic acid (7NCCA) (PubMed:23795903). {ECO:0000269|PubMed:11583992, ECO:0000269|PubMed:18337254, ECO:0000269|PubMed:23795903}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R12035|reaction.R12035]] `KEGG` `database` - via EC:1.7.1.17
- `is_component_of` --> [[complex.ecocyc.CPLX0-7693|complex.ecocyc.CPLX0-7693]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1412|gene.b1412]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P41407`
- `KEGG:ecj:JW1409;eco:b1412;ecoc:C3026_08225;`
- `GeneID:947569;`
- `GO:GO:0005829; GO:0006979; GO:0009055; GO:0010181; GO:0016652; GO:0016655; GO:0042803; GO:0050446`
- `EC:1.6.5.-; 1.7.1.17`

## Notes

FMN-dependent NADH:quinone oxidoreductase (EC 1.6.5.-) (Azo-dye reductase) (FMN-dependent NADH-azo compound oxidoreductase) (FMN-dependent NADH-azoreductase) (EC 1.7.1.17)
