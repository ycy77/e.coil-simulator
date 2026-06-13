---
entity_id: "protein.P23522"
entity_type: "protein"
name: "garL"
source_database: "UniProt"
source_id: "P23522"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "garL yhaF b3126 JW3095"
---

# garL

`protein.P23522`

## Static

- Type: `protein`
- Source: `UniProt:P23522`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible retro-aldol cleavage of both 5-keto-4-deoxy-D-glucarate and 2-keto-3-deoxy-D-glucarate to pyruvate and tartronic semialdehyde (PubMed:9772162, Ref.5). In vitro, can catalyze the aldolisation reaction between hydroxypyruvate (HPA) or pyruvate (PA) and D-glyceraldehyde (D-GA) (Ref.7). The condensation of hydroxypyruvate and D-glyceraldehyde produces 2-dehydro-D-gluconate as the major product (Ref.7). The condensation of pyruvate and D-glyceraldehyde produces 2-dehydro-3-deoxy-L-galactonate as the major product and 2-dehydro-3-deoxy-D-gluconate (Ref.7). {ECO:0000269|PubMed:9772162, ECO:0000269|Ref.5, ECO:0000269|Ref.7}. α-dehydro-β-deoxy-D-glucarate aldolase cleaves both 5-dehydro-4-deoxy- and 2-dehydro-3-deoxy-D-glucarate, thereby continuing the catabolism of D-glucarate and D-galactarate . Crystal structures of the enzyme alone and in complex with pyruvate have been solved. The enzyme is a hexamer that may be assembled by association of three dimers .

## Biological Role

Component of α-dehydro-β-deoxy-D-glucarate aldolase (complex.ecocyc.CPLX0-7615).

## Enriched Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible retro-aldol cleavage of both 5-keto-4-deoxy-D-glucarate and 2-keto-3-deoxy-D-glucarate to pyruvate and tartronic semialdehyde (PubMed:9772162, Ref.5). In vitro, can catalyze the aldolisation reaction between hydroxypyruvate (HPA) or pyruvate (PA) and D-glyceraldehyde (D-GA) (Ref.7). The condensation of hydroxypyruvate and D-glyceraldehyde produces 2-dehydro-D-gluconate as the major product (Ref.7). The condensation of pyruvate and D-glyceraldehyde produces 2-dehydro-3-deoxy-L-galactonate as the major product and 2-dehydro-3-deoxy-D-gluconate (Ref.7). {ECO:0000269|PubMed:9772162, ECO:0000269|Ref.5, ECO:0000269|Ref.7}.

## Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7615|complex.ecocyc.CPLX0-7615]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b3126|gene.b3126]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23522`
- `KEGG:ecj:JW3095;eco:b3126;ecoc:C3026_17040;`
- `GeneID:947630;`
- `GO:GO:0000287; GO:0005737; GO:0008672; GO:0016830; GO:0016832; GO:0019394; GO:0042838; GO:0046392; GO:0061677`
- `EC:4.1.2.20`

## Notes

5-keto-4-deoxy-D-glucarate aldolase (KDGluc aldolase) (KDGlucA) (EC 4.1.2.20) (2-dehydro-3-deoxy-D-glucarate aldolase) (2-keto-3-deoxy-D-glucarate aldolase) (5-dehydro-4-deoxy-D-glucarate aldolase) (Alpha-keto-beta-deoxy-D-glucarate aldolase)
