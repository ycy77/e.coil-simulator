---
entity_id: "protein.P09099"
entity_type: "protein"
name: "xylB"
source_database: "UniProt"
source_id: "P09099"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xylB b3564 JW3536"
---

# xylB

`protein.P09099`

## Static

- Type: `protein`
- Source: `UniProt:P09099`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of D-xylulose to D-xylulose 5-phosphate (PubMed:17123542). Also catalyzes the phosphorylation of 1-deoxy-D-xylulose to 1-deoxy-D-xylulose 5-phosphate, with lower efficiency (PubMed:11168365). Can also use D-ribulose, xylitol and D-arabitol, but D-xylulose is preferred over the other substrates (PubMed:17123542). Has a weak substrate-independent Mg-ATP-hydrolyzing activity (PubMed:17123542). {ECO:0000269|PubMed:11168365, ECO:0000269|PubMed:17123542}. Xylulokinase catalyzes the phosphorylation of D-xylulose, the second step in the xylose degradation pathway, producing D-xylulose-5-phosphate, an intermediate of the pentose phosphate pathway. In the absence of substrate, xylulokinase has weak ATPase activity . Xylulokinase can also catalyze the phosphorylation of 1-deoxy-D-xylulose. This would allow a potential salvage pathway for generating 1-deoxy-D-xylulose 5-phosphate for use in the biosynthesis of terpenoids, thiamine and pyridoxal . The kinetic mechanism of the enzyme has been studied, suggesting a predominantly ordered reaction mechanism. The enzyme undergoes significant conformational changes upon binding of the substrate and of ATP. Two conserved aspartate residues, D6 and D233, were found to be essential for catalytic activity, and a catalytic mechanism has been proposed...

## Biological Role

Component of xylulokinase (complex.ecocyc.CPLX0-7466).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorylation of D-xylulose to D-xylulose 5-phosphate (PubMed:17123542). Also catalyzes the phosphorylation of 1-deoxy-D-xylulose to 1-deoxy-D-xylulose 5-phosphate, with lower efficiency (PubMed:11168365). Can also use D-ribulose, xylitol and D-arabitol, but D-xylulose is preferred over the other substrates (PubMed:17123542). Has a weak substrate-independent Mg-ATP-hydrolyzing activity (PubMed:17123542). {ECO:0000269|PubMed:11168365, ECO:0000269|PubMed:17123542}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7466|complex.ecocyc.CPLX0-7466]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3564|gene.b3564]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09099`
- `KEGG:ecj:JW3536;eco:b3564;ecoc:C3026_19325;`
- `GeneID:948133;`
- `GO:GO:0004856; GO:0005524; GO:0005998; GO:0016301; GO:0042803; GO:0042843; GO:0103020`
- `EC:2.7.1.-; 2.7.1.17`

## Notes

Xylulose kinase (XK) (Xylulokinase) (EC 2.7.1.17) (1-deoxy-D-xylulokinase) (EC 2.7.1.-)
