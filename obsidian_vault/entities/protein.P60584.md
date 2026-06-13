---
entity_id: "protein.P60584"
entity_type: "protein"
name: "caiA"
source_database: "UniProt"
source_id: "P60584"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01052, ECO:0000269|PubMed:8060125}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "caiA yaaO b0039 JW0038"
---

# caiA

`protein.P60584`

## Static

- Type: `protein`
- Source: `UniProt:P60584`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01052, ECO:0000269|PubMed:8060125}.

## Enriched Summary

FUNCTION: Catalyzes the reduction of crotonobetainyl-CoA to gamma-butyrobetainyl-CoA (PubMed:10209289, PubMed:10978161, PubMed:8060125). The electron donor could be the FixA/FixB complex (PubMed:12081978). {ECO:0000269|PubMed:10978161, ECO:0000269|PubMed:12081978, ECO:0000305|PubMed:10209289, ECO:0000305|PubMed:8060125}. Although E. coli K-12 does contain the cai genes, it can not utilize carnitine as a carbon or nitrogen source. However, under anaerobic conditions, carnitine can be metabolized to γ-butyrobetaine. The CaiA enzyme has been purified from the O44 K74 strain . In that strain, CaiA appears to be a homotetramer and forms a complex with CaiB, γ-butyrobetaine-CoA:carnitine CoA transferase . Expression of the cai operon is induced by carnitine and crotonobetaine under anaerobic conditions . demonstrated production of γ-butyrobetaine in an engineered L-carnitine-overproducing mutant of K-12 BW25113 and abolition of γ-butyrobetaine formation upon caiA deletion.

## Biological Role

Catalyzes CROBETREDUCT-RXN (reaction.ecocyc.CROBETREDUCT-RXN). Bound by FAD (molecule.C00016).

## Annotation

FUNCTION: Catalyzes the reduction of crotonobetainyl-CoA to gamma-butyrobetainyl-CoA (PubMed:10209289, PubMed:10978161, PubMed:8060125). The electron donor could be the FixA/FixB complex (PubMed:12081978). {ECO:0000269|PubMed:10978161, ECO:0000269|PubMed:12081978, ECO:0000305|PubMed:10209289, ECO:0000305|PubMed:8060125}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.CROBETREDUCT-RXN|reaction.ecocyc.CROBETREDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0039|gene.b0039]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P60584`
- `KEGG:ecj:JW0038;eco:b0039;ecoc:C3026_00205;`
- `GeneID:86862551;93777396;949064;`
- `GO:GO:0003995; GO:0005737; GO:0009437; GO:0033539; GO:0050660`
- `EC:1.3.8.13`

## Notes

Crotonobetainyl-CoA reductase (EC 1.3.8.13) (Crotobetaine reductase) (Crotonobetainyl-CoA dehydrogenase)
