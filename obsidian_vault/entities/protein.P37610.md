---
entity_id: "protein.P37610"
entity_type: "protein"
name: "tauD"
source_database: "UniProt"
source_id: "P37610"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tauD ssiD yaiG b0368 JW0360"
---

# tauD

`protein.P37610`

## Static

- Type: `protein`
- Source: `UniProt:P37610`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the alpha-ketoglutarate-dependent hydroxylation of taurine yielding sulfite and aminoacetaldehyde after decomposition of an unstable intermediate (PubMed:9287300). Is required for the utilization of taurine (2-aminoethanesulfonate) as an alternative sulfur source for growth in the absence of sulfate (PubMed:8808933). To a lesser extent, pentanesulfonate, 3-(N-morpholino)propanesulfonate and 1,3-dioxo-2-isoindolineethanesulfonate are also desulfonated by this enzyme in vitro; however, desulfonation by TauD of organosulfonates other than taurine seem to be of little or no importance for sulfur metabolism in vivo (PubMed:9287300). {ECO:0000269|PubMed:8808933, ECO:0000269|PubMed:9287300}.

## Biological Role

Catalyzes taurine,2-oxoglutarate:O2 oxidoreductase (sulfite-forming) (reaction.R05320). Component of α-ketoglutarate-dependent taurine dioxygenase (complex.ecocyc.CPLX0-227).

## Enriched Pathways

- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the alpha-ketoglutarate-dependent hydroxylation of taurine yielding sulfite and aminoacetaldehyde after decomposition of an unstable intermediate (PubMed:9287300). Is required for the utilization of taurine (2-aminoethanesulfonate) as an alternative sulfur source for growth in the absence of sulfate (PubMed:8808933). To a lesser extent, pentanesulfonate, 3-(N-morpholino)propanesulfonate and 1,3-dioxo-2-isoindolineethanesulfonate are also desulfonated by this enzyme in vitro; however, desulfonation by TauD of organosulfonates other than taurine seem to be of little or no importance for sulfur metabolism in vivo (PubMed:9287300). {ECO:0000269|PubMed:8808933, ECO:0000269|PubMed:9287300}.

## Pathways

- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R05320|reaction.R05320]] `KEGG` `database` - via EC:1.14.11.17
- `is_component_of` --> [[complex.ecocyc.CPLX0-227|complex.ecocyc.CPLX0-227]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0368|gene.b0368]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37610`
- `KEGG:ecj:JW0360;eco:b0368;`
- `GeneID:945021;`
- `GO:GO:0000908; GO:0005737; GO:0006790; GO:0008198; GO:0019529; GO:0031418; GO:0042802; GO:0051289; GO:1990205`
- `EC:1.14.11.17`

## Notes

Alpha-ketoglutarate-dependent taurine dioxygenase (EC 1.14.11.17) (2-aminoethanesulfonate dioxygenase) (Sulfate starvation-induced protein 3) (SSI3)
