---
entity_id: "protein.P0ABR7"
entity_type: "protein"
name: "yeaW"
source_database: "UniProt"
source_id: "P0ABR7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yeaW b1802 JW5294"
---

# yeaW

`protein.P0ABR7`

## Static

- Type: `protein`
- Source: `UniProt:P0ABR7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Converts carnitine to trimethylamine and malic semialdehyde. Can also use gamma-butyrobetaine, choline and betaine as substrates. {ECO:0000269|PubMed:25440057}. Partially purified YeaW protein was shown to contain a [2Fe-2S] iron-sulfur cluster that can be reduced by dithionite, but not ascorbate, identifying it as a low-potential Rieske iron-sulfur cluster protein . When incubated together in the presence of NADH, YeaWX liberated TRIMETHYLAMINE from several substrates, including CARNITINE, GAMMA-BUTYROBETAINE and CHOLINE . It has not yet been determined whether a physical YeaWX complex exists.

## Biological Role

Catalyzes L-carnitine,NADPH:oxygen oxidoreductase (trimethylamine-forming) (reaction.R11911). Component of 2Fe-2S cluster-containing protein YeaW (complex.ecocyc.CPLX0-7675), carnitine monooxygenase (complex.ecocyc.CPLX0-8232).

## Annotation

FUNCTION: Converts carnitine to trimethylamine and malic semialdehyde. Can also use gamma-butyrobetaine, choline and betaine as substrates. {ECO:0000269|PubMed:25440057}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R11911|reaction.R11911]] `KEGG` `database` - via EC:1.14.13.239
- `is_component_of` --> [[complex.ecocyc.CPLX0-7675|complex.ecocyc.CPLX0-7675]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.CPLX0-8232|complex.ecocyc.CPLX0-8232]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1802|gene.b1802]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABR7`
- `KEGG:ecj:JW5294;eco:b1802;ecoc:C3026_10270;`
- `GeneID:93776050;946325;`
- `GO:GO:0005506; GO:0009437; GO:0016709; GO:0032991; GO:0042802; GO:0051537`
- `EC:1.14.13.239`

## Notes

Carnitine monooxygenase oxygenase subunit (EC 1.14.13.239) (Carnitine monooxygenase alpha subunit)
