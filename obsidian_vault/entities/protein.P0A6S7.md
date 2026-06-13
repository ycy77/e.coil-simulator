---
entity_id: "protein.P0A6S7"
entity_type: "protein"
name: "gpsA"
source_database: "UniProt"
source_id: "P0A6S7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00394}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gpsA b3608 JW3583"
---

# gpsA

`protein.P0A6S7`

## Static

- Type: `protein`
- Source: `UniProt:P0A6S7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00394}.

## Enriched Summary

FUNCTION: Catalyzes the reduction of the glycolytic intermediate dihydroxyacetone phosphate (DHAP) to sn-glycerol 3-phosphate (G3P), the key precursor for phospholipid synthesis (PubMed:28326, PubMed:355254, PubMed:4597451). Is able to use both NADPH and NADH with similar efficiency. Can also catalyze the reverse reaction in vitro (PubMed:28326). {ECO:0000269|PubMed:28326, ECO:0000269|PubMed:355254, ECO:0000269|PubMed:4597451}. Glycerol-3-phosphate dehydrogenase (GpsA) catalyzes the NAD(P)H-dependent reduction of the glycolytic intermediate dihydroxyacetone-phosphate to produce glycerol-3-phosphate, a precursor for the biosynthesis of phospholipids . GpsA activity is strongly inhibited in vitro by glycerol-3-phosphate, and it was shown that this inhibition does not involve dimer association or dissociation. A mutant version of the protein which is resistant to feedback inhibition has been studied . The enzyme is constitutively produced, and is present in the cell in low amounts. It was calculated that on average only about 1000 molecules are present per cell . GpsA did not show dehydrogenase activity in a high-throughput screen of purified proteins .

## Biological Role

Catalyzes sn-glycerol-3-phosphate:NAD+ 2-oxidoreductase (reaction.R00842), sn-glycerol-3-phosphate:NADP+ 2-oxidoreductase (reaction.R00844). Component of glycerol-3-phosphate dehydrogenase, biosynthetic (complex.ecocyc.GLYC3PDEHYDROGBIOSYN-CPLX).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the reduction of the glycolytic intermediate dihydroxyacetone phosphate (DHAP) to sn-glycerol 3-phosphate (G3P), the key precursor for phospholipid synthesis (PubMed:28326, PubMed:355254, PubMed:4597451). Is able to use both NADPH and NADH with similar efficiency. Can also catalyze the reverse reaction in vitro (PubMed:28326). {ECO:0000269|PubMed:28326, ECO:0000269|PubMed:355254, ECO:0000269|PubMed:4597451}.

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00842|reaction.R00842]] `KEGG` `database` - via EC:1.1.1.94
- `catalyzes` --> [[reaction.R00844|reaction.R00844]] `KEGG` `database` - via EC:1.1.1.94
- `is_component_of` --> [[complex.ecocyc.GLYC3PDEHYDROGBIOSYN-CPLX|complex.ecocyc.GLYC3PDEHYDROGBIOSYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3608|gene.b3608]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6S7`
- `KEGG:ecj:JW3583;eco:b3608;ecoc:C3026_19565;`
- `GeneID:93778322;948125;`
- `GO:GO:0005829; GO:0005975; GO:0006072; GO:0042803; GO:0046167; GO:0046168; GO:0046474; GO:0047952; GO:0051287; GO:0141152; GO:0141153`
- `EC:1.1.1.94`

## Notes

Glycerol-3-phosphate dehydrogenase [NAD(P)+] (EC 1.1.1.94) (NAD(P)(+)-dependent glycerol-3-phosphate dehydrogenase) (NAD(P)H-dependent dihydroxyacetone-phosphate reductase)
