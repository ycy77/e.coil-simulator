---
entity_id: "protein.P76254"
entity_type: "protein"
name: "yeaX"
source_database: "UniProt"
source_id: "P76254"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yeaX b1803 JW1792"
---

# yeaX

`protein.P76254`

## Static

- Type: `protein`
- Source: `UniProt:P76254`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Converts carnitine to trimethylamine and malic semialdehyde. Can also use gamma-butyrobetaine, choline and betaine as substrates. {ECO:0000269|PubMed:25440057}. When incubated together in the presence of NADH, YeaWX liberated TRIMETHYLAMINE from several substrates, including CARNITINE, GAMMA-BUTYROBETAINE and CHOLINE . It has not yet been determined whether a physical YeaWX complex exists.

## Biological Role

Catalyzes L-carnitine,NADPH:oxygen oxidoreductase (trimethylamine-forming) (reaction.R11911). Component of carnitine monooxygenase (complex.ecocyc.CPLX0-8232).

## Annotation

FUNCTION: Converts carnitine to trimethylamine and malic semialdehyde. Can also use gamma-butyrobetaine, choline and betaine as substrates. {ECO:0000269|PubMed:25440057}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R11911|reaction.R11911]] `KEGG` `database` - via EC:1.14.13.239
- `is_component_of` --> [[complex.ecocyc.CPLX0-8232|complex.ecocyc.CPLX0-8232]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1803|gene.b1803]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76254`
- `KEGG:ecj:JW1792;eco:b1803;ecoc:C3026_10275;`
- `GeneID:946329;`
- `GO:GO:0009437; GO:0016491; GO:0016709; GO:0046872; GO:0051537`
- `EC:1.14.13.239`

## Notes

Carnitine monooxygenase reductase subunit (EC 1.14.13.239) (Carnitine monooxygenase beta subunit)
