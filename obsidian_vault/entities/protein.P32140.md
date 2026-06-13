---
entity_id: "protein.P32140"
entity_type: "protein"
name: "yihS"
source_database: "UniProt"
source_id: "P32140"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yihS b3880 JW5569"
---

# yihS

`protein.P32140`

## Static

- Type: `protein`
- Source: `UniProt:P32140`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the isomerization of sulfoquinovose (SQ) to 6-deoxy-6-sulfo-D-fructose (SF) (PubMed:24463506, PubMed:33791429). Can also catalyze the interconversion of SQ and sulforhamnose (SR) (PubMed:33791429). Has a clear preference for beta-SQ and little-to-no activity on alpha-SQ (PubMed:33791429). In vitro, can also catalyze the interconversion of mannose, fructose and glucose, or lyxose and xylulose, but has extremely low activity with glucose (PubMed:18328504). {ECO:0000269|PubMed:18328504, ECO:0000269|PubMed:24463506, ECO:0000269|PubMed:33791429}. Sulfoquinovose isomerase (YihS) catalyzes the isomerization to CPD-16501 , a part of the PWY-7446 pathway. YihS has mannose isomerase activity in vitro. Predicted active site residues were analyzed by site-directed mutagenesis. A crystal structure of the enzyme has been solved at 2.5 Å resolution . YihS may be identical to the enzyme first identified by , although the quarternary structure differs. The mannose isomerase identified in is a tetramer in solution, while YihS is a hexamer . Expression of YihS is induced by growth on sulfoquinovose and lactose . A yihS mutant is unable to grow on sulfoquinovose as the sole source of carbon . In the absence of ppGpp (ΔrelA spoT), overproduction of YihS reduces the growth rate and increases persistence .

## Biological Role

Catalyzes 6-deoxy-6-sulfo-D-glucopyranose isomerase (2-epimerizing); (reaction.R12996). Component of sulfoquinovose isomerase (complex.ecocyc.CPLX0-7683).

## Enriched Pathways

- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the isomerization of sulfoquinovose (SQ) to 6-deoxy-6-sulfo-D-fructose (SF) (PubMed:24463506, PubMed:33791429). Can also catalyze the interconversion of SQ and sulforhamnose (SR) (PubMed:33791429). Has a clear preference for beta-SQ and little-to-no activity on alpha-SQ (PubMed:33791429). In vitro, can also catalyze the interconversion of mannose, fructose and glucose, or lyxose and xylulose, but has extremely low activity with glucose (PubMed:18328504). {ECO:0000269|PubMed:18328504, ECO:0000269|PubMed:24463506, ECO:0000269|PubMed:33791429}.

## Pathways

- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R12996|reaction.R12996]] `KEGG` `database` - via EC:5.3.1.31
- `is_component_of` --> [[complex.ecocyc.CPLX0-7683|complex.ecocyc.CPLX0-7683]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b3880|gene.b3880]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32140`
- `KEGG:ecj:JW5569;eco:b3880;ecoc:C3026_20975;`
- `GeneID:75204551;948374;`
- `GO:GO:0005975; GO:0034214; GO:0042802; GO:0050089; GO:0061593; GO:0061720; GO:1902777`
- `EC:5.3.1.31`

## Notes

Sulfoquinovose isomerase (SQ isomerase) (EC 5.3.1.31) (Sulfoquinovose-sulfofructose isomerase) (SQ-SF isomerase)
